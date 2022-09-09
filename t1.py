# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import (QWidget, QSlider, QLineEdit, QLabel, QPushButton, QScrollArea,QApplication,
                             QHBoxLayout, QVBoxLayout, QMainWindow, QFrame)
from PyQt5.QtCore import Qt, QSize, QRect, QMetaObject, QCoreApplication
from PyQt5 import QtWidgets, uic, QtGui
import sys

class Ui_Beechat_Networks(object):
    def setupUi(self, Beechat_Networks):
        # Setting initial height for storing new messages
        self.initial_height = 475
        self.each_height_gap_single_line = 110
        self.each_height_gap_double_line = 135
        self.last_message_bubble_height = 60
        self.last_message_is_mine = True 
        
            
        Beechat_Networks.setObjectName("Beechat_Networks")
        # Beechat_Networks.resize(730, 700)
        Beechat_Networks.setFixedSize(730, 700)
        # setting font
        QtGui.QFontDatabase.addApplicationFont("Nunito.ttf")
        font = QtGui.QFont("Nunito", 14)
        
        # setting id font
        id_font = QtGui.QFont("Nunito", 12)
        
        Beechat_Networks.setFont(font)
        Beechat_Networks.setWindowOpacity(1.0)
        Beechat_Networks.setAutoFillBackground(False)
        Beechat_Networks.setStyleSheet("background-color:  #010523;")
        self.centralwidget = QtWidgets.QWidget(Beechat_Networks)
        self.centralwidget.setObjectName("centralwidget")
        
        self.scroll = QScrollArea(self.centralwidget)
        self.widget = QWidget()
        # self.scroll.setGeometry(QRect(30, 150, 600, 400))
        self.vbox = QVBoxLayout()
        
        # logo
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QRect(20, 20, 100, 100))
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        
        # public broadcast label
        self.public_broadcast = QtWidgets.QLabel(self.centralwidget)
        self.public_broadcast.setGeometry(QRect(150, 20, 371, 61))

        self.public_broadcast.setFont(font)
        self.public_broadcast.setStyleSheet("color: rgb(255, 255, 255);")
        self.public_broadcast.setObjectName("public_broadcast")

        
        # id label
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QRect(150, 65, 400, 51))
        self.label.setFont(font)
        self.label.setStyleSheet("color: #a6a6a6 ;")
        self.label.setObjectName("label")
        
        # horizontal line

        self.line1 = QtWidgets.QFrame(self.centralwidget)
        self.line1.setObjectName(u"line")
        self.line1.setGeometry(QRect(40, 140, 650, 1))
        # self.line1.setCursor(QCursor(Qt.PointingHandCursor))
        self.line1.setStyleSheet("background-color: white;")
        # self.line1.setLineWidth(2)
        self.line1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line1.setFrameShadow(QtWidgets.QFrame.Sunken)

# ********************************************************************************************
        # frame 1
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QRect(0, 10, 500, 90))
        self.frame1.setStyleSheet("background-color: #1f243f;\n"
                        "border-radius: 20px;")
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        
        # label 2 (into frame 1)
        self.label_2 = QtWidgets.QLabel(self.frame1)
        self.label_2.setGeometry(QRect(30, 0, 271, 41))
        
        self.label_2.setFont(id_font)
        self.label_2.setStyleSheet("color: #a6a6a6;")
        self.label_2.setObjectName("label_2")
        
        # label 3 (into frame1)
        self.label_3 = QtWidgets.QLabel(self.frame1)
        self.label_3.setGeometry(QRect(30, 40, 281, 41))
        # font = QtGui.QFont()
        # font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        
# **********************************************************************************************
        # frame 2 starts here
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        # self.frame_2.setGeometry(QtCore.QRect(0, 110, 500, 120))
        self.frame_2.setStyleSheet("background-color: #1f243f;\n"
                "border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        # message id label
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QRect(30, 0, 271, 41))
        # font = QtGui.QFont()
        # font.setPointSize(14)
        self.label_4.setFont(id_font)
        self.label_4.setStyleSheet("color: #a6a6a6;")
        self.label_4.setObjectName("label_4")
        
        # message
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QRect(30, 40, 451, 68))
        # font = QtGui.QFont()
        # font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setTextFormat(Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")

# *******************************************************************************
     
        # reply message frame
        self.reply = QtWidgets.QFrame(self.centralwidget)
        self.reply.setGeometry(QRect(280, 250, 371, 60))
        self.reply.setStyleSheet("background-color: #4857a8;\n"
                "border-radius: 20px;")
        self.reply.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.reply.setFrameShadow(QtWidgets.QFrame.Raised)
        self.reply.setObjectName("reply")
        
        # reply label inside reply_frame
        self.label_7 = QtWidgets.QLabel(self.reply)
        self.label_7.setGeometry(QRect(30, 10, 281, 41))
        # font = QtGui.QFont()
        # font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        
        # input widget
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QRect(20, 550, 681, 101))
        self.widget1.setObjectName("widget")
        
        # plain text edit inside qwidget
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget1)
        # font = QtGui.QFont()
        # font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setGeometry(QRect(10, 0, 640, 90))
        self.plainTextEdit.setStyleSheet("background-color: rgb(58, 60, 66);\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius: 20px;\n"
                "padding: 20px;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        # send button inside qwidget
        self.send_button = QtWidgets.QPushButton(self.widget1)
        self.send_button.setGeometry(QRect(590, 0, 90, 90))
        # font = QtGui.QFont()
        # font.setPointSize(14)
        self.send_button.setFont(font)
        self.send_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-radius: 45px;\n"
                "border: 2px solid white;")
        self.send_button.setObjectName("send_button")
        
        
        Beechat_Networks.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Beechat_Networks)
        self.menubar.setGeometry(QRect(0, 0, 730, 22))
        self.menubar.setObjectName("menubar")
        Beechat_Networks.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Beechat_Networks)
        self.statusbar.setObjectName("statusbar")
        Beechat_Networks.setStatusBar(self.statusbar)

        self.retranslateUi(Beechat_Networks)
        QMetaObject.connectSlotsByName(Beechat_Networks)
        
        # setting up scrollable layout
        self.vbox.addWidget(self.frame1)
        self.vbox.addWidget(self.frame_2)
        self.vbox.addWidget(self.reply)

        
        self.widget.setLayout(self.vbox)
        
        #Scroll Area Properties
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setFixedSize(600, 400)
        self.scroll.setWidget(self.widget)

        # self.centralwidget.setWidget(self.scroll)
        # self.setCentralWidget(self.scroll)


    def retranslateUi(self, Beechat_Networks):
        _translate = QCoreApplication.translate
        Beechat_Networks.setWindowTitle(_translate("Beechat_Networks", "Beechat Networks"))
        self.public_broadcast.setText(_translate("Beechat_Networks", "Public broadcast"))
        self.label.setText(_translate("Beechat_Networks", "My ID: 0013A20041EFADC2"))
        self.label_2.setText(_translate("Beechat_Networks", "0013A20041EFADC2"))
        self.label_3.setText(_translate("Beechat_Networks", "Hello Everyone"))
        self.label_4.setText(_translate("Beechat_Networks", "0013A20041EFADC2"))
        self.label_5.setText(_translate("Beechat_Networks", "Hello Everyone this is a message that is 73 characters long."))
        self.label_7.setText(_translate("Beechat_Networks", "Hello Everyone"))
        self.send_button.setText(_translate("Beechat_Networks", "send"))
        self.send_button.clicked.connect(self.send_message)
        
        
        
    
    def send_message(self):
        self.text = self.plainTextEdit.toPlainText()
        self.plainTextEdit.clear()
        self.plainTextEdit.setFocus()
        
        # showing message in front of window as my message
        # making a new frame 
        self.new_frame = QtWidgets.QFrame()
        if self.last_message_bubble_height == 60:
                self.current_height = self.each_height_gap_single_line
        elif self.last_message_bubble_height == 120:
                self.current_height = self.each_height_gap_double_line
                
        self.height = self.initial_height + self.current_height
        
        # Making a new frame
        # self.new_frame.setGeometry(QRect(320, self.height, 371, 60))
        self.new_frame.setStyleSheet("background-color: #4857a8;\n"
                "border-radius: 20px;")
        self.new_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.new_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.new_frame.setObjectName("new_frame")
        
        self.new_label = QLabel(self.new_frame)
        self.new_label.setText(self.text)
        
        self.vbox.addWidget(self.new_frame)
        
        # self.scroll.setGeometry(QRect(30, 150, 600, 500))
        print(self.text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Beechat_Networks = QtWidgets.QMainWindow()
    ui = Ui_Beechat_Networks()
    ui.setupUi(Beechat_Networks)
    Beechat_Networks.show()
    sys.exit(app.exec_())
