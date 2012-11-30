# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MandelbrotGui.ui'
#
# Created: Wed Nov 28 22:23:27 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainGui(object):
    def setupUi(self, MainGui):
        MainGui.setObjectName(_fromUtf8("MainGui"))
        MainGui.setWindowModality(QtCore.Qt.WindowModal)
        MainGui.resize(400, 569)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainGui.setFont(font)
        self.centralwidget = QtGui.QWidget(MainGui)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 410, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.MaxIterations = QtGui.QLineEdit(self.centralwidget)
        self.MaxIterations.setGeometry(QtCore.QRect(140, 410, 250, 20))
        self.MaxIterations.setObjectName(_fromUtf8("MaxIterations"))
        self.XCenter = QtGui.QLineEdit(self.centralwidget)
        self.XCenter.setGeometry(QtCore.QRect(140, 440, 250, 20))
        self.XCenter.setObjectName(_fromUtf8("XCenter"))
        self.YCenter = QtGui.QLineEdit(self.centralwidget)
        self.YCenter.setGeometry(QtCore.QRect(140, 470, 250, 20))
        self.YCenter.setObjectName(_fromUtf8("YCenter"))
        self.Width = QtGui.QLineEdit(self.centralwidget)
        self.Width.setGeometry(QtCore.QRect(140, 500, 250, 20))
        self.Width.setObjectName(_fromUtf8("Width"))
        self.GenerateBtn = QtGui.QPushButton(self.centralwidget)
        self.GenerateBtn.setGeometry(QtCore.QRect(10, 530, 380, 30))
        self.GenerateBtn.setObjectName(_fromUtf8("GenerateBtn"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 440, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 470, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 500, 130, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.Viewer = QtGui.QLabel(self.centralwidget)
        self.Viewer.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.Viewer.setMinimumSize(QtCore.QSize(400, 400))
        self.Viewer.setAutoFillBackground(False)
        self.Viewer.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.Viewer.setText(_fromUtf8(""))
        self.Viewer.setMargin(0)
        self.Viewer.setIndent(0)
        self.Viewer.setObjectName(_fromUtf8("Viewer"))
        self.LoadingView = QtGui.QLabel(self.centralwidget)
        self.LoadingView.setGeometry(QtCore.QRect(167, 167, 66, 66))
        self.LoadingView.setObjectName(_fromUtf8("LoadingView"))
        MainGui.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainGui)
        QtCore.QMetaObject.connectSlotsByName(MainGui)

    def retranslateUi(self, MainGui):
        MainGui.setWindowTitle(QtGui.QApplication.translate("MainGui", "Mandelbrot Fractal Generator", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainGui", "Max Iterations", None, QtGui.QApplication.UnicodeUTF8))
        self.GenerateBtn.setText(QtGui.QApplication.translate("MainGui", "Generate Fractal Image", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainGui", "X Center", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainGui", "Y Center", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainGui", "Width", None, QtGui.QApplication.UnicodeUTF8))
        self.LoadingView.setText(QtGui.QApplication.translate("MainGui", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

