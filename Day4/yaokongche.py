import rospy
import pygame
from geometry_msgs.msg import Twist
lis = 0
ans = 0

while True:
	pub = rospy.Publisher('/turtle1/cmd/vel',Twist,queue_size = 10)
	rospy.init_node('/turtle1/cmd/vel',anonymous = True)
	rate = rospy.Rate(10)
	pub_twist = Twist()
	pub_twist.linear.x = lis
	pub_twist.angular = ans
	pub.publish( pub_twist )
	rate.sleep()
	if keys_pressed[pygame.K_W]:
		lis = 1 
