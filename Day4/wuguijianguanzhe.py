import rospy
from geometry_msgs.msg import Twist

def callback(xue):
	if(xue.linear.x > 0):
		rospy.loginfo("xiaao wugui qianjin")
	if(xue.linear.x < 0):
		rospy.loginfo("xiaao wugui houtui")
	if(xue.angular.z > 0):
		rospy.loginfo("xiaao wugui zuozhuan")
	if(xue.angular.z < 0):
		rospy.loginfo("xiaao wugui youzhuan")
def listener():
	rospy.init_node('wuguijianguanzhe',anonymous = True)
	rospy.Subscriber("/turtle1/cmd_vel",Twist,callback)
	rospy.spin()
if __name__ =='__main__':
	listener()
