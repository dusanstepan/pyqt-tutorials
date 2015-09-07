import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__appname__ = "Ninth Video"


class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        self.setWindowTitle(__appname__)

        btn = QPushButton("Open Dialog")
        self.mainSpinBox = QSpinBox()
        self.mainCheckBox = QCheckBox("Main Checkbox Value")

        layout = QVBoxLayout()
        layout.addWidget(self.mainSpinBox)
        layout.addWidget(self.mainCheckBox)
        layout.addWidget(btn)
        self.setLayout(layout)

        self.connect(btn, SIGNAL("clicked()"), self.dialogOpen)

    def dialogOpen(self):
        initValues = {'mainSpinBox' : self.mainSpinBox.value(), 'mainCheckBox' : self.mainCheckBox.isChecked()}
        dialog = Dialog(initValues)
        if dialog.exec_():
            self.mainSpinBox.setValue(dialog.spinBox.value())
            self.mainCheckBox.setChecked(dialog.checkBox.isChecked())

class Dialog(QDialog):

    def __init__(self, initValues, parent=None):
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
        
        self.spinBox.setValue(initValues['mainSpinBox'])
        self.checkBox.setChecked(initValues['mainCheckBox'])

        self.connect(buttonOk, SIGNAL("clicked()"), self, SLOT("accept()"))
        self.connect(buttonCancel, SIGNAL("clicked()"), self, SLOT("reject()"))

    def accept(self):

        class GreaterThanFive(Exception): pass
        class IsZero(Exception): pass

        try:
            if self.spinBox.value() > 5:
                raise GreaterThanFive("The spinBox value cannot be greater than 5")
            elif self.spinBox.value() == 0:
                raise IsZero("The spinBox value cannot be equal to zero")
        except GreaterThanFive, e:
            QMessageBox.warning(self, __appname__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return
        except IsZero, e:
            QMessageBox.warning(self, __appname__, str(e))
            self.spinBox.selectAll()
            self.spinBox.setFocus()
            return
        else:
            QDialog.accept(self)


app = QApplication(sys.argv)
program = Program()
program.show()
app.exec_()

