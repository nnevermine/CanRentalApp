import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from login_page import Ui_login_widget
import sqlite3
from sqlite3 import Error

class Login(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        # databaseManagement.__init__(self)
        self.ui = Ui_login_widget()
        self.ui.setupUi(self)
        self.ui.signin_button.clicked.connect(self.signin)
        
    def signin(self):
        name = self.ui.username_field.text()

        pwd  = self.getPassword(name)
        #If the user enter the registered username
        if pwd:
            #correct password
            if self.ui.password_field.text() == self.decryptPassword(pwd):
                print("logging in")
            #wrong password
            else:
                print("Wrong password")
                self.ui.password_field.setText("")

    def getPassword(self, name):
        conn = None
        try:
            conn = sqlite3.connect(r"/Users/nnevermine/Documents/GitHub/CarRentalApp/userInfo.db")
            cur = conn.cursor()
            cur.execute("SELECT * FROM userInformation WHERE userName=?", (name,))
            rows = cur.fetchall()
            # enter invalid username
            if len(rows) == 0:
                print("Invalid username")
                self.ui.username_field.setText("")
                return
            else:
                return rows[0][1]
        except Error as e:
            print(e)
        
    def decryptPassword(self, pwd):
        #reverse cipher decryption
        translated =  ""  
        i = len(pwd)  -  1   
        while  i >=  0 :   
                translated = translated + pwd[i]      
                i  =  i  - 1     
        return translated
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Login()
    w.show()
    sys.exit(app.exec_())

