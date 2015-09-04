import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__appname__ = "Ninth Video"


class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)

        btn = QPushButton("Open Dialog")
        self.label1 = QLabel("Label 1 Result")
        self.label2 = QLabel("Label 2 Result")

        layout = QVBoxLayout()
        layout.addWidget(btn)
        layout.addWidget(self.label1)
        layout.addWidget(self.label2)
        self.setLayout(layout)

        self.connect(btn, SIGNAL("clicked()"), self.dialogOpen)

    def dialogOpen(self):
        dialog = Dialog()
        if dialog.exec_():
            self.label1.setText("Spinbox value is " + str(dialog.spinBox.value()))
            self.label2.setText("Checkbox is " + str(dialog.checkBox.isChecked()))
        else:
            QMessageBox.warning(self, __appname__, "Dialog canceled")

class Dialog(QDialog):

    def __init__(self, parent=None):
        super(Dialog, self).__init__(parent)

        self.setWindowTitle("Dialog")

        self.checkBox = QCheckBox("Check me out!")
        self.spinBox = QSpinBox()
        buttonOk = QPushButton("OK")
        buttonCancel = QPushButton("Cancel")

        layout = QGridLayout()
        layout.addWidget(self.spinBox, 0, 0)
        layout.addWidget(self.checkBox, 0, 1)
        layout.addWidget(buttonOk)
        layout.addWidget(buttonCancel)
        self.setLayout(layout)

        self.connect(buttonOk, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))


app = QApplication(sys.argv)
program = Program()
program.show()
app.exec_()

