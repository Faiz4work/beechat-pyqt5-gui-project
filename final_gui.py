from PyQt5 import QtCore, QtGui, QtWidgets
from digi.xbee.devices import XBeeDevice



class Ui_Beechat_Networks(object):
    def setupUi(self, Beechat_Networks, device):
        self.device = device
        self.device.open()
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
        font.setPointSize(14)
        self.public_broadcast.setFont(font)
        self.public_broadcast.setStyleSheet("color: rgb(255, 255, 255);")
        self.public_broadcast.setObjectName("public_broadcast")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 60, 371, 51))
        
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #a6a6a6 ;")
        self.label.setObjectName("label")
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 592, 681, 101))
        self.widget.setObjectName("widget")
        
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 661, 90))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(58, 60, 66);\n"
                "color: rgb(255, 255, 255);\n"
                "border-radius: 45px;\n"
                "padding-top: 10px;\n"
                "padding-left: 30px;")
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
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 501, 120))
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
        
        # widget no 7
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
        
        # adding a button to send reply
        self.send_button.clicked.connect(self.add_reply_widget)
        
        # Calling receive message function
        def data_receive_callback(xbee_message):
            self.device_id = xbee_message.remote_device.get_64bit_addr()
            self.client_message = xbee_message.data.decode()
            self.add_cilent_message_widget(self.device_id, self.client_message)

        self.device.add_data_received_callback(data_receive_callback)


    def add_reply_widget(self):
        # getting text and clearing then focus agian on input widget
        self.text = self.plainTextEdit.toPlainText()
        self.plainTextEdit.clear()
        self.plainTextEdit.setFocus()
        
        # widget 8
        self.new_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.new_widget.setMinimumSize(QtCore.QSize(600, 100))
        self.new_widget.setMaximumSize(QtCore.QSize(624, 200))
        # self.new_widget.setStyleSheet("background-color: #4857a8;")
        self.new_widget.setObjectName("new_widget")
        
        self.new_frame = QtWidgets.QFrame(self.new_widget)
        self.new_frame.setGeometry(QtCore.QRect(180, 10, 441, 91))
        self.new_frame.setStyleSheet("background-color: #4857a8;\n"
                "border-radius: 20px;")
        self.new_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.new_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.new_frame.setObjectName("new_frame")
        
        self.flabel_2 = QtWidgets.QLabel(self.new_frame)
        self.flabel_2.setGeometry(QtCore.QRect(30, 20, 431, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.flabel_2.setFont(font)
        self.flabel_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.flabel_2.setWordWrap(True)
        self.flabel_2.setObjectName("flabel_2")
        self.flabel_2.setText(self.text)
        
        self.verticalLayout.addWidget(self.new_widget)
        # sending messgae to client
        self.device.send_data_broadcast(self.text)

    
    # Adding client message in message scroll bar
    def add_cilent_message_widget(self, device_id, client_message):
        self.device_id = device_id
        self.client_message = client_message
        
        # client message widget
        self.new_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.new_widget.setMinimumSize(QtCore.QSize(600, 100))
        self.new_widget.setMaximumSize(QtCore.QSize(624, 200))
        # self.new_widget.setStyleSheet("background-color: #4857a8;")
        self.new_widget.setObjectName("new_widget")
        
        self.new_frame = QtWidgets.QFrame(self.new_widget)
        self.new_frame.setGeometry(QtCore.QRect(0, 0, 501, 120))
        self.new_frame.setStyleSheet("background-color: #1f243f;\n"
                "border-radius: 20px;")
        self.new_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.new_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.new_frame.setObjectName("new_frame")
        
        # Id label
        self.flabel_1 = QtWidgets.QLabel(self.new_frame)
        self.flabel_1.setGeometry(QtCore.QRect(30, 10, 251, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.flabel_1.setFont(font)
        self.flabel_1.setStyleSheet("color: #a6a6a6;")
        self.flabel_1.setObjectName("label_3")
        self.flabel_1.setText(self.device_id)
        
        self.flabel_2 = QtWidgets.QLabel(self.new_frame)
        self.flabel_2.setGeometry(QtCore.QRect(30, 40, 500, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.flabel_2.setFont(font)
        self.flabel_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.flabel_2.setWordWrap(True)
        self.flabel_2.setObjectName("flabel_2")
        self.flabel_2.setText(self.client_message)
        
        self.verticalLayout.addWidget(self.new_widget)
        
if __name__ == "__main__":
    import sys
    
#     Setting xbee device
    # TODO: Replace with the serial port where your local module is connected to.
    PORT = "/dev/ttyUSB0"
    # TODO: Replace with the baud rate of your local module.
    BAUD_RATE = 9600
    device = XBeeDevice(PORT, BAUD_RATE)
    
#     Initiilzing app
    app = QtWidgets.QApplication(sys.argv)
    Beechat_Networks = QtWidgets.QMainWindow()
    ui = Ui_Beechat_Networks()
    ui.setupUi(Beechat_Networks, device)
    Beechat_Networks.show()
    sys.exit(app.exec_())
