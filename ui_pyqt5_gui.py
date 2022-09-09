# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pyqt5_guiUOgSWo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Beechat_Networks(object):
    def setupUi(self, Beechat_Networks):
        if not Beechat_Networks.objectName():
            Beechat_Networks.setObjectName(u"Beechat_Networks")
        Beechat_Networks.resize(706, 702)
        font = QFont()
        font.setPointSize(14)
        Beechat_Networks.setFont(font)
        Beechat_Networks.setWindowOpacity(1.000000000000000)
        Beechat_Networks.setAutoFillBackground(False)
        Beechat_Networks.setStyleSheet(u"background-color:  #010523;")
        self.centralwidget = QWidget(Beechat_Networks)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo = QLabel(self.centralwidget)
        self.logo.setObjectName(u"logo")
        self.logo.setGeometry(QRect(20, 10, 151, 151))
        self.logo.setPixmap(QPixmap(u"logo.png"))
        self.logo.setScaledContents(True)
        self.public_broadcast = QLabel(self.centralwidget)
        self.public_broadcast.setObjectName(u"public_broadcast")
        self.public_broadcast.setGeometry(QRect(240, 30, 371, 61))
        font1 = QFont()
        font1.setPointSize(27)
        self.public_broadcast.setFont(font1)
        self.public_broadcast.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(240, 100, 371, 51))
        font2 = QFont()
        font2.setPointSize(20)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: #a6a6a6 ;")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 550, 681, 101))
        self.plainTextEdit = QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 0, 641, 90))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(58, 60, 66);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 45px;\n"
"padding: 10px;")
        self.send_button = QPushButton(self.widget)
        self.send_button.setObjectName(u"send_button")
        self.send_button.setGeometry(QRect(590, 0, 90, 90))
        self.send_button.setFont(font)
        self.send_button.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border-radius: 45px;\n"
"border: 2px solid white;")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 180, 661, 351))
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.scrollArea = QScrollArea(self.frame)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 641, 330))
        self.scrollArea.setMaximumSize(QSize(16777215, 330))
        self.scrollArea.setStyleSheet(u"background-color: rgb(85, 255, 127);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 639, 328))
        self.formLayout = QFormLayout(self.scrollAreaWidgetContents_2)
        self.formLayout.setObjectName(u"formLayout")
        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(400, 200))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 30, 47, 14))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.frame_3)

        self.frame_4 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(400, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.frame_4)

        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(400, 200))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 30, 47, 14))

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.frame_2)

        self.frame_5 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(400, 200))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.frame_5)

        self.frame_6 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(400, 200))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 20, 47, 14))

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.frame_6)

        self.frame_7 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(359, 177))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 20, 47, 14))

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.frame_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        Beechat_Networks.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Beechat_Networks)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 706, 22))
        Beechat_Networks.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Beechat_Networks)
        self.statusbar.setObjectName(u"statusbar")
        Beechat_Networks.setStatusBar(self.statusbar)

        self.retranslateUi(Beechat_Networks)

        QMetaObject.connectSlotsByName(Beechat_Networks)
    # setupUi

    def retranslateUi(self, Beechat_Networks):
        Beechat_Networks.setWindowTitle(QCoreApplication.translate("Beechat_Networks", u"MainWindow", None))
        self.logo.setText("")
        self.public_broadcast.setText(QCoreApplication.translate("Beechat_Networks", u"Public broadcast", None))
        self.label.setText(QCoreApplication.translate("Beechat_Networks", u"My ID: 0013A20041EFADC2", None))
        self.send_button.setText(QCoreApplication.translate("Beechat_Networks", u"send", None))
        self.label_2.setText(QCoreApplication.translate("Beechat_Networks", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Beechat_Networks", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Beechat_Networks", u"TextLabel", None))
        self.label_6.setText(QCoreApplication.translate("Beechat_Networks", u"TextLabel", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Beechat_Networks = QtWidgets.QMainWindow()
    ui = Ui_Beechat_Networks()
    ui.setupUi(Beechat_Networks)
    Beechat_Networks.show()
    sys.exit(app.exec_())