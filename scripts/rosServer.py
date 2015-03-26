#!/usr/bin/env python

import roslib; roslib.load_manifest('epoc')
from epoc.srv import *
import rospy
from mainGUI import *

class ROS(GUIForm):
	def __init__(self, GUIForm):
		#print 'inicializando ros class'
		self.gui = GUIForm
		#print 'Objeto gui creado: ', self.gui
		#print 'fin de __init__'

	def grafica_frecuencias(self, request):
		frecuencias = request.sen
		#frecuencias_lista = []
		self.gui.frecuencias = list(frecuencias)
		#tiempo = []
		#tiempo.extend(range(14))

		#print "Frecuencias: ", frecuencias
		#print 'Objeto gui enviado: ', self.gui
		#self.gui.graficar(self.gui, frecuencias_lista)
		#GUIForm.PlotFunc(frecuencias)
		self.gui.ui.widget.canvas.ax.clear()
		self.gui.ui.widget.canvas.ax.plot(frecuencias)
		self.gui.ui.widget.canvas.draw()
	 
		#plt.scatter(tiempo, frecuencias)
		#plt.draw()
		#time.sleep(0.1)

		return FrecuenciasResponse(0)

	def recibe_frecuencias(self, gui):
		rospy.init_node('recibe_frecuencias_server')
		print 'porcesando recibe_frecuencias'
		#raw_input('Enter para iniciar...')
		s = rospy.Service('transmite_frecuencias', Frecuencias, self.grafica_frecuencias)
		print 'En la espera de frecuencias...'
		#rospy.spin()



    #recibe_frecuencias()
    #print 'recibe_frecuencias ejecutada correctamente'
	
	#plt.ion()
	#plt.show()
	