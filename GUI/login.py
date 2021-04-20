import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from login_page import Ui_login_widget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_login_widget()
    ui.setupUi(Form)
    Form.show()
    
    sys.exit(app.exec_())