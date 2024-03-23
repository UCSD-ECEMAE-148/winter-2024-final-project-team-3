# duck_pkg

This ROS2 package is designed to control and navigate a robot toward a detected duck using object detection and PID control.

Contents
* `duck_model.py`

This Python script defines the `RoboflowOakNode` class, which inherits from the `Node` class of `rclpy`. It is responsible for the following functionalities:

1. **Importing Dependencies**: Imports necessary Python modules and ROS2 libraries for object detection, control, and publishing commands.
2. **Initializing RoboflowOakNode Class**: Defines the `RoboflowOakNode` class, which initializes parameters for object detection, PID control, and creates a publisher for sending velocity commands.
3. **Object Detection and Visualization**: The `run` method continuously captures frames from a camera, resizes them for faster processing, and uses the `RoboflowOak` object to detect ducks in the frame. The detected ducks are visualized on the frame, and their distance from the center is calculated and logged.
4. **Control Logic**: If a duck is detected, the code switches from a circling mode to a driving mode. The `controller` method is called, which implements a PID (Proportional-Integral-Derivative) control algorithm to steer the robot toward the detected duck. The PID terms are calculated based on the duck's distance from the center, and the resulting steering and throttle values are published to the `/cmd_vel` topic.
5. **Termination and Clamping**: If the duck is detected within the top 70 rows (assuming the duck is close enough), the steering and throttle values are set to zero to stop the robot. The `clamp` function is used to limit the steering and throttle values within a specified range. The program can be terminated by pressing the 'q' key while displaying the frame.

Usage
To run the `duck_model.py` script, navigate to the `ros2_ws` directory and execute the following command:
  > ```ros2 launch ucsd_robocar_nav2_pkg all_nodes.launch.py```

This will start `RoboflowOakNode` and begin the object detection and control process.
