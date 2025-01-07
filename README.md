# Assignment 2 part 1

## Run it

roslaunch rt_12_part1 assignment1_modified.launch

## Implemented
- pub_pos_vit.py publishes the robot position and velocity by relying on the values published on the topic /odom (should be a custom message, also, could be displayed on the terminal every second for example)
- msg/RobotOdom.msg created for pub_pos_vit.py
- CMakeLists.txt modified to create custom messages (To be done)
- set_target.py (to be implemented)
- last_target.py (to be implemented)
