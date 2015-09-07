import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import mainwindow

class MainDialog(QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.connect(self.pushButton, SIGNAL("clicked()"), self.showMessageBox)

    def showMessageBox(self):
        QMessageBox.information(self, "Hello!", "Hello there " + self.lineEdit.text());



app = QApplication(sys.argv)
program = MainDialog()
program.show()
app.exec_()

