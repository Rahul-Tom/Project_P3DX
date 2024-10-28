from launch import LaunchDescription
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    twist_mux_params = os.path.join(get_package_share_directory('p3dx_navigation'),'config','twist_mux.yaml')

    twist_mux_node = Node(
        package='twist_mux',
        executable='twist_mux',
        name='twist_mux_node',
        output='screen',
        parameters=[twist_mux_params],
        remappings=[('/cmd_vel_out', 'RosAria/cmd_vel')]
    )
    
    return LaunchDescription([
        twist_mux_node,
    ])
