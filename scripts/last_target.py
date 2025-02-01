#!/usr/bin/env python

import rospy
from assignment_2_2024.srv import LastTarget, LastTargetResponse

def callback(targ):
	rospy.loginfo("Last target: ")
	response = LastTargetResponse()
	response.x = rospy.get_param("/des_pos_x")
	response.y = rospy.get_param("/des_pos_y")
	rospy.loginfo(f"x_last = {response.x}, y_last = {response.y}")
	return response


def main():
	rospy.init_node("last_target")
	
	rospy.Service("last_target", LastTarget, callback)
	
	rospy.spin() 

if __name__ == "__main__":
	main()
