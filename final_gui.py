from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Beechat_Networks(object):
    def setupUi(self, Beechat_Networks):
        Beechat_Networks.setObjectName("Beechat_Networks")
        Beechat_Networks.resize(709, 743)
        font = QtGui.QFont()
        font.setPointSize(14)
        Beechat_Networks.setFont(font)
        Beechat_Networks.setWindowOpacity(1.0)
        Beechat_Networks.setAutoFillBackground(False)
        Beechat_Networks.setStyleSheet("background-color:  #010523;")
        self.centralwidget = QtWidgets.QWidget(Beechat_Networks)
        self.centralwidget.setObjectName("centralwidget")
        
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(20, 20, 91, 91))
        self.logo.setPixmap(QtGui.QPixmap("logo.png"))
        self.logo.setScaledContents(True)
        self.logo.setObjectName("logo")
        
        self.public_broadcast = QtWidgets.QLabel(self.centralwidget)
        self.public_broadcast.setGeometry(QtCore.QRect(180, 10, 371, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.public_broadcast.setFont(font)
        self.public_broadcast.setStyleSheet("color: rgb(255, 255, 255);")
        self.public_broadcast.setObjectName("public_broadcast")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 60, 371, 51))
        
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #a6a6a6 ;")
        self.label.setObjectName("label")
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 592, 681, 101))
        self.widget.setObjectName("widget")
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 661, 90))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(58, 60, 66);\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius: 45px;\n"
                "padding: 10px;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        
        self.send_button = QtWidgets.QPushButton(self.widget)
        self.send_button.setGeometry(QtCore.QRect(590, 0, 90, 90))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.send_button.setFont(font)
        self.send_button.setStyleSheet("color: rgb(255, 255, 255);\n"
                "border-radius: 45px;\n"
                "border: 2px solid white;")
        self.send_button.setObjectName("send_button")
        
        # Scroll area starts
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(20, 170, 671, 401))
        self.scrollArea.setStyleSheet("background-color: rgb(1, 5, 35);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 643, 443))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_2.setMinimumSize(QtCore.QSize(600, 100))
        self.widget_2.setMaximumSize(QtCore.QSize(624, 200))
        self.widget_2.setStyleSheet("")
        self.widget_2.setObjectName("widget_2")
        
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setGeometry(QtCore.QRect(-1, 0, 501, 91))
        self.frame.setStyleSheet("background-color: #1f243f;\n"
                "border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: #a6a6a6;")
        self.label_2.setObjectName("label_2")
        
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(30, 40, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        
        self.verticalLayout.addWidget(self.widget_2)
        
        self.widget_6 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_6.setMinimumSize(QtCore.QSize(600, 100))
        self.widget_6.setMaximumSize(QtCore.QSize(624, 200))
        self.widget_6.setStyleSheet("")
        self.widget_6.setObjectName("widget_6")
        
        self.frame_2 = QtWidgets.QFrame(self.widget_6)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 501, 101))
        self.frame_2.setStyleSheet("background-color: #1f243f;\n"
                "border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: #a6a6a6;")
        self.label_3.setObjectName("label_3")
        
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 40, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        
        self.verticalLayout.addWidget(self.widget_6)
        
        self.widget_7 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_7.setMinimumSize(QtCore.QSize(600, 100))
        self.widget_7.setMaximumSize(QtCore.QSize(624, 200))
        self.widget_7.setStyleSheet("")
        self.widget_7.setObjectName("widget_7")
        
        self.frame_3 = QtWidgets.QFrame(self.widget_7)
        self.frame_3.setGeometry(QtCore.QRect(180, 10, 441, 91))
        self.frame_3.setStyleSheet("background-color: #4857a8;\n"
"border-radius: 20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        
        self.verticalLayout.addWidget(self.widget_7)
        
        self.widget_8 = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.widget_8.setMinimumSize(QtCore.QSize(600, 100))
        self.widget_8.setMaximumSize(QtCore.QSize(624, 200))
        self.widget_8.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.widget_8.setObjectName("widget_8")
        
        self.verticalLayout.addWidget(self.widget_8)
        
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 120, 671, 2))
        self.line.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        Beechat_Networks.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Beechat_Networks)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 709, 22))
        self.menubar.setObjectName("menubar")
        Beechat_Networks.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Beechat_Networks)
        self.statusbar.setObjectName("statusbar")
        Beechat_Networks.setStatusBar(self.statusbar)

        self.retranslateUi(Beechat_Networks)
        QtCore.QMetaObject.connectSlotsByName(Beechat_Networks)

    def retranslateUi(self, Beechat_Networks):
        _translate = QtCore.QCoreApplication.translate
        Beechat_Networks.setWindowTitle(_translate("Beechat_Networks", "MainWindow"))
        self.public_broadcast.setText(_translate("Beechat_Networks", "Public broadcast"))
        self.label.setText(_translate("Beechat_Networks", "My ID: 0013A20041EFADC2"))
        self.send_button.setText(_translate("Beechat_Networks", "send"))
        self.label_2.setText(_translate("Beechat_Networks", "0013A20041EFD42C"))
        self.label_4.setText(_translate("Beechat_Networks", "Hello Everyone!"))
        self.label_3.setText(_translate("Beechat_Networks", "0013A20041EFD42C"))
        self.label_5.setText(_translate("Beechat_Networks", "Hello Everyone! Here is the characters which is not more then 73 characters"))
        self.label_6.setText(_translate("Beechat_Networks", "Hello Everyone!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Beechat_Networks = QtWidgets.QMainWindow()
    ui = Ui_Beechat_Networks()
    ui.setupUi(Beechat_Networks)
    Beechat_Networks.show()
    sys.exit(app.exec_())
