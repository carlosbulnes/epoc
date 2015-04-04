#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import roslib; roslib.load_manifest('epoc')
from epoc.msg import Frecuencias
from GUI import *
import sys
from time import sleep

class GUIForm(QtGui.QWidget):
 
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_EpocGUI()
        self.ui.setupUi(self)
        self.grafica = False
        self.listener()

        QtCore.QObject.connect(self.ui.playButton, QtCore.SIGNAL('clicked()'), self.habilitaGraficar)
        QtCore.QObject.connect(self.ui.stopButton, QtCore.SIGNAL('clicked()'), self.detenerROS)
        QtCore.QObject.connect(self.ui.pauseButton, QtCore.SIGNAL('clicked()'), self.pausaGraficar)

    def habilitaGraficar(self):
        """ Habilita la graficación por medio de la bandera """

        self.grafica = True

    def graficar(self, frecuencias):
        """ Funcion que manda los datos a graficar """

        self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.ax.plot(frecuencias)
        self.ui.widget.canvas.draw()

    def detenerROS(self):
        """ Detiene la comunicacion ROS, no se puede revertir """

        detener = QtGui.QMessageBox.question(self, 'Detener', 
        "¿Detener y grabar datos de experimento?",
        QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        
        if detener == QtGui.QMessageBox.Yes:
            #rospy.signal_shutdown("Se presiono el boton detener")
            self.grafica = False
            #sleep(.1)
            #self.ui.textBrowser.setPlainText("")
            self.generarLog()

    def pausaGraficar(self):
        self.grafica = False

    def generarLog(self):
        sleep(.1)
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Nombre del archivo:')

        file = open(text + '.xls', 'w')
        file.write(self.ui.textBrowser.toPlainText())
        self.ui.textBrowser.setPlainText("")

    def callback(self, data):
        """ Recibe el mensaje transmitido """

        if self.grafica:
            frecuencias = list(data.datos)
            frecuencias.insert(0, 0)
            self.graficar(frecuencias)
            rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.datos)
            self.ui.textBrowser.appendPlainText(str(frecuencias))
            self.ui.textBrowser.appendPlainText("")

    def listener(self):
        """ Inicia la comunicacion ROS """

        rospy.init_node('listener', anonymous=True, disable_signals=False)
        rospy.Subscriber("mensaje", Frecuencias, self.callback)


if __name__ == '__main__':
 
    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    myapp.show()
    globalGUI = myapp   
    sys.exit(app.exec_())
    rospy.signal_shutdown("Se presiono el boton detener")
    #listener()
