from PySide6 import Qt
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_window(object):
    def setupUi(self, window):
        if not window.objectName():
            window.setObjectName(u"window")
        window.resize(650, 450)
        window.setMinimumSize(QSize(650, 450))
        window.setMaximumSize(QSize(650, 450))
        self.label = QLabel(window)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 20, 241, 21))
        font = QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel{\n"
"background-color:rgb(0, 45, 61);\n"
"color:white;\n"
"}")
        self.selectModel_label = QLabel(window)
        self.selectModel_label.setObjectName(u"selectModel_label")
        self.selectModel_label.setGeometry(QRect(40, 70, 151, 16))
        self.listWidget = QListWidget(window)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(40, 90, 231, 121))
        self.listWidget.setStyleSheet(u"QListWidget {\n"
"    border: 2px solid gray;\n"
"    border-radius: 3px;\n"
"    background-color: rgb(0, 59, 76);\n"
"    color: white;\n"
"}")
        self.pickup_label = QLabel(window)
        self.pickup_label.setObjectName(u"pickup_label")
        self.pickup_label.setGeometry(QRect(40, 220, 141, 16))
        self.pickup_dateEdit = QDateEdit(window)
        self.pickup_dateEdit.setObjectName(u"pickup_dateEdit")
        self.pickup_dateEdit.setGeometry(QRect(40, 240, 110, 22))
        self.pickup_dateEdit.setDate(QDate(2021,1,1))
        self.pickup_timeEdit = QTimeEdit(window)
        self.pickup_timeEdit.setObjectName(u"pickup_timeEdit")
        self.pickup_timeEdit.setGeometry(QRect(160, 240, 118, 22))
        self.return_label = QLabel(window)
        self.return_label.setObjectName(u"return_label")
        self.return_label.setGeometry(QRect(40, 280, 131, 16))
        self.return_timeEdit = QTimeEdit(window)
        self.return_timeEdit.setObjectName(u"return_timeEdit")
        self.return_timeEdit.setGeometry(QRect(160, 300, 118, 22))
        self.return_dateEdit = QDateEdit(window)
        self.return_dateEdit.setObjectName(u"return_dateEdit")
        self.return_dateEdit.setGeometry(QRect(40, 300, 110, 22))
        self.return_dateEdit.setDate(QDate(2021,1,1))
        self.service_label = QLabel(window)
        self.service_label.setObjectName(u"service_label")
        self.service_label.setGeometry(QRect(40, 340, 91, 16))
        self.serviceBranch_comboBox = QComboBox(window)
        self.serviceBranch_comboBox.setObjectName(u"serviceBranch_comboBox")
        self.serviceBranch_comboBox.setGeometry(QRect(40, 360, 241, 21))
        self.serviceBranch_comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    padding: 1px 18px 1px 3px;\n"
"    min-width: 6em;\n"
"}")
        self.name_label = QLabel(window)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setGeometry(QRect(40, 385, 91, 16))
        self.name_lineEdit = QLineEdit(window)
        self.name_lineEdit.setObjectName(u"days_lineEdit")
        self.name_lineEdit.setGeometry(QRect(40, 405, 240, 21))
        # self.map_button = QPushButton(window)
        # self.map_button.setObjectName(u"map_button")
        # self.map_button.setGeometry(QRect(90, 390, 131, 31))
        self.confirmation_label = QLabel(window)
        self.confirmation_label.setObjectName(u"confirmation_label")
        self.confirmation_label.setGeometry(QRect(390, 70, 181, 16))
        font1 = QFont()
        font1.setPointSize(15)
        self.confirmation_label.setFont(font1)
        self.model_label = QLabel(window)
        self.model_label.setObjectName(u"model_label")
        self.model_label.setGeometry(QRect(350, 100, 81, 16))
        self.pph_label = QLabel(window)
        self.pph_label.setObjectName(u"pph_label")
        self.pph_label.setGeometry(QRect(350, 140, 91, 16))
        self.interval_label = QLabel(window)
        self.interval_label.setObjectName(u"interval_label")
        self.interval_label.setGeometry(QRect(350, 180, 101, 16))
        self.days_label = QLabel(window)
        self.days_label.setObjectName(u"days_label")
        self.days_label.setGeometry(QRect(350, 220, 71, 16))
        self.branch_label = QLabel(window)
        self.branch_label.setObjectName(u"branch_label")
        self.branch_label.setGeometry(QRect(350, 260, 101, 16))
        self.price_label = QLabel(window)
        self.price_label.setObjectName(u"price_label")
        self.price_label.setGeometry(QRect(350, 300, 81, 16))
        self.model_lineEdit = QLineEdit(window)
        self.model_lineEdit.setObjectName(u"model_lineEdit")
        self.model_lineEdit.setGeometry(QRect(430, 100, 181, 21))
        self.model_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    color: rgb(0, 59, 76);\n"
"}")
        self.pph_lineEdit = QLineEdit(window)
        self.pph_lineEdit.setObjectName(u"pph_lineEdit")
        self.pph_lineEdit.setGeometry(QRect(450, 141, 161, 20))
        self.pph_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    color: rgb(0, 59, 76);\n"
"}")
        self.interval_lineEdit = QLineEdit(window)
        self.interval_lineEdit.setObjectName(u"interval_lineEdit")
        self.interval_lineEdit.setGeometry(QRect(460, 180, 151, 21))
        self.interval_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    color: rgb(0, 59, 76);\n"
"}")
        self.days_lineEdit = QLineEdit(window)
        self.days_lineEdit.setObjectName(u"days_lineEdit")
        self.days_lineEdit.setGeometry(QRect(420, 220, 191, 21))
        self.days_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    color: rgb(0, 59, 76);\n"
"}")
        self.branch_lineEdit = QLineEdit(window)
        self.branch_lineEdit.setObjectName(u"branch_lineEdit")
        self.branch_lineEdit.setGeometry(QRect(460, 260, 151, 21))
        self.branch_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    color: rgb(0, 59, 76);\n"
"}")
        self.price_lineEdit = QLineEdit(window)
        self.price_lineEdit.setObjectName(u"price_lineEdit")
        self.price_lineEdit.setGeometry(QRect(430, 300, 181, 21))
        self.price_lineEdit.setStyleSheet(u"QLineEdit {\n"
"    border: 1px solid gray;\n"
"    border-radius: 3px;\n"
"    color: rgb(0, 59, 76);\n"
"}")
        self.display_button = QPushButton(window)
        self.display_button.setObjectName(u"display_button")
        self.display_button.setGeometry(QRect(370, 340, 231, 38))
        self.display_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"    background-color: rgb(0, 59, 76);\n"
"    min-width: 80px;\n"
"}")
        self.confirm_button = QPushButton(window)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.setGeometry(QRect(430, 390, 111, 41))
        self.confirm_button.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #8f8f91;\n"
"    border-radius: 6px;\n"
"    color: white;\n"
"    background-color: rgb(0, 183, 224);\n"
"    min-width: 80px;\n"
"}")
        self.line = QFrame(window)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(300, 60, 20, 371))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.retranslateUi(window)

        QMetaObject.connectSlotsByName(window)
    # setupUi

    def retranslateUi(self, window):
        window.setWindowTitle(QCoreApplication.translate("window", u"Reservation", None))
        self.label.setText(QCoreApplication.translate("window", u"   CAR RENTAL RESERVATION", None))
        self.selectModel_label.setText(QCoreApplication.translate("window", u"select car model:", None))
        self.pickup_label.setText(QCoreApplication.translate("window", u"Pick up date and time:", None))
        self.return_label.setText(QCoreApplication.translate("window", u"Return date and time:", None))
        self.service_label.setText(QCoreApplication.translate("window", u"Service branch:", None))
        # self.map_button.setText(QCoreApplication.translate("window", u"Explore in Map", None))
        self.name_label.setText(QCoreApplication.translate("window", u"Username:", None))
        self.confirmation_label.setText(QCoreApplication.translate("window", u"Reservation Confirmation", None))
        self.model_label.setText(QCoreApplication.translate("window", u"car model:", None))
        self.pph_label.setText(QCoreApplication.translate("window", u"Price per hour:", None))
        self.interval_label.setText(QCoreApplication.translate("window", u"Rental's interval:", None))
        self.days_label.setText(QCoreApplication.translate("window", u"Total days:", None))
        self.branch_label.setText(QCoreApplication.translate("window", u"Service branch:", None))
        self.price_label.setText(QCoreApplication.translate("window", u"Total price:", None))
        self.display_button.setText(QCoreApplication.translate("window", u"Display reservation information", None))
        self.confirm_button.setText(QCoreApplication.translate("window", u"confirm", None))
    # retranslateUi
