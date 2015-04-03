# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'epoc.ui'
#
# Created: Mon Mar 16 12:44:17 2015
#      by: PyQt4 UI code generator 4.9.1

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EpocGUI(object):
    def setupUi(self, EpocGUI):
        EpocGUI.setObjectName(_fromUtf8("EpocGUI"))
        #EpocGUI.resize(975, 700)
        EpocGUI.setGeometry(200, 100, 975, 700)
        #EpocGUI.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.centralwidget = QtGui.QWidget(EpocGUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = matplotlibWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 60, 611, 561))
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
        
        #self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser = QtGui.QPlainTextEdit(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(630, 270, 331, 340))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setReadOnly(True)
        #EpocGUI.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(EpocGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 975, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        #EpocGUI.setMenuBar(self.menubar)

        self.retranslateUi(EpocGUI)
        QtCore.QMetaObject.connectSlotsByName(EpocGUI)

    def retranslateUi(self, EpocGUI):
        EpocGUI.setWindowTitle(QtGui.QApplication.translate("EpocGUI", "Epoc", None, QtGui.QApplication.UnicodeUTF8))
        #EpocGUI.setWindowTitle('Epoc')

from matplotlibwidgetFile import matplotlibWidget
#import imagenes_rc