#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Point, Twist

def odom_callback(msg):
    position_msg = Point()
    position_msg.x = msg.pose.pose.position.x
    position_msg.y = msg.pose.pose.position.y
    position_msg.z = 0

    velocity_msg = Twist()
    velocity_msg.linear.x = msg.twist.twist.linear.x
    velocity_msg.angular.z = msg.twist.twist.angular.z

    position_pub.publish(position_msg)
    velocity_pub.publish(velocity_msg)

    rospy.loginfo(f"Position: x={position_msg.x}, y={position_msg.y}")
    rospy.loginfo(f"Vitesse: Vx={velocity_msg.linear.x}, Wz={velocity_msg.angular.z}")

if __name__ == '__main__':
    rospy.init_node('odom_publisher', anonymous=True)

    position_pub = rospy.Publisher('/robot_position', Point, queue_size=10)
    velocity_pub = rospy.Publisher('/robot_velocity', Twist, queue_size=10)

    rospy.Subscriber('/odom', Odometry, odom_callback)
    
    rospy.spin()
