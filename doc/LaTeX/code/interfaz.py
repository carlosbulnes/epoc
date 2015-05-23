#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import roslib; roslib.load_manifest('epoc')
from epoc.msg import Frecuencias
from GUI import *
import sys
from time import strftime
from time import sleep

class GUIForm(QtGui.QWidget):
 
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_EpocGUI()
        self.ui.setupUi(self)
        self.grafica = False
        self.frecuencias = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        self.listener()

        QtCore.QObject.connect(self.ui.botonEjecutar, QtCore.SIGNAL('clicked()'), self.habilitaGraficar)
        QtCore.QObject.connect(self.ui.botonDetener, QtCore.SIGNAL('clicked()'), self.detenerROS)
        QtCore.QObject.connect(self.ui.botonPausar, QtCore.SIGNAL('clicked()'), self.pausaGraficar)

    def habilitaGraficar(self):
        self.grafica = True

    def graficar(self, frecuencias):

        self.ui.widget.canvas.ax.plot(frecuencias[0])
        self.ui.widget_2.canvas.ax.plot(frecuencias[1])
        self.ui.widget_3.canvas.ax.plot(frecuencias[2])
        self.ui.widget_4.canvas.ax.plot(frecuencias[3])
        self.ui.widget_5.canvas.ax.plot(frecuencias[4])
        self.ui.widget_6.canvas.ax.plot(frecuencias[5])
        self.ui.widget_7.canvas.ax.plot(frecuencias[6])
        self.ui.widget_8.canvas.ax.plot(frecuencias[7])
        self.ui.widget_9.canvas.ax.plot(frecuencias[8])
        self.ui.widget_10.canvas.ax.plot(frecuencias[9])
        self.ui.widget_11.canvas.ax.plot(frecuencias[10])
        self.ui.widget_12.canvas.ax.plot(frecuencias[11])
        self.ui.widget_13.canvas.ax.plot(frecuencias[12])
        self.ui.widget_14.canvas.ax.plot(frecuencias[13])
        
        self.ui.widget.canvas.draw()
        self.ui.widget_2.canvas.draw()
        self.ui.widget_3.canvas.draw()
        self.ui.widget_4.canvas.draw()
        self.ui.widget_5.canvas.draw()
        self.ui.widget_6.canvas.draw()
        self.ui.widget_7.canvas.draw()
        self.ui.widget_8.canvas.draw()
        self.ui.widget_9.canvas.draw()
        self.ui.widget_10.canvas.draw()
        self.ui.widget_11.canvas.draw()
        self.ui.widget_12.canvas.draw()
        self.ui.widget_13.canvas.draw()
        self.ui.widget_14.canvas.draw()

    def detenerROS(self):
        self.grafica = False
        self.generarLog()

    def pausaGraficar(self):
        self.grafica = False

    def generarLog(self):
        sleep(.1)

        nombre = self.ui.textNombrePrueba.toPlainText()
        if nombre:
            nombre = nombre + '_' + strftime("%d-%m-%y_%H:%M") + '.xls'
            file = open(nombre, 'w')
            file.write('Senal 1, Senal 2, Senal 3, Senal 4, Senal 5, Senal 6, Senal 7,'
                        ' Senal 8, Senal 9, Senal 10, Senal 11, Senal 12, Senal 13, Senal 14\n')
            file.write(self.ui.textBrowser.toPlainText())
            self.ui.textBrowser.setPlainText("")
        else:
            msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Warning,
                "QMessageBox.warning()", "Espeficifica un nombre y presiona Detener nuevamente",
                QtGui.QMessageBox.NoButton, self)
            msgBox.exec_()

    def callback(self, data):

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
                self.ui.widget_8.canvas.ax.clear()
                self.ui.widget_9.canvas.ax.clear()
                self.ui.widget_10.canvas.ax.clear()
                self.ui.widget_11.canvas.ax.clear()
                self.ui.widget_12.canvas.ax.clear()
                self.ui.widget_13.canvas.ax.clear()
                self.ui.widget_14.canvas.ax.clear()

            self.graficar(self.frecuencias)

    def listener(self):
         rospy.init_node('listener', anonymous=True, disable_signals=False)
        rospy.Subscriber("mensaje", Frecuencias, self.callback)


if __name__ == '__main__':
 
    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    myapp.show()
    sys.exit(app.exec_())
    #rospy.signal_shutdown("Se presiono el boton detener")
    #listener()
