#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys

from EpocGUI import *
from rosServer import *

class GUIForm(QtGui.QWidget):
 
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_EpocGUI()
        self.ui.setupUi(self)
        #self.recibe_frecuencias(self)
        #print 'Creando objeto de ROS'
        self.ros = ROS(self)
        #print 'Objeto ros creado'
        #raw_input()
        #ros.recibe_frecuencias2()
        QtCore.QObject.connect(self.ui.playButton, QtCore.SIGNAL('clicked()'), self.playGraph)

    def playGraph(self):
    	#self.ros.recibe_frecuencias(self)
        pass

    def graficar(self, gui, frecuencias):
        #print 'comienza a graficar valores: ', frecuencias
        print 'Objeto recibido', gui
        #randomNumbers = random.sample(range(0, 10), 10)
        gui.ui.widget.canvas.ax.clear()
        gui.ui.widget.canvas.ax.plot(frecuencias)
        gui.ui.widget.canvas.draw()
        print 'termina de graficar'

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    myapp.show()
    globalGUI = myapp
    myapp.ros.recibe_frecuencias(myapp)      
    sys.exit(app.exec_())
