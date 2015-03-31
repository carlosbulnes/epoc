#!/usr/bin/env python

import rospy
import roslib; roslib.load_manifest('epoc')
from epoc.msg import Frecuencias
from EpocGUI import *
import sys

class GUIForm(QtGui.QWidget):
 
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_EpocGUI()
        self.ui.setupUi(self)
        self.grafica = False

        self.listener()        
        #self.recibe_frecuencias(self)
        #print 'Creando objeto de ROS'
        #self.ros = ROS(self)
        #print 'Objeto ros creado'
        #raw_input()
        #ros.recibe_frecuencias2()
        #self.listener()
        #QtCore.QObject.connect(self.ui.playButton, QtCore.SIGNAL('clicked()'), self.playGraph)
        QtCore.QObject.connect(self.ui.playButton, QtCore.SIGNAL('clicked()'), self.playGraph)
        QtCore.QObject.connect(self.ui.stopButton, QtCore.SIGNAL('clicked()'), self.stop_service)
        QtCore.QObject.connect(self.ui.pauseButton, QtCore.SIGNAL('clicked()'), self.pauseGraph)

    def playGraph(self):
        #""" Activa la comunicacion ROS """
        #self.listener()
        self.grafica = True
        #self.ui.playButton.setEnable(False) # Inhabilita el boton para evitar multiples invocaciones al servidor.
        #self.ui.stopButton.setEnable(True) # Habilita el boton de Stop
        #print "Frecuencias: ", self.frecuencias
        #self.ros.recibe_frecuencias(self)

    def graficar(self, frecuencias):
        #print 'comienza a graficar valores: ', frecuencias
        #print 'Objeto recibido', gui
        #randomNumbers = random.sample(range(0, 10), 10)
        #if self.grafica:
        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.ax.plot(frecuencias)
        self.ui.widget.canvas.draw()
        #print 'termina de graficar'

    def stop_service(self):
        detener = QtGui.QMessageBox.warning(self, 'Precaucion', 
        'Al detener el servicio sera necesario reiniciar el programa',
        QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        
        if detener == QtGui.QMessageBox.Yes:
            rospy.signal_shutdown("Se presiono el boton detener")
        
        #self.ui.playButton.setEnable(True) # Reactiva el boton de Play para poder volver a iniciar el servidor.
        #self.ui.stopButton.setEnable(False) # Inhabilita el boton de Stop

    def pauseGraph(self):
        self.grafica = False

    def callback(self, data):
        if self.grafica:
            #frecuencias = [0]
            frecuencias = list(data.datos)
            frecuencias.insert(0, 0)
            self.graficar(frecuencias)
        #print 'Senales: ', self.frecuencias
        #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
            rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.datos)

    def listener(self):

        # In ROS, nodes are uniquely named. If two nodes with the same
        # node are launched, the previous one is kicked off. The
        # anonymous=True flag means that rospy will choose a unique
        # name for our 'talker' node so that multiple talkers can
        # run simultaneously.
        rospy.init_node('listener', anonymous=True, disable_signals=False)

        rospy.Subscriber("mensaje", Frecuencias, self.callback)
        #print 'comunicacion iniciada'
        #raw_input()

        # spin() simply keeps python from exiting until this node is stopped
        #rospy.spin()

if __name__ == '__main__':
 
    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    myapp.show()
    globalGUI = myapp   
    sys.exit(app.exec_())
    #listener()
