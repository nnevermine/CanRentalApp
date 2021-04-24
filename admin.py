from PySide6 import Qt
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import sqlite3
from sqlite3 import Error
import datetime
from datetime import date
from admin_page import Ui_Admin

class Admin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Admin()
        self.ui.setupUi(self)
        self.dbConnection = None
        self.initDBConnection()
        self.showOngoing()
        self.showCompleted()
    def initDBConnection(self):
        try:
            self.dbConnection = sqlite3.connect("/Users/nnevermine/Desktop/carRental.db")
            print("connected to database")
        except Error as e:
            print(e)

        return self.dbConnection
    def showOngoing(self):
        tableRow = 0
        self.ui.onGoing_table.setColumnCount(8)
        self.ui.onGoing_table.setHorizontalHeaderLabels(["username", " car id", "car model", "interval", "pick-up time", "return time", "branch", "income"])
        result = self.dbConnection.cursor().execute("""SELECT * FROM admin""")
    
        for row_no, row_data in enumerate(result):
            interval = row_data[3].split(" ")
            #get pick up date
            pickUp = interval[0]
            currentDate = datetime.datetime.now()
            expectedDate = pickUp + " " + row_data[4][:-3]
            expectedDate = datetime.datetime.strptime(expectedDate, "%d/%m/%Y %H:%M")

            #still on going date
            if(currentDate <= expectedDate):
                self.ui.onGoing_table.insertRow(tableRow)
                for col_no, col_data in enumerate(row_data):
                    item = str(col_data)
                    self.ui.onGoing_table.setItem(tableRow, col_no, QTableWidgetItem(item))
        self.ui.onGoing_table.verticalHeader().setDefaultSectionSize(10)

    def showCompleted(self):
        tableRow = 0
        self.ui.completed_table.setColumnCount(8)
        self.ui.completed_table.setHorizontalHeaderLabels(["username", " car id", "car model", "interval", "pick-up time", "return time", "branch", "income"])
        result = self.dbConnection.cursor().execute("""SELECT * FROM admin""")
    
        for row_no, row_data in enumerate(result):
            interval = row_data[3].split(" ")
            #get pick up date
            pickUp = interval[0]
            currentDate = datetime.datetime.now()
            expectedDate = pickUp + " " + row_data[4][:-3]
            expectedDate = datetime.datetime.strptime(expectedDate, "%d/%m/%Y %H:%M")

            #completed history
            if(currentDate > expectedDate):
                self.ui.completed_table.insertRow(tableRow)
                for col_no, col_data in enumerate(row_data):
                    item = str(col_data)
                    self.ui.completed_table.setItem(tableRow, col_no, QTableWidgetItem(item))
        self.ui.completed_table.verticalHeader().setDefaultSectionSize(10)