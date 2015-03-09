#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
import roslib; roslib.load_manifest('epoc')
from epoc.srv import *

def envia_frecuencias(f):
	rospy.wait_for_service('transmite_frecuencias')
	try:
		transmite_frecuencias = rospy.ServiceProxy('transmite_frecuencias', Frecuencias)
		
		result = transmite_frecuencias(f)
		return result.a
	except rospy.ServiceException, e:
		print "Falló llamada al servicio: %s"%e


if __name__ == "__main__":
    
    frecuencias = [12.31, 32.21, 3.123, 2.54, 0.123, 1.331, 0.313,
    			   12.41, 31.41, 1.232, 9.15, 1.004, 3.123, 12.31]
	
    frecuencias2 = [2.31, 2.21, 13.123, 22.54, 1.123, 11.331, 3.313, 
   					2.41, 3.41, 11.232, 3.15, 12.004, 13.123, 1.31]

    for i in range(100):
    #while True:
    	if i % 2 is 0:
    		envia_frecuencias(frecuencias)
    	else:
    		envia_frecuencias(frecuencias2)