#!/usr/bin/env python
import roslib; roslib.load_manifest('epoc')
from epoc.srv import *
import rospy

import numpy as np 
import matplotlib.pyplot as plt

def grafica_frecuencias(request):
	frecuencias = request.sen
	tiempo = []
	tiempo.extend(range(14))
	print "Frecuencias: ", frecuencias
	plt.plot(tiempo, frecuencias)
	plt.show()

	return FrecuenciasResponse(0)

def recibe_frecuencias():
	rospy.init_node('recibe_frecuencias_server')
	s = rospy.Service('transmite_frecuencias', Frecuencias, grafica_frecuencias)
	print 'En la espera de frecuencias...'
	rospy.spin()

if __name__ == "__main__":
	recibe_frecuencias()