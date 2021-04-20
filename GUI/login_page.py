# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6 import Qt
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import images_rc

class Ui_login_widget(object):
    def setupUi(self, login_widget):
        if not login_widget.objectName():
            login_widget.setObjectName(u"login_widget")
        login_widget.setEnabled(True)
        login_widget.resize(700, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login_widget.sizePolicy().hasHeightForWidth())
        login_widget.setSizePolicy(sizePolicy)
        login_widget.setMinimumSize(QSize(700, 500))
        login_widget.setMaximumSize(QSize(650, 450))
        login_widget.setAcceptDrops(False)
        login_widget.setStyleSheet(u"QWidget {\n"
"	background-image: url(:/login/login_background.png);\n"
"	background-repeat: no-repeat;\n"
"	backgrond-position: center;\n"
"}\n"
"\n"
"QFrame {\n"
"	background: none;\n"
"	background-color: white;\n"
"	border-radius: 10px;\n"
"	alignment: center;\n"
"	padding-right: 10px;\n"
"	padding-left: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"	background: none;\n"
"	color: #0c7b93;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background: none;\n"
"	background-color: white;\n"
"	border-style: outset;\n"
"	border-width: 2px;\n"
"	border-color: #0c7b93;\n"
"	border-top: none;\n"
"	border-left: none;\n"
"	border-right: none;\n"
"}")
        self.verticalLayout = QVBoxLayout(login_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 10, 60)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 61)
        self.label = QLabel(login_widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(200, 50))
        font = QFont()
        font.setPointSize(32)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"QLabel {\n"
"	background: none;\n"
"	padding-left: 10px;\n"
"	color: white;\n"
"}")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft)

        self.pushButton_2 = QPushButton(login_widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        font1 = QFont()
        font1.setPointSize(16)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background: none;\n"
"	border: none;\n"
"	color: rgb(17, 135, 157);\n"
"	text-align: right;\n"
"	padding-right: 50px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(183, 182, 184);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.login_frame = QFrame(login_widget)
        self.login_frame.setObjectName(u"login_frame")
        sizePolicy.setHeightForWidth(self.login_frame.sizePolicy().hasHeightForWidth())
        self.login_frame.setSizePolicy(sizePolicy)
        self.login_frame.setMinimumSize(QSize(350, 250))
        self.login_frame.setMaximumSize(QSize(350, 250))
        self.login_frame.setFocusPolicy(Qt.NoFocus)
        self.login_frame.setStyleSheet(u"")
        self.login_frame.setFrameShape(QFrame.StyledPanel)
        self.login_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.login_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.login_label = QLabel(self.login_frame)
        self.login_label.setObjectName(u"login_label")
        self.login_label.setMaximumSize(QSize(120, 35))
        font2 = QFont()
        font2.setPointSize(28)
        self.login_label.setFont(font2)
        self.login_label.setStyleSheet(u"QLabel {\n"
"	padding: 0px;\n"
"}")
        self.login_label.setScaledContents(False)
        self.login_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.login_label)


        self.username_field = QLineEdit(self.login_frame)
        self.username_field.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setMinimumSize(QSize(300, 40))
        self.username_field.setMaximumSize(QSize(300, 40))
        font3 = QFont()
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(True)
        self.username_field.setFont(font3)
        self.username_field.setFocusPolicy(Qt.ClickFocus)
        self.username_field.setStyleSheet(u"")
        self.username_field.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.username_field.setClearButtonEnabled(False)

        self.verticalLayout_3.addWidget(self.username_field)

        self.password_field = QLineEdit(self.login_frame)
        self.password_field.setAttribute(Qt.WA_MacShowFocusRect, 0)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setMinimumSize(QSize(300, 40))
        self.password_field.setMaximumSize(QSize(300, 40))
        self.password_field.setFocusPolicy(Qt.ClickFocus)
        self.password_field.setStyleSheet(u"")
        self.password_field.setEchoMode(QLineEdit.Password)

        self.verticalLayout_3.addWidget(self.password_field)

        self.horizontalLayout = QHBoxLayout()
#ifndef Q_OS_MAC
        self.horizontalLayout.setSpacing(-1)
#endif
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout.setContentsMargins(0, -1, -1, -1)
        self.pushButton = QPushButton(self.login_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 40))
        self.pushButton.setMaximumSize(QSize(150, 40))
        font4 = QFont()
        font4.setPointSize(14)
        self.pushButton.setFont(font4)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background: none;\n"
"	border: none;\n"
"	color: rgb(50, 50, 50);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	color: rgb(17, 135, 157);\n"
"}")

        self.horizontalLayout.addWidget(self.pushButton)

        self.signin_button = QPushButton(self.login_frame)
        self.signin_button.setObjectName(u"signin_button")
        self.signin_button.setMinimumSize(QSize(100, 40))
        self.signin_button.setMaximumSize(QSize(100, 40))
        self.signin_button.setStyleSheet(u"QPushButton {\n"
"	background: none;\n"
"	background-color: #0c7b93;\n"
"	border-radius: 10px;\n"
"	font: bold;\n"
"	font-size: 18px;\n"
"	color: #FFFFFF;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background: none;\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #0C5A76, stop: 1 #0c7b93);\n"
"}")

        self.horizontalLayout.addWidget(self.signin_button)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 1)

        self.verticalLayout.addWidget(self.login_frame, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.verticalLayout.setStretch(1, 2)

        self.retranslateUi(login_widget)

        QMetaObject.connectSlotsByName(login_widget)
    # setupUi

    def retranslateUi(self, login_widget):
        login_widget.setWindowTitle(QCoreApplication.translate("login_widget", u"CarRental", None))
        self.label.setText(QCoreApplication.translate("login_widget", u"<html><head/><body><p><span style=\" color:#adafb4;\">Car</span><span style=\" color:#dadee2;\">Rental</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("login_widget", u"Create Account", None))
        self.login_label.setText(QCoreApplication.translate("login_widget", u"<strong>Login</strong>", None))
        self.username_field.setText("")
        self.username_field.setPlaceholderText(QCoreApplication.translate("login_widget", u"Username", None))
        self.password_field.setText("")
        self.password_field.setPlaceholderText(QCoreApplication.translate("login_widget", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("login_widget", u"Forgot Password", None))
        self.signin_button.setText(QCoreApplication.translate("login_widget", u"Sign In", None))
    # retranslateUi

