#!/usr/bin/env python
import roslib; roslib.load_manifest('epoc')
from epoc.srv import *
import rospy

import matplotlib.pyplot as plt
import sys
from PyQt4 import QtGui, QtCore
import sys
from EpocGUI import *
#import initGUI as gui

class GUIForm(QtGui.QWidget):
 
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_EpocGUI()
        self.ui.setupUi(self)
        #self.recibe_frecuencias(self)
        print 'Creando objeto de ROS'
        self.ros = ROS(self)
        print 'Objeto ros creado'
        #raw_input()
        #ros.recibe_frecuencias2()
        QtCore.QObject.connect(self.ui.playButton, QtCore.SIGNAL('clicked()'), self.playGraph)

    def playGraph(self):
    	self.ros.recibe_frecuencias(self)

    def graficar(self, gui, frecuencias):
        #print 'comienza a graficar valores: ', frecuencias
        print 'Objeto recibido', gui
        #randomNumbers = random.sample(range(0, 10), 10)
        gui.ui.widget.canvas.ax.clear()
        gui.ui.widget.canvas.ax.plot(frecuencias)
        gui.ui.widget.canvas.draw()
        print 'termina de graficar'
	

class ROS(GUIForm):
	def __init__(self, GUIForm):
		#print 'inicializando ros class'
		self.gui = GUIForm
		print 'Objeto gui creado: ', self.gui
		#print 'fin de __init__'

	def grafica_frecuencias(self, request):
		frecuencias = request.sen
		#frecuencias_lista = []
		frecuencias_lista = list(frecuencias)
		#tiempo = []
		#tiempo.extend(range(14))

		print "Frecuencias: ", frecuencias
		print 'Objeto gui enviado: ', self.gui
		self.gui.graficar(self.gui, frecuencias_lista)
		#GUIForm.PlotFunc(frecuencias)
		#gui.ui.widget.canvas.ax.clear()
		#gui.ui.widget.canvas.ax.plot(frecuencias)
		#gui.ui.widget.canvas.draw()
	 
		#plt.scatter(tiempo, frecuencias)
		#plt.draw()
		#time.sleep(0.1)

		return FrecuenciasResponse(0)

	def recibe_frecuencias(self, gui):
		rospy.init_node('recibe_frecuencias_server')
		#print 'porcesando recibe_frecuencias'
		#raw_input()
		s = rospy.Service('transmite_frecuencias', Frecuencias, self.grafica_frecuencias)
		print 'En la espera de frecuencias...'
		rospy.spin()

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    myapp.show()
    globalGUI = myapp
    sys.exit(app.exec_())

    #recibe_frecuencias()
    #print 'recibe_frecuencias ejecutada correctamente'
	
	#plt.ion()
	#plt.show()
	