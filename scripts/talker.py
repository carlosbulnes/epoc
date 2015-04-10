#!/usr/bin/env python

import rospy
import numpy as np
import roslib; roslib.load_manifest('epoc')
from epoc.msg import Frecuencias

def talker():
    pub = rospy.Publisher('mensaje', Frecuencias)
    rospy.init_node('talker', anonymous=True, disable_signals=False)
    rate = rospy.Rate(3) # 10hz
    while not rospy.is_shutdown():
        hello_str = "%s" % rospy.get_time()
        rospy.loginfo(hello_str)
        data = []
        
        for i in range(14):
            data.append(np.random.random())

        pub.publish(data)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass