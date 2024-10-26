from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    
    turtle_teleop_key_node = Node(
        package='turtlesim',
        executable='turtle_teleop_key',
        name='turtle_teleop_key_node',
         prefix = 'xterm -e',
        output='screen',
        remappings=[('/turtle1/cmd_vel', '/RosAria/cmd_vel')]
    )
    
    return LaunchDescription([
        turtle_teleop_key_node,
    ])
