from PySide6 import Qt
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
import sqlite3
from sqlite3 import Error
from datetime import date
from reservation_page import Ui_window

class Reservation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_window()
        self.ui.setupUi(self)
        self.dbConnection = None
        self.initDBConnection()
        #list of information
        self.info =[]
        #check wheter user click display before confirm
        self.dis = False


        #combo box setup
        branches = ["rama 3", "Sathorn", "Ladkrabang", "Rangsit", "Siam"]
        for b in branches:
                self.ui.serviceBranch_comboBox.addItem(b)

        #model list setup
        self.showList()
        self.ui.display_button.clicked.connect(self.display)
        self.ui.confirm_button.clicked.connect(self.confirm)

    def initDBConnection(self):
        try:
            self.dbConnection = sqlite3.connect("/Users/nnevermine/Desktop/carRental.db")
            print("connected to database")
        except Error as e:
            print(e)

        return self.dbConnection

    def showList(self):
        result = self.dbConnection.cursor().execute("""SELECT carModel,available FROM carCatalog""")
        for row_no, row_data in enumerate(result):
            #show only the available car
            if(row_data[1] > 0):
                item = QListWidgetItem(row_data[0])
                self.ui.listWidget.addItem(item)
    def display(self):
        #mark that user has clicked the display button before confirm
        self.dis = True

        #car model
        model = str(self.ui.listWidget.currentItem().text())
        self.ui.model_lineEdit.setText(model)

        #price per hour
        result = self.dbConnection.cursor().execute("""SELECT car_id, pph FROM carCatalog WHERE carModel=?""",(model,))
        for row_no, row_data in enumerate(result):
            car_id = row_data[0]
            pph = row_data[1]
        self.ui.pph_lineEdit.setText(str(pph) + " baht")

        #interval
        startD = int(self.ui.pickup_dateEdit.date().day())
        startM = int(self.ui.pickup_dateEdit.date().month())
        startY = int(self.ui.pickup_dateEdit.date().year())
        start = str(startD) + "/" + str(startM) + "/" + str(startY)

        endD = int(self.ui.return_dateEdit.date().day())
        endM = int(self.ui.return_dateEdit.date().month())
        endY = int(self.ui.return_dateEdit.date().year())
        end = str(endD) + "/" + str(endM) + "/" + str(endY)

        interval = str(start) + " to " + str(end)
        self.ui.interval_lineEdit.setText(interval)
        
        #no. of days
        s_date = date(startY, startM, startD)
        e_date = date(endY, endM, endD)
        delta = e_date - s_date
        days = delta.days
        #return same date
        if days == 0:
            days = 1
        self.ui.days_lineEdit.setText(str(days))

        #service branch
        branch = self.ui.serviceBranch_comboBox.currentText()
        self.ui.branch_lineEdit.setText(branch)

        #price
        price = pph * days
        self.ui.price_lineEdit.setText(str(price) + " baht")

        #username
        name = self.ui.name_lineEdit.text()

        #time
        pickup_time = self.ui.pickup_timeEdit.time().toString()
        return_time = self.ui.return_timeEdit.time().toString()

        #gather all information(username, carmodel, interval, pick-up time, return time, branch, total income)
        self.info = [name,car_id,model,interval,pickup_time,return_time,branch,price]
        
    def confirm(self):
        #has to click display before confirm
        if self.dis == True:
            #update car avilability
            result = self.dbConnection.cursor().execute("""UPDATE carCatalog SET available = 0 WHERE car_id = ?""",(self.info[1],))
            self.dbConnection.commit()
            item = self.ui.listWidget.currentItem()
            self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

            #insert data into the database
            adminTable = self.dbConnection.cursor().execute("""INSERT INTO admin(username, carId, carModel, interval, pickupTime, returnTime, branch, income)VALUES(?,?,?,?,?,?,?,?)""", tuple(self.info))
            self.dbConnection.commit()

            #insert data to userHistory
            adminTable = self.dbConnection.cursor().execute("""INSERT INTO userHistory(username, carId, carModel, interval, pickupTime, returnTime, branch, price)VALUES(?,?,?,?,?,?,?,?)""", tuple(self.info))
            self.dbConnection.commit()

            #clear lineEdits ready for other reservation
            self.ui.model_lineEdit.setText("")
            self.ui.pph_lineEdit.setText("")
            self.ui.interval_lineEdit.setText("")
            self.ui.days_lineEdit.setText("")
            self.ui.branch_lineEdit.setText("")
            self.ui.price_lineEdit.setText("")
            self.dis = False

            dialog = QMessageBox()
            dialog.setText("Reservation successful")
            dialog.exec_()