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
        self.frecuencias = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        self.listener()

        QtCore.QObject.connect(self.ui.playButton, QtCore.SIGNAL('clicked()'), self.habilitaGraficar)
        QtCore.QObject.connect(self.ui.stopButton, QtCore.SIGNAL('clicked()'), self.detenerROS)
        QtCore.QObject.connect(self.ui.pauseButton, QtCore.SIGNAL('clicked()'), self.pausaGraficar)

    def habilitaGraficar(self):
        """ Habilita la graficación por medio de la bandera """

        self.grafica = True

    def graficar(self, frecuencias):
        """ Funcion que manda los datos a graficar """

        #self.ui.widget.canvas.ax.clear()
        self.ui.widget.canvas.ax.plot(frecuencias[0])
        self.ui.widget.canvas.ax.plot(frecuencias[1])
        self.ui.widget_2.canvas.ax.plot(frecuencias[2])
        self.ui.widget_2.canvas.ax.plot(frecuencias[3])
        self.ui.widget_3.canvas.ax.plot(frecuencias[4])
        self.ui.widget_3.canvas.ax.plot(frecuencias[5])
        self.ui.widget_4.canvas.ax.plot(frecuencias[6])
        self.ui.widget_4.canvas.ax.plot(frecuencias[7])
        self.ui.widget_5.canvas.ax.plot(frecuencias[8])
        self.ui.widget_5.canvas.ax.plot(frecuencias[9])
        self.ui.widget_6.canvas.ax.plot(frecuencias[10])
        self.ui.widget_6.canvas.ax.plot(frecuencias[11])
        self.ui.widget_7.canvas.ax.plot(frecuencias[12])
        self.ui.widget_7.canvas.ax.plot(frecuencias[13])
        
        self.ui.widget.canvas.draw()
        self.ui.widget_2.canvas.draw()
        self.ui.widget_3.canvas.draw()
        self.ui.widget_4.canvas.draw()
        self.ui.widget_5.canvas.draw()
        self.ui.widget_6.canvas.draw()
        self.ui.widget_7.canvas.draw()

    def detenerROS(self):
        """ Detiene la comunicacion ROS, no se puede revertir """

        #detener = QtGui.QMessageBox.question(self, 'Detener', 
        #"¿Detener y grabar datos de experimento?",
        #QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        
        #if detener == QtGui.QMessageBox.Yes:
            #rospy.signal_shutdown("Se presiono el boton detener")
        self.grafica = False
            #sleep(.1)
        self.generarLog()

    def pausaGraficar(self):
        self.grafica = False

    def generarLog(self):
        sleep(.1)
        text, ok = QtGui.QInputDialog.getText(self, 'Input Dialog', 'Nombre del archivo:')

        file = open(text + '.xls', 'w')
        file.write('Señal 1, Señal 2, Señal 3, Señal 4, Señal 5, Señal 6, Señal 7,'
                    ' Señal 8, Señal 9, Señal 10, Señal 11, Señal 12, Señal 13, Señal 14\n')
        file.write(self.ui.textBrowser.toPlainText())
        self.ui.textBrowser.setPlainText("")

    def callback(self, data):
        """ Recibe el mensaje transmitido """

        if self.grafica:
            data = list(data.datos)
            
            self.frecuencias[0].append(data[0])
            self.frecuencias[1].append(data[1])
            self.frecuencias[2].append(data[2])
            self.frecuencias[3].append(data[3])
            self.frecuencias[4].append(data[4])
            self.frecuencias[5].append(data[5])
            self.frecuencias[6].append(data[6])
            self.frecuencias[7].append(data[7])
            self.frecuencias[8].append(data[8])
            self.frecuencias[9].append(data[9])
            self.frecuencias[10].append(data[10])
            self.frecuencias[11].append(data[11])
            self.frecuencias[12].append(data[12])
            self.frecuencias[13].append(data[13])
            
            log = str(str(data[0]) + ', ' + str(data[1]) + ', ' + str(data[2]) + 
                      ', ' + str(data[3]) + ', ' + str(data[4]) + ', ' + str(data[5]) + 
                      ', ' + str(data[6]) + ', ' + str(data[7]) + ', ' + str(data[8]) + 
                      ', ' + str(data[9]) + ', ' + str(data[10]) + ', ' + str(data[11]) + 
                      ', ' + str(data[12]) + ', ' + str(data[13]))
            
            self.ui.textBrowser.appendPlainText(log)
            self.ui.textBrowser.appendPlainText("")

            if len(self.frecuencias[0]) == 30:
                self.frecuencias = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
                self.ui.widget.canvas.ax.clear()
                self.ui.widget_2.canvas.ax.clear()
                self.ui.widget_3.canvas.ax.clear()
                self.ui.widget_4.canvas.ax.clear()
                self.ui.widget_5.canvas.ax.clear()
                self.ui.widget_6.canvas.ax.clear()
                self.ui.widget_7.canvas.ax.clear()

            self.graficar(self.frecuencias)
            #rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.datos)

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
