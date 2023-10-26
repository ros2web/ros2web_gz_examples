# ros2web_gz_examples

## Dependencies

- `ROS2` (>= Humble)
- `Gazebo` (>= Garden)
- [`ros_gz`](https://github.com/gazebosim/ros_gz)
- [`ros2web`](https://github.com/ros2web/ros2web)
- [`ros2web_app`](https://github.com/ros2web/ros2web_app)


## Installation
```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src
git clone https://github.com/ros2web/ros2web_gz_examples
cd ~/ros2_ws
colcon build --symlink-install
. ./install/local_setup.bash
```

## Usage
```bash
# Start the Gazebo
ros2 launch gz_simple_robot robot.launch.py

# Star the simple_robot (another terminal)
ros2 run simple_robot simple_robot

# Star ros2web (another terminal)
ros2 web server --no-auth
```

Access the following URL.

http://localhost:8080/simple_robot


