import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import time
import mainwindow

class MainDialog(QMainWindow, mainwindow.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.setText("Process")
        self.connect(self.pushButton, SIGNAL("clicked()"), self.processData)

        self.workerThread = WorkerThread()

        self.connect(self.workerThread, SIGNAL("threadDone(QString)"), self.threadDone, Qt.DirectConnection)

    def processData(self):
        self.workerThread.start()
        QMessageBox.information(self, "Done!", "Done")

    def threadDone(self, text):
        self.lineEdit.setText("Thread finished")
        print text

class WorkerThread(QThread):

    def __init__(self, parent=None):
        super(WorkerThread, self).__init__(parent)

    def run(self):
        time.sleep(3)
        self.emit(SIGNAL("threadDone(QString)"), "Confirmation that thread is finished")

app = QApplication(sys.argv)
program = MainDialog()
program.show()
app.exec_()

