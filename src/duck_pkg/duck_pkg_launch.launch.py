import os
from launch import LaunchDescription
from launch_ros.actions import Node




def generate_launch_description():
   package_name = 'duck_pkg'


   ld = LaunchDescription()


   RoboflowOakNode = Node(
           package=package_name,
           executable='duck_model',
           output='screen')


   ld.add_action(RoboflowOakNode)
   return ld
