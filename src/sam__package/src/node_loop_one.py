#! /usr/bin/env python
import rospy

rospy.init_node("loop_node_one")

rate = rospy.Rate(2)

while not rospy.is_shutdown():
        print"my node loop 1 is active"
        rate.sleep()
