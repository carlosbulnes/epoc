# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'epoc3.ui'
#
# Created: Tue Apr 14 21:19:24 2015
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
        EpocGUI.resize(1101, 897)
        hbox = QtGui.QHBoxLayout()
        
        self.centralwidget = QtGui.QWidget(EpocGUI)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.widget = matplotlibWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 10, 260, 180))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.widget_2 = matplotlibWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(250, 10, 260, 180))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.widget_3 = matplotlibWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(500, 10, 260, 180))
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.widget_4 = matplotlibWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(0, 180, 260, 180))
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.widget_5 = matplotlibWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(250, 180, 260, 180))
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.widget_6 = matplotlibWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(500, 180, 260, 180))
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.widget_7 = matplotlibWidget(self.centralwidget)
        self.widget_7.setGeometry(QtCore.QRect(0, 350, 260, 180))
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.widget_8 = matplotlibWidget(self.centralwidget)
        self.widget_8.setGeometry(QtCore.QRect(250, 350, 260, 180))
        self.widget_8.setObjectName(_fromUtf8("widget_8"))
        self.widget_9 = matplotlibWidget(self.centralwidget)
        self.widget_9.setGeometry(QtCore.QRect(500, 350, 260, 180))
        self.widget_9.setObjectName(_fromUtf8("widget_9"))
        self.widget_10 = matplotlibWidget(self.centralwidget)
        self.widget_10.setGeometry(QtCore.QRect(0, 520, 260, 180))
        self.widget_10.setObjectName(_fromUtf8("widget_10"))
        self.widget_11 = matplotlibWidget(self.centralwidget)
        self.widget_11.setGeometry(QtCore.QRect(250, 520, 260, 180))
        self.widget_11.setObjectName(_fromUtf8("widget_11"))
        self.widget_12 = matplotlibWidget(self.centralwidget)
        self.widget_12.setGeometry(QtCore.QRect(500, 520, 260, 180))
        self.widget_12.setObjectName(_fromUtf8("widget_12"))
        self.widget_13 = matplotlibWidget(self.centralwidget)
        self.widget_13.setGeometry(QtCore.QRect(0, 690, 260, 180))
        self.widget_13.setObjectName(_fromUtf8("widget_13"))
        self.widget_14 = matplotlibWidget(self.centralwidget)
        self.widget_14.setGeometry(QtCore.QRect(250, 690, 260, 180))
        self.widget_14.setObjectName(_fromUtf8("widget_14"))

        self.pauseButton = QtGui.QPushButton(self.centralwidget)
        self.pauseButton.setGeometry(QtCore.QRect(780, 180, 85, 27))
        self.pauseButton.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("img/pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseButton.setIcon(icon)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setGeometry(QtCore.QRect(980, 180, 85, 27))
        self.stopButton.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("img/stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopButton.setIcon(icon1)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        
        self.playButton = QtGui.QPushButton(self.centralwidget)
        self.playButton.setGeometry(QtCore.QRect(880, 180, 85, 27))
        self.playButton.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("img/play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.playButton.setIcon(icon2)
        self.playButton.setObjectName(_fromUtf8("playButton"))
        self.textBrowser = QtGui.QPlainTextEdit(self.centralwidget)

        self.textBrowser.setGeometry(QtCore.QRect(760, 290, 331, 500))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setReadOnly(True)

        self.textEdit_2 = QtGui.QTextEdit(self.centralwidget)

        self.textEdit_2.setGeometry(QtCore.QRect(780, 120, 281, 21))
        self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.label = QtGui.QLabel(self.centralwidget)

        self.label.setGeometry(QtCore.QRect(780, 100, 141, 16))
        self.label.setObjectName(_fromUtf8("label"))
        
        self.menubar = QtGui.QMenuBar(EpocGUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.retranslateUi(EpocGUI)
        QtCore.QMetaObject.connectSlotsByName(EpocGUI)

    def retranslateUi(self, EpocGUI):
        EpocGUI.setWindowTitle(QtGui.QApplication.translate("EpocGUI", "Epoc", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("EpocGUI", "Nombre del experimento", None, QtGui.QApplication.UnicodeUTF8))

