#!/usr/bin/env python

import matplotlib.pyplot as plt
import sys
from multiprocessing import *

from EpocGUI import *
from rosServer import *

pool = Pool(processes=2)

class GUIForm(QtGui.QWidget):
 
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_EpocGUI()
        self.ui.setupUi(self)
        #self.recibe_frecuencias(self)
        #print 'Creando objeto de ROS'
        self.ros = ROS(self)
        self.frecuencias = []
        #print 'Objeto ros creado'
        #raw_input()
        #ros.recibe_frecuencias2()
        QtCore.QObject.connect(self.ui.playButton, QtCore.SIGNAL('clicked()'), self.playGraph)

    def playGraph(self):
        print "Frecuencias: ", self.frecuencias
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

def runGUI(app):
    sys.exit(app.exec_())

if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    #myapp.show()
    globalGUI = myapp
    
    pool.apply_async(myapp.ros.recibe_frecuencias, (myapp))
    pool.apply_async(runGUI, (app))
    #pool.close()
    #pool.join()

    #threads = list()
    #t = threading.Thread(target=myapp.ros.recibe_frecuencias(myapp))
    #server = threading.Thread(target=myapp.ros.recibe_frecuencias(myapp))
    #server = Process(target=myapp.ros.recibe_frecuencias(myapp))
    #threads.append(t)
    #gui = threading.Thread(target=sys.exit(app.exec_()))
    #gui = Process(target=sys.exit(app.exec_()))
    #threads.append(t)
    #print threads
    #raw_input()

    #server.start()
    #gui.start()
    #pool.join()

    #myapp.ros.recibe_frecuencias(myapp)      
    #sys.exit(app.exec_())
