#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import roslib; roslib.load_manifest('epoc')
from epoc.msg import Frecuencias
from GUI import *
import sys
from time import strftime
from time import sleep
import datetime

class GUIForm(QtGui.QWidget):
 
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        
        # Inicialización de la interfaz
        self.ui = Ui_EpocGUI()
        self.ui.setupUi(self)

        # Bandera para permite/impedir graficación
        self.grafica = False

        # Lista de frecuencias
        self.frecuencias = [[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        
        # Comienza a escuchar los mensajes en ROS
        self.listener()
        self.tiempo_i = datetime.datetime.now()
        self.tiempo_f = datetime.datetime.now()
        self.ocurrencias = 0

        # Definición de los botones
        QtCore.QObject.connect(self.ui.botonEjecutar, QtCore.SIGNAL('clicked()'), self.habilitaGraficar)
        QtCore.QObject.connect(self.ui.botonDetener, QtCore.SIGNAL('clicked()'), self.detenerGraficar)
        QtCore.QObject.connect(self.ui.botonPausar, QtCore.SIGNAL('clicked()'), self.pausaGraficar)

    def habilitaGraficar(self):
        """ Habilita la graficación por medio de la bandera """

        self.grafica = True
        self.tiempo_i = datetime.datetime.now()
        self.ocurrencias = 0

    def graficar(self, frecuencias):
        """ Funcion que manda los datos a graficar """

        # Añade los puntos a la gráfica
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
        
        # Realiza el dibujado en la gráfica
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

    def detenerGraficar(self):
        """ Detiene la graficación y genera el log """

        self.grafica = False
        self.tiempo_f = datetime.datetime.now()
        print 'tiempo_i: %s' % self.tiempo_i
        print 'tiempo_f: %s' % self.tiempo_f
        print 'diferencia: %s' % (self.tiempo_f - self.tiempo_i)
        print 'Ocurrencias: ' + str(self.ocurrencias)
        self.generarLog()

    def pausaGraficar(self):
        """ Pausa la graficación """
        self.grafica = False

    def generarLog(self):
        sleep(.1)

        # Extracción del nombre del cuadro de texto
        nombre = self.ui.textNombrePrueba.toPlainText()
        
        # Valida que se haya ingresado un nombre de prueba
        if nombre:
            nombre = nombre + '_' + strftime("%d-%m-%y_%H:%M") + '.csv'
            file = open(nombre, 'w')
            file.write('F3, FC5, AF3, F7, T7, P7, O1, O2, P8, T8, F8, AF4, FC6, F4\n')
            file.write(self.ui.textBrowser.toPlainText())
            self.ui.textBrowser.setPlainText("")
        else:
            msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Warning,
                "QMessageBox.warning()", "Espeficifica un nombre y presiona Detener nuevamente",
                QtGui.QMessageBox.NoButton, self)
            msgBox.exec_()

    def callback(self, data):
        """ Recibe el mensaje transmitido """

        if self.grafica:
            data = list(data.datos)
            self.ocurrencias += 1
            '''
            # La lista frecuencias va encolando las señales en cada iteración
            # data contiene las 14 señales de la iteración actual
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
            
            # Arma el texto para mostrarlo en el cuadro de log
            log = str(str(data[0]) + ', ' + str(data[1]) + ', ' + str(data[2]) + 
                      ', ' + str(data[3]) + ', ' + str(data[4]) + ', ' + str(data[5]) + 
                      ', ' + str(data[6]) + ', ' + str(data[7]) + ', ' + str(data[8]) + 
                      ', ' + str(data[9]) + ', ' + str(data[10]) + ', ' + str(data[11]) + 
                      ', ' + str(data[12]) + ', ' + str(data[13]))
            
            self.ui.textBrowser.appendPlainText(log)
            self.ui.textBrowser.appendPlainText("")

            # Resetea la lista de frecuencias y limpia las gráficas cuando la lista llega a los 30 elementos
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
            '''

    def listener(self):
        """ Inicia la comunicacion ROS """

        rospy.init_node('listener', anonymous=True, disable_signals=False)

        # Se suscribe a un mensaje de ROS, el primer parametro identifica al mensaje,
        # el segundo es el nombre del mensaje definido en la carpeta msg del proyecto,
        # el tercer parametro es la llamada al metodo callback que se encargara de estar leyendo siempre los mensajes
        rospy.Subscriber("mensaje", Frecuencias, self.callback) 


if __name__ == '__main__':
 
    app = QtGui.QApplication(sys.argv)
    myapp = GUIForm()
    myapp.show()
    sys.exit(app.exec_())
