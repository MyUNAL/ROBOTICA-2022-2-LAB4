import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import termios, sys, os
from numpy import pi

TERMIOS = termios

class PhantomX:

    def joint_publisher(self):
        pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
        rospy.init_node('joint_publisher', anonymous=False)
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1","joint_2","joint_3","joint_4","joint_5"]
        point = JointTrajectoryPoint()
        while True:
            key = input('Seleccione Posición: ')
            i=0
            if key == 'h':
                point.positions = [0, 0, 0, 0, 0]    
                point.time_from_start = rospy.Duration(0.5)
                state.points.append(point)
                pub.publish(state)
                rospy.sleep(1)
                    
            elif key == 'o':
                point.positions = [pi/2, -pi/4, pi/2, pi/2, -pi/2]    
                point.time_from_start = rospy.Duration(0.5)
                state.points.append(point)
                pub.publish(state)
                rospy.sleep(1)

            elif key == '2':
                point.positions = [-20*pi/180, 20*pi/180, -20*pi/180, 20*pi/180, 0]    
                point.time_from_start = rospy.Duration(0.5)
                state.points.append(point)
                pub.publish(state)
                rospy.sleep(1)
            elif key == '3':
                point.positions = [30*pi/180, -30*pi/180, 30*pi/180, -30*pi/180, 0]    
                point.time_from_start = rospy.Duration(0.5)
                state.points.append(point)
                pub.publish(state)
                rospy.sleep(1)
            elif key == '4':
                point.positions = [-pi/2,15*pi/180,-55*pi/180,17*pi/180,0]    
                point.time_from_start = rospy.Duration(0.5)
                state.points.append(point)
                pub.publish(state)
                rospy.sleep(1)
            elif key == '5':
                point.positions = [-pi/2,pi/4,-55*pi/180,pi/4,10*pi/180]    
                point.time_from_start = rospy.Duration(0.5)
                state.points.append(point)
                pub.publish(state)
                rospy.sleep(1)
            

            elif key == 'x':
                break

if __name__ == '__main__':
    try:
        ph = PhantomX()
        ph.joint_publisher()
    except rospy.ROSInterruptException:
        pass
