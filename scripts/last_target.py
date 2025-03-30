#!/usr/bin/env python

"""
.. module: last_target
   :platform unix
   :synopsis: Is another script blablabla.

This is the description of the second script.

.. moduleauthor:: Bertille Beaujean <beaujean.bertille@orange.fr>

"""

import rospy
from assignment_2_2024.srv import LastTarget, LastTargetResponse

def callback(targ):
	"""This function does something.
	Args:
	   msg (RobotOdom): The custom message.
	Kwargs:
	   what (can): this possibly be.
	Returns:
	   nothing.
	
	"""
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
