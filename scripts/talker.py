#!/usr/bin/env python

# Librerias de ROS
import rospy
import numpy as np
import roslib; roslib.load_manifest('epoc')
from epoc.msg import Frecuencias

# Librerias de Emokit
from emokit.emotiv import Emotiv
import platform
if platform.system() == "Windows":
    import socket  # Needed to prevent gevent crashing on Windows. (surfly / gevent issue #459)
import gevent

def obtenerData(data):
    packet = headset.dequeue()
    #print packet.gyro_x, packet.gyro_y
    data.append(packet.sensors['F3']['value'])
    data.append(packet.sensors['FC5']['value'])
    data.append(packet.sensors['AF3']['value'])
    data.append(packet.sensors['F7']['value'])
    data.append(packet.sensors['T7']['value'])
    data.append(packet.sensors['P7']['value'])
    data.append(packet.sensors['O1']['value'])
    data.append(packet.sensors['O2']['value'])
    data.append(packet.sensors['P8']['value'])
    data.append(packet.sensors['T8']['value'])
    data.append(packet.sensors['F8']['value'])
    data.append(packet.sensors['AF4']['value'])
    data.append(packet.sensors['FC6']['value'])
    data.append(packet.sensors['F4']['value'])
    print data
    gevent.sleep(0)    

def talker(): 
    pub = rospy.Publisher('mensaje', Frecuencias)
    rospy.init_node('talker', anonymous=True, disable_signals=False)
    rate = rospy.Rate(20) # 10hz

    while not rospy.is_shutdown():
        data = []
        hello_str = "%s" % rospy.get_time()
        rospy.loginfo(hello_str)
        
        obtenerData(data)
        #for i in range(14):
        #    data.append(np.random.random())
        
        pub.publish(data)
        rate.sleep()

        
if __name__ == '__main__':
    headset = Emotiv()
    gevent.spawn(headset.setup)
    gevent.sleep(0)    
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
    except KeyboardInterrupt:
        headset.close()
    finally:
        headset.close()    