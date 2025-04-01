#!/usr/bin/env python

"""
.. module: last_target
   :platform unix
   :synopsis: Service node that, when called, returns the coordinates of the last target sent by the user.

.. moduleauthor:: Bertille Beaujean <beaujean.bertille@orange.fr>

Service node that, when called, returns the coordinates of the last target sent by the user.

**Service:**
/last_target

"""

import rospy
from assignment_2_2024.srv import LastTarget, LastTargetResponse

def callback(targ):
	"""This function reads the position of the last target sent to the robot, on the topics */des_pos_x* and */des_pos_y*. It informs the user of their value with 'loginfo'.
	
	Args:
	   targ (srv): The service.
	   
	Returns:
	   coordinates x and y of the last target LastTargetResponse()
	
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
