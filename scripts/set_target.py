#!/usr/bin/env python

import rospy
import actionlib
from nav_msgs.msg import Odometry
from assignment_2_2024.msg import RobotOdom, PlanningAction, PlanningGoal
from actionlib_msgs.msg import GoalStatus

def set_target_client():
	global first_start
	client = actionlib.SimpleActionClient('/reaching_goal', PlanningAction)
	client.wait_for_server()
	
	while not rospy.is_shutdown():
		rospy.loginfo("Press T to set a new target. Press C to cancel the previous target.")
		act = input()
		
		goal = PlanningGoal()
		goal.target_pose.pose.position.x = rospy.get_param('/des_pos_x', 0.0)
		goal.target_pose.pose.position.y = rospy.get_param('/des_pos_y', 1.0)
		
		if act == "t" or act == "T":
			rospy.loginfo("Set the target coordinates (x,y)")
			x_tar = float(input("Type the desired x coordinate : "))
			y_tar = float(input("Type the desired y coordinate : "))
			
			rospy.set_param('/des_pos_x', x_tar)
			rospy.set_param('/des_pos_y', y_tar)
			
			goal.target_pose.pose.position.x = x_tar
			goal.target_pose.pose.position.y = y_tar
			client.send_goal(goal)
			
			rospy.loginfo(f"New target has been set : x={goal.target_pose.pose.position.x}, y={goal.target_pose.pose.position.y}")
		    	

		elif act == "c" or act == "C":
			if client.get_state() == GoalStatus.ACTIVE:
				rospy.loginfo(f"Cancelling target (x={goal.target_pose.pose.position.x}, y={goal.target_pose.pose.position.y})...")
				client.cancel_goal()
				rospy.loginfo("Target cancelled.")
			else:
				rospy.loginfo("The robot is not currently aiming at a target.")

		if client.get_state() == GoalStatus.SUCCEEDED:
			rospy.loginfo(f"Target (x={goal.target_pose.pose.position.x}, y={goal.target_pose.pose.position.y}) reached.")	
		
		


if __name__ == '__main__':
	rospy.init_node('action_client', anonymous=True)
	
	set_target_client()
	
	rospy.spin()
