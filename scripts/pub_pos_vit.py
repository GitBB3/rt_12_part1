#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
#from geometry_msgs.msg import Point, Twist
from assignment_2_2024.msg import RobotOdom

#position_msg = Point()
#velocity_msg = Twist()
robot_state = RobotOdom()

def odom_callback(msg):
    #global position_msg, velocity_msg
    global robot_state
    
    #position_msg.x = msg.pose.pose.position.x
    #position_msg.y = msg.pose.pose.position.y
    #position_msg.z = 0
    
    robot_state.x = msg.pose.pose.position.x
    robot_state.y = msg.pose.pose.position.y
    robot_state.z = 0

    #velocity_msg.linear.x = msg.twist.twist.linear.x
    #velocity_msg.angular.z = msg.twist.twist.angular.z
    
    robot_state.vel_x = msg.twist.twist.linear.x
    robot_state.vel_z = msg.twist.twist.angular.z


def publish_data(event):
    #position_pub.publish(position_msg)
    #velocity_pub.publish(velocity_msg)
    robot_state_pub.publish(robot_state)
    
    rospy.loginfo(f"Position: x={robot_state.x}, y={robot_state.y}")
    rospy.loginfo(f"Velocity: Vx={robot_state.vel_x}, Wz={robot_state.vel_z}")

if __name__ == '__main__':
    rospy.init_node('odom_publisher', anonymous=True)

    #position_pub = rospy.Publisher('/robot_position', Point, queue_size=10)
    #velocity_pub = rospy.Publisher('/robot_velocity', Twist, queue_size=10)
    robot_state_pub = rospy.Publisher('/robot_odom', RobotOdom, queue_size=10)
    
    rospy.Subscriber('/odom', Odometry, odom_callback)
    
    rospy.Timer(rospy.Duration(1.0), publish_data)
    
    rospy.spin()
