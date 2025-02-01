# Assignment 2 part 1 (Updated)

## Launch the simulation
It might be convenient to rename the package rt_12_part1 in assignment_2_2024 while cloning it.
Launch the simulation with:

**roslaunch assignment_2_2024 assignment1_modified.launch**

As a result, you should see
- a window with gazebo simulating the robot and its environment ;
- a window with Rviz ;
- a terminal showing the position (x,y) and the velocity (Vx,Wz) of the robot every second _pub_pos_vit.py_ (pub/sub using a custom message built from the topic /odom);
- a terminal to set or cancel new targets, with a message explaining how to do so _set_target.py_ (action client using feedback status to know when the target has been reached);
- a terminal for the output of the service node _last_target_, which shows the coordinates (x,y) of the last target sent by the user (service returning the coordinates of the last target when called). The node should be called on a terminal by **rosservice call /last_target** whenever the user wants information on the last node.
