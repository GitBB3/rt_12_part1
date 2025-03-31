#!/usr/bin/env python

"""
.. module: pub_pos_vit
   :platform: unix
   :synopsis: Python node publishing the robot position and velocity as a custom message (x, y, x_vel, vel_z), by relying on the values published on the topic */odom*.
   
.. moduleauthor:: Bertille Beaujean <beaujean.bertille@orange.fr>

ROS node to publish the odometry of the robot. The node publishes the
robot position and velocity as a custom message (x,y, vel_x, vel_z), by relying on the values published on the
topic /odom.

**Subscribes to**:
/odom topic where the simulator publishes the robot position

**Publishes to**:
/robot_odom the desired components of the odometry of the robot

"""

import rospy
import actionlib
from nav_msgs.msg import Odometry
from assignment_2_2024.msg import RobotOdom

robot_state = RobotOdom()


def odom_callback(msg):
	"""This function reads the relevant position and velocity sent through the message *msg*, which should be the information from the topic */odom*. Then, it updates the values of the *robot_state* which is a custom message of type *RobotOdom*, with the current values of (x,y, vel_x, vel_z).
	
	Args:
	   msg (geometry_msgs): The odometry of the robot.
	   
	Returns:
	   No return value.
	
	"""
	robot_state.x = msg.pose.pose.position.x
	robot_state.y = msg.pose.pose.position.y
	robot_state.z = 0

	robot_state.vel_x = msg.twist.twist.linear.x
	robot_state.vel_z = msg.twist.twist.angular.z


def publish_data(event):
	"""This function publishes the values of position and velocity of the robot communicated by the custom message *(RobotOdom)* *event*.
	
	Args:
	   event (RobotOdom): The custom message (x,y, vel_x, vel_z).
	   
	Returns:
	   No return value. 
	
	"""
	robot_state_pub.publish(robot_state)
    
	rospy.loginfo(f"Position: x={robot_state.x}, y={robot_state.y}")
	rospy.loginfo(f"Velocity: Vx={robot_state.vel_x}, Wz={robot_state.vel_z}")

if __name__ == '__main__':
	rospy.init_node('odom_publisher', anonymous=True)
    
	robot_state_pub = rospy.Publisher('/robot_odom', RobotOdom, queue_size=10)
    
	rospy.Subscriber('/odom', Odometry, odom_callback)
    
	rospy.Timer(rospy.Duration(1.0), publish_data)	
	
	rospy.spin()
