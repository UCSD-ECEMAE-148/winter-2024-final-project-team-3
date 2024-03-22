import rclpy
from rclpy.node import Node
from rclpy.duration import Duration
from roboflowoak import RoboflowOak
import cv2
import time
import numpy as np
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32, Int32


class RoboflowOakNode(Node):
  def __init__(self):
    super().__init__('duck_model')

    # Stretched resolution for faster processing
    self.desired_width = 480
    self.desired_height = 480

    # Instantiate RoboflowOak object
    self.rf = RoboflowOak(model="duck-locator", confidence=0.89, overlap=0.5,
                version="4", api_key="kRDWKAMr0bBMM48sYY2L", rgb=True,
                depth=False, device=None, blocking=True)

    # Publishers for sending control commands
    self.twist_publisher = self.create_publisher(Twist, '/cmd_vel', 10)
    self.twist_cmd = Twist() # Create Twist message for control commands

    # Parameter initialization
    self.declare_parameters(
      namespace='',
      parameters=[
        ('Kp_steering', 1),
        ('Ki_steering', 0),
        ('Kd_steering', 0.0006),
        ('error_threshold', 0.01),
        ('zero_throttle', 0.3),
        ('max_throttle', 0.25),
        ('min_throttle', 0.12),
        ('max_right_steering', 1.0),
        ('max_left_steering', -1.0)
      ])
    self.Kp = self.get_parameter('Kp_steering').value
    self.Ki = self.get_parameter('Ki_steering').value
    self.Kd = self.get_parameter('Kd_steering').value
    self.error_threshold = self.get_parameter('error_threshold').value
    self.zero_throttle = self.get_parameter('zero_throttle').value
    self.max_throttle = self.get_parameter('max_throttle').value
    self.min_throttle = self.get_parameter('min_throttle').value
    self.max_right_steering = self.get_parameter('max_right_steering').value
    self.max_left_steering = self.get_parameter('max_left_steering').value

    # PID control initialization
    self.Ts = float(1/20)
    self.ek = 0 # Current error
    self.ek_1 = 0 # Previous error
    self.proportional_error = 0
    self.derivative_error = 0
    self.integral_error = 0
    self.integral_max = 1E-8

    self.get_logger().info(
      f'\nKp_steering: {self.Kp}'
      f'\nKi_steering: {self.Ki}'
      f'\nKd_steering: {self.Kd}'
      f'\nerror_threshold: {self.error_threshold}'
      f'\nzero_throttle: {self.zero_throttle}'
      f'\nmax_throttle: {self.max_throttle}'
      f'\nmin_throttle: {self.min_throttle}'
      f'\nmax_right_steering: {self.max_right_steering}'
      f'\nmax_left_steering: {self.max_left_steering}'
    )


  def run(self):
    circle_mode=True
    while rclpy.ok():
      t0 = time.time()
      result, frame, _, _ = self.rf.detect()
      predictions = result["predictions"]

      # timing: for benchmarking purposes
      t = time.time() - t0

      # Logs the FPS and Predictions
      self.get_logger().info('FPS: %.2f' % (1/t))

      # Resize frame for faster processing (replace with desired_width and desired_height from init)
      frame = cv2.resize(frame, (self.desired_width, self.desired_height), interpolation=cv2.INTER_AREA)

      # Draw vertical centerline
      center_x = frame.shape[1] // 2 # Center x-coordinate
      cv2.line(frame, (center_x, 0), (center_x, frame.shape[0]), (0, 255, 0), 1) # Center line


      for prediction in predictions:
        prediction_x = int(prediction.x)
        prediction_y = int(prediction.y)

        # Calculate horizontal distance from centerline to prediction.x
        center_x = frame.shape[1] // 2 # Center x-coordinate
        distance_from_center = ((prediction_x - center_x)/ center_x)

        cv2.line(frame, (center_x, frame.shape[0] // 2), (prediction_x, prediction_y), (0, 0, 255), 1)



        # Log the prediction with signed distance
        self.get_logger().info('PREDICTIONS: %s, DISTANCE_FROM_CENTER: %d' % (prediction.json(), distance_from_center))


      if circle_mode:
        # Drive in a circle while looking for the duck
        self.twist_cmd.linear.x = 0.2  # Set a constant linear velocity
        self.twist_cmd.angular.z = 0.9  # Set a constant angular velocity for circling
        self.twist_publisher.publish(self.twist_cmd)


         # Check if a duck is detected
      if len(predictions) > 0:
        # Stop circling and switch to driving towards the duck
        circle_mode = False
        self.get_logger().info('I found you Mommy!')
        # Call the controller function with distance_from_center as input
        distance_from_center_float = float(distance_from_center)  # Convert to float
        self.controller(Float32(data=distance_from_center_float))
        # Check if duck is within the top 70 rows (assuming desired_height is set)
        if prediction_y < 100:
          # Stop steering and set throttle to zero
          self.twist_cmd.angular.z = 0.0  # Set steering to zero
          self.twist_cmd.linear.x = 0.0  # Set throttle to zero
          self.twist_publisher.publish(self.twist_cmd)
          self.get_logger().info('I found you Mommy!')

      if circle_mode==False and len(predictions) == 0:
        circle_mode=True


      cv2.imshow("frame", frame)

      if cv2.waitKey(1) == ord('q'):
        break

  def controller(self, data):
    # setting up PID control
    self.ek = data.data

    # Throttle gain scheduling (function of error)
    self.inf_throttle = self.min_throttle - (self.min_throttle - self.max_throttle) / (1 - self.error_threshold)
    throttle_float_raw = ((self.min_throttle - self.max_throttle) / (1 - self.error_threshold)) * abs(self.ek) + self.inf_throttle
    throttle_float = self.clamp(throttle_float_raw, self.max_throttle, self.min_throttle)

    # Steering PID terms
    self.proportional_error = self.Kp * self.ek
    self.derivative_error = self.Kd * (self.ek - self.ek_1) / self.Ts
    self.integral_error += self.Ki * self.ek * self.Ts
    self.integral_error = self.clamp(self.integral_error, self.integral_max)
    steering_float_raw = self.proportional_error + self.derivative_error + self.integral_error
    steering_float = self.clamp(steering_float_raw, self.max_right_steering, self.max_left_steering)

    # Publish values
    try:
      # publish control signals
      self.twist_cmd.angular.z = steering_float
      self.twist_cmd.linear.x = throttle_float
      self.twist_publisher.publish(self.twist_cmd)

      # shift current time and error values to previous values
      self.ek_1 = self.ek

    except KeyboardInterrupt:
      self.twist_cmd.linear.x = self.zero_throttle
      self.twist_publisher.publish(self.twist_cmd)

  def clamp(self, value, upper_bound, lower_bound=None):
    if lower_bound==None:
      lower_bound = -upper_bound # making lower bound symmetric about zero
    if value < lower_bound:
      value_c = lower_bound
    elif value > upper_bound:
      value_c = upper_bound
    else:
      value_c = value
    return value_c

def main(args=None):
  rclpy.init(args=args)
  duck_model = RoboflowOakNode()
  duck_model.run()
  rclpy.shutdown()

if __name__ == '__main__':
  main()
