#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import rospy
import roslib; roslib.load_manifest('epoc')
from epoc.srv import *

import numpy as np

def envia_frecuencias(f):
	rospy.wait_for_service('transmite_frecuencias')
	try:
		transmite_frecuencias = rospy.ServiceProxy('transmite_frecuencias', Frecuencias)
		print 'Enviando...'
		result = transmite_frecuencias(f)
		return result.a
	except rospy.ServiceException, e:
		print "Falló llamada al servicio: %s"%e


if __name__ == "__main__":
    
    #frecuencias = [12.31, 32.21, 3.123, 2.54, 0.123, 1.331, 0.313,
    #			   12.41, 31.41, 1.232, 9.15, 1.004, 3.123, 12.31]
	
    for i in range(1000):
    	frecuencias = []
    	for j in range(14):
    		frecuencias.append(np.random.random())
    	envia_frecuencias(frecuencias)
