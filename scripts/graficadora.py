#!/usr/bin/env python
import roslib; roslib.load_manifest('epoc')
from epoc.srv import *
import rospy

import time
import matplotlib.pyplot as plt

def grafica_frecuencias(request):
	frecuencias = request.sen
	tiempo = []
	tiempo.extend(range(14))
	print "Frecuencias: ", frecuencias
	plt.scatter(tiempo, frecuencias)
	plt.draw()
	time.sleep(0.1)

	return FrecuenciasResponse(0)

def recibe_frecuencias():
	rospy.init_node('recibe_frecuencias_server')
	s = rospy.Service('transmite_frecuencias', Frecuencias, grafica_frecuencias)
	print 'En la espera de frecuencias...'
	rospy.spin()

if __name__ == "__main__":
	plt.ion()
	plt.show()
	recibe_frecuencias()