#!/usr/bin/env python

import rospy
import actionlib
from nav_msgs.msg import Odometry
from assignment_2_2024.msg import RobotOdom

robot_state = RobotOdom()

def odom_callback(msg):

	robot_state.x = msg.pose.pose.position.x
	robot_state.y = msg.pose.pose.position.y
	robot_state.z = 0

	robot_state.vel_x = msg.twist.twist.linear.x
	robot_state.vel_z = msg.twist.twist.angular.z


def publish_data(event):
	robot_state_pub.publish(robot_state)
    
	rospy.loginfo(f"Position: x={robot_state.x}, y={robot_state.y}")
	rospy.loginfo(f"Velocity: Vx={robot_state.vel_x}, Wz={robot_state.vel_z}")

if __name__ == '__main__':
	rospy.init_node('odom_publisher', anonymous=True)
    
	robot_state_pub = rospy.Publisher('/robot_odom', RobotOdom, queue_size=10)
    
	rospy.Subscriber('/odom', Odometry, odom_callback)
    
	rospy.Timer(rospy.Duration(1.0), publish_data)	
	
	rospy.spin()
