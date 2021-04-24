from PySide6 import Qt
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from reservation_page import Ui_window
from reservation import Reservation
from admin_page import Ui_Admin
from admin import Admin
import sys

class Application(QMainWindow):
    def __init__(self, parent=None):
        super(Application, self).__init__(parent)
        self.reservation_button = QPushButton("Reservation")
        self.reservation_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: rgb(0, 59, 76);\n"
"    min-width: 80px;\n"
"}")
        self.catalog_button = QPushButton("Car catalog")
        self.catalog_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: rgb(0, 59, 76);\n"
"    min-width: 80px;\n"
"}")
        self.history_button = QPushButton("Car history")
        self.history_button.setStyleSheet(u"QPushButton {\n"
"    color: white;\n"
"    background-color: rgb(0, 59, 76);\n"
"    min-width: 80px;\n"
"}")

        layout = QGridLayout()
        self.setLayout(layout)

        groupbox = QGroupBox("Menu")
        layout.addWidget(groupbox)
        
        vbox = QVBoxLayout()
        groupbox.setLayout(vbox)
        vbox.addWidget(self.reservation_button)
        vbox.addWidget(self.catalog_button)
        vbox.addWidget(self.history_button)

        
        self.setCentralWidget(groupbox)
 
        self.reservation_button.clicked.connect(self.showReservation)
        self.catalog_button.clicked.connect(self.showCatalog)
        self.history_button.clicked.connect(self.showHistory)
        self.reservation = Reservation()
        self.admin = Admin()
        
 
    def showReservation(self):
        self.reservation.show()
    def showCatalog(self):
        print("catalog")
    def showHistory(self):
        self.admin.show()

 
 
def main():
    app = QApplication(sys.argv)
    main = Application()
    main.show()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()