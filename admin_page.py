# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Admin(object):
    def setupUi(self, Admin):
        if not Admin.objectName():
            Admin.setObjectName(u"Admin")
        Admin.resize(650, 450)
        Admin.setMinimumSize(QSize(650, 450))
        Admin.setMaximumSize(QSize(650, 450))
        self.centralwidget = QWidget(Admin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 0, 561, 41))
        font = QFont()
        font.setFamily(u"Arial Black")
        font.setPointSize(25)
        font.setBold(True)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 50, 71, 16))
        self.onGoing_table = QTableWidget(self.centralwidget)
        self.onGoing_table.setObjectName(u"onGoing_table")
        self.onGoing_table.setGeometry(QRect(30, 70, 591, 141))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 220, 71, 16))
        self.completed_table = QTableWidget(self.centralwidget)
        self.completed_table.setObjectName(u"completed_table")
        self.completed_table.setGeometry(QRect(30, 240, 591, 141))
        Admin.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Admin)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 650, 22))
        Admin.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Admin)
        self.statusbar.setObjectName(u"statusbar")
        Admin.setStatusBar(self.statusbar)

        self.retranslateUi(Admin)

        QMetaObject.connectSlotsByName(Admin)
    # setupUi

    def retranslateUi(self, Admin):
        Admin.setWindowTitle(QCoreApplication.translate("Admin", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Admin", u"RENTAL RESERVATION HISTORY", None))
        self.label_2.setText(QCoreApplication.translate("Admin", u"on-going", None))
        self.label_3.setText(QCoreApplication.translate("Admin", u"completed", None))
    # retranslateUi

