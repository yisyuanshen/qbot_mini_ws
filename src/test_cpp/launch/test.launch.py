import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    return LaunchDescription([
        Node(
            package='test_py',
            executable='talker',
            name='talker_py',
            output='screen',
        ),

        Node(
            package='test_cpp',
            executable='listener',
            name='listener_cpp',
            output='screen',
        )
    ])