# Assignment 2 part 1

## Run it

roslaunch rt_12_part1 assignment1_modified.launch

## Implemented
- pub_pos_vit.py publishes the robot position and velocity by relying on the values published on the topic /odom (should be the custom message RoborOdom.msg, also, could be displayed on the terminal every second for example)
- msg/RobotOdom.msg created for pub_pos_vit.py (not in the CMakeLists.txt yet)
- CMakeLists.txt modified to create custom messages (To be done - did not work at the moment so not commited)
- set_target.py (only the beginning)
- last_target.py (only the beginning)
