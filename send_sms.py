# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'send_sms.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import requests

def SMS(phone='', message=''):
    requests.post(url="https://ghasedakapi.com/v1/sms/send/simple", data = { "message" : message, "Receptor" : phone, "linenumber" : "10000000007997" }, headers = { "apikey": "" })
    return True

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(706, 379)
        MainWindow.setMinimumSize(QtCore.QSize(706, 379))
        MainWindow.setMaximumSize(QtCore.QSize(706, 379))
        MainWindow.setAutoFillBackground(True)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.phone = QtWidgets.QLineEdit(self.centralwidget)
        self.phone.setGeometry(QtCore.QRect(450, 80, 201, 29))
        self.phone.setObjectName("phone")
        self.message = QtWidgets.QLineEdit(self.centralwidget)
        self.message.setGeometry(QtCore.QRect(450, 120, 201, 121))
        self.message.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.message.setObjectName("message")
        self.send = QtWidgets.QPushButton(self.centralwidget)
        self.send.setGeometry(QtCore.QRect(460, 260, 95, 27))
        self.send.setObjectName("send")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 70, 281, 201))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("./message.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(-10, 0, 731, 411))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.raise_()
        self.phone.raise_()
        self.message.raise_()
        self.send.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.send.clicked.connect(self.sendMessage)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def sendMessage(self):
        phone = self.phone.text()
        message = self.message.text()
        if len(phone) == 11 and len(message) != 0:
            SMS(phone=phone, message=message)
        else:
            return False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ارسال پیامک"))
        self.phone.setPlaceholderText(_translate("MainWindow", "شماره موبایل"))
        self.message.setPlaceholderText(_translate("MainWindow", "متن پیام"))
        self.send.setText(_translate("MainWindow", "ارسال"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

