from os import environ, path

from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

from launch import LaunchDescription

# Running imu and diff drive controller node with sudo due to needing
# GPIO. This will also pass in relevant environment variables when launching
# the nodes

# This will run on odroid with passwordless sudo
prefixes = [
    'LD_LIBRARY_PATH', 'AMENT_PREFIX_PATH', 'ROS_VERSION',
    'ROS_PYTHON_VERSION', 'PYTHONPATH', 'PATH', 'ROS_DISTRO'
]
prefixes = [prefix + '=' + environ[prefix] for prefix in prefixes]
node_prefix = 'sudo ' + ' '.join(prefixes)


def generate_launch_description():
    return LaunchDescription([
        # Node(
        #     prefix=node_prefix,
        #     package='imu_adafruit_bno055',
        #     node_executable='imu_bno055_publisher',
        #     output='screen',
        #     parameters=[
        #         {"calibration_data_path": path.join(get_package_share_directory('rover_base'), 'imu_calibration',
        #                                             'calibration_data.dat')}
        #     ],
        # ),
        Node(
            prefix=node_prefix,
            package='motor_controls',
            node_executable='diff_drive_controller_node',
            output='screen',
            parameters=[
                path.join(get_package_share_directory('rover_base'), 'config',
                          'diff_drive_controller.yaml')
            ],
        ),
        # Node(package='tf2_ros',
        #      node_executable='static_transform_publisher',
        #      output='screen',
        #      arguments=[
        #          '0', '0', '0.03', '0', '0', '0', 'base_link',
        #          'imu_bno055_link'
        #      ]),
        # Node(package='tf2_ros',
        #      node_executable='static_transform_publisher',
        #      output='screen',
        #      arguments=[
        #          '0.2', '0', '0.05', '0', '0', '0', 'base_link',
        #          'laser_frame'
        #      ]),
        # Node(package='tf2_ros',
        #      node_executable='static_transform_publisher',
        #      output='screen',
        #      arguments=[
        #          '0.06', '0.02', '0.05', '0', '0', '0', 'base_link',
        #          'camera_pose_optical_frame'
        #      ]),
        # Node(package='tf2_ros',
        #      node_executable='static_transform_publisher',
        #      output='screen',
        #      arguments=[
        #          '0.06', '0.02', '0.07', '0', '0', '0', 'base_link',
        #          'd435_link'
        #      ]),
        # Node(
        #     package='slam_toolbox',
        #     node_executable='async_slam_toolbox_node',
        #     name='slam_toolbox',
        #     output='screen',
        #     parameters=[
        #         path.join(get_package_share_directory('rover_base'), 'config',
        #                   'mapper_params_online_async.yaml')
        #     ],
        # ),
        # Node(
        #     package='robot_localization',
        #     node_executable='ekf_node',
        #     name='ekf_filter_node',
        #     output='screen',
        #     parameters=[
        #         path.join(get_package_share_directory('rover_base'), 'config',
        #                   'ekf.yaml')
        #     ],
        # ),
        # Node(
        #     name='rplidar',
        #     package='rplidar_ros',
        #     node_executable='rplidar',
        #     output='screen',
        #     parameters=[{
        #         path.join(get_package_share_directory('rover_base'), 'config',
        #                   'rplidar.yaml')
        #     }],
        # ),
        # Node(
        #     package='realsense_node',
        #     node_executable='realsense_node',
        #     namespace="/t265",
        #     output='screen',
        #     parameters=[
        #         path.join(get_package_share_directory('rover_base'), 'config',
        #                   'realsense.yaml')
        #     ]
        # ),
        # Node(
        #     package='realsense_node',
        #     node_executable='realsense_node',
        #     namespace="/d435",
        #     output='screen',
        #     parameters=[
        #         path.join(get_package_share_directory('rover_base'), 'config',
        #                   'realsense.yaml')
        #     ]
        # ),
        # Node(
        #     package='rover_base',
        #     node_executable='timestamped_key_teleop',
        #     name='timestamped_key_teleop_node',
        #     output='screen',
        # ),
    ])
