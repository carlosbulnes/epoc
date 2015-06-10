# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QHBoxLayout, QVBoxLayout, QGridLayout
from matplotlibwidgetFile import matplotlibWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EpocGUI(object):
    def setupUi(self, EpocGUI):

        # Definición de las layouts
        EpocGUI.main_layout = QHBoxLayout()
        self.layout_izq = QVBoxLayout()
        self.layout_der = QVBoxLayout()
        self.grid = QtGui.QGridLayout()
        self.grid_botones = QtGui.QGridLayout()

        EpocGUI.setObjectName(_fromUtf8("EpocGUI"))
        EpocGUI.resize(1101, 897) # Tamaño por defecto

        # Definición de las gráficas
        self.centralwidget = QtGui.QWidget(EpocGUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        self.widget = matplotlibWidget(self.centralwidget)
        self.widget.setObjectName(_fromUtf8("widget"))

        self.widget_2 = matplotlibWidget(self.centralwidget)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        
        self.widget_3 = matplotlibWidget(self.centralwidget)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        
        self.widget_4 = matplotlibWidget(self.centralwidget)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        
        self.widget_5 = matplotlibWidget(self.centralwidget)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.widget_6 = matplotlibWidget(self.centralwidget)
        self.widget_6.setObjectName(_fromUtf8("widget_6"))

        self.widget_7 = matplotlibWidget(self.centralwidget)
        self.widget_7.setObjectName(_fromUtf8("widget_7"))

        self.widget_8 = matplotlibWidget(self.centralwidget)
        self.widget_8.setObjectName(_fromUtf8("widget_8"))

        self.widget_9 = matplotlibWidget(self.centralwidget)
        self.widget_9.setObjectName(_fromUtf8("widget_9"))

        self.widget_10 = matplotlibWidget(self.centralwidget)
        self.widget_10.setObjectName(_fromUtf8("widget_10"))

        self.widget_11 = matplotlibWidget(self.centralwidget)
        self.widget_11.setObjectName(_fromUtf8("widget_11"))

        self.widget_12 = matplotlibWidget(self.centralwidget)
        self.widget_12.setObjectName(_fromUtf8("widget_12"))

        self.widget_13 = matplotlibWidget(self.centralwidget)
        self.widget_13.setObjectName(_fromUtf8("widget_13"))

        self.widget_14 = matplotlibWidget(self.centralwidget)
        self.widget_14.setObjectName(_fromUtf8("widget_14"))

        # Definición de los botones
        self.botonPausar = QtGui.QPushButton(self.centralwidget)
        self.botonPausar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonPausar.setIcon(icon)
        self.botonPausar.setObjectName(_fromUtf8("botonPausar"))
        
        self.botonDetener = QtGui.QPushButton(self.centralwidget)
        self.botonDetener.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("img/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonDetener.setIcon(icon1)
        self.botonDetener.setObjectName(_fromUtf8("botonDetener"))
        
        self.botonEjecutar = QtGui.QPushButton(self.centralwidget)
        self.botonEjecutar.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.botonEjecutar.setIcon(icon2)
        self.botonEjecutar.setObjectName(_fromUtf8("botonEjecutar"))

        # Definición del cuadro de log
        self.textBrowser = QtGui.QPlainTextEdit(self.centralwidget)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setReadOnly(True)
        self.textBrowser.setSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)

        # Definición de cuadro y etiqueta de nombre
        self.textNombrePrueba = QtGui.QTextEdit(self.centralwidget)
        self.textNombrePrueba.setObjectName(_fromUtf8("textEdit_2"))
        self.textNombrePrueba.setMaximumHeight(25)

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        
        self.menubar = QtGui.QMenuBar(EpocGUI)
        #self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        
        # Agrega las gráficas a un gridLayout
        #EpocGUI.main_layout.addWidget(self.centralwidget)
        self.grid.addWidget(self.widget,0,0)
        self.grid.addWidget(self.widget_2,0,1)
        self.grid.addWidget(self.widget_3,0,2)
        self.grid.addWidget(self.widget_4,1,0)
        self.grid.addWidget(self.widget_5,1,1)
        self.grid.addWidget(self.widget_6,1,2)
        self.grid.addWidget(self.widget_7,2,0)
        self.grid.addWidget(self.widget_8,2,1)
        self.grid.addWidget(self.widget_9,2,2)
        self.grid.addWidget(self.widget_10,3,0)
        self.grid.addWidget(self.widget_11,3,1)
        self.grid.addWidget(self.widget_12,3,2)
        self.grid.addWidget(self.widget_13,4,0)
        self.grid.addWidget(self.widget_14,4,1)
        
        # Agrega las gráficas a la parte izquierda de la pantalla
        self.layout_izq.addLayout(self.grid)

        # Agrega elementos de la parte derecha de la pantalla
        self.layout_der.addWidget(self.label)
        self.layout_der.addWidget(self.textNombrePrueba)

        self.grid_botones.addWidget(self.botonPausar,0,0)
        self.grid_botones.addWidget(self.botonEjecutar,0,1)
        self.grid_botones.addWidget(self.botonDetener,0,2)
        self.layout_der.addLayout(self.grid_botones)

        self.layout_der.addWidget(self.textBrowser)

        # Agrega los layouts izquierdo y derecho al principal
        EpocGUI.main_layout.addLayout(self.layout_izq)
        EpocGUI.main_layout.addLayout(self.layout_der)        
        EpocGUI.setLayout(EpocGUI.main_layout)
        
        self.retranslateUi(EpocGUI)
        QtCore.QMetaObject.connectSlotsByName(EpocGUI)

    def retranslateUi(self, EpocGUI):
        EpocGUI.setWindowTitle(QtGui.QApplication.translate("EpocGUI", "Epoc", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EpocGUI", "Nombre del experimento", None, QtGui.QApplication.UnicodeUTF8))