# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'epoc2.ui'
#
# Created: Sat Apr 11 18:36:04 2015
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from matplotlibwidgetFile import matplotlibWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EpocGUI(object):
    def setupUi(self, EpocGUI):
        EpocGUI.setObjectName(_fromUtf8("EpocGUI"))
        EpocGUI.resize(975, 765)

        self.centralwidget = QtGui.QWidget(EpocGUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = matplotlibWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 291, 171))
        self.widget.setObjectName(_fromUtf8("widget"))

        self.pauseButton = QtGui.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(650, 160, 85, 27))
        self.pauseButton.setText(_fromUtf8("Pausar"))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(850, 160, 85, 27))
        self.stopButton.setText(_fromUtf8("Detener"))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("img/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        
        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(750, 160, 85, 27))
        self.playButton.setText(_fromUtf8("Ejecutar"))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon2)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        
        self.textBrowser = QtGui.QPlainTextEdit(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(630, 270, 331, 340))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setReadOnly(True)

        self.widget_2 = matplotlibWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(320, 20, 291, 171))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.widget_4 = matplotlibWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(320, 200, 291, 171))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.widget_3 = matplotlibWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(20, 200, 291, 171))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.widget_7 = matplotlibWidget(self.centralwidget)
        self.widget_7.setGeometry(QtCore.QRect(20, 560, 291, 171))
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.widget_6 = matplotlibWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(320, 380, 291, 171))
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.widget_5 = matplotlibWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(20, 380, 291, 171))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        
        self.textNombrePrueba = QtGui.QPlainTextEdit(self.centralwidget)
        self.textNombrePrueba.setGeometry(QtCore.QRect(650, 100, 281, 21))
        self.textNombrePrueba.setObjectName(_fromUtf8("textNombrePrueba"))
        
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(650, 80, 141, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.menubar = QtGui.QMenuBar(EpocGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.retranslateUi(EpocGUI)
        QtCore.QMetaObject.connectSlotsByName(EpocGUI)

    def retranslateUi(self, EpocGUI):
        EpocGUI.setWindowTitle(QtGui.QApplication.translate("EpocGUI", "Epoc", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EpocGUI", "Nombre del experimento", None, QtGui.QApplication.UnicodeUTF8))
