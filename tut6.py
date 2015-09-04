import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

__appname__ = "Eight video"

class Program(QDialog):

    def __init__(self, parent=None):
        super(Program, self).__init__(parent)

        openButton = QPushButton("Open")
        saveButton = QPushButton("Save")
        dirButton = QPushButton("Other")
        closeButton = QPushButton("Close...")

        self.connect(openButton, SIGNAL("clicked()"), self.open)
        self.connect(saveButton, SIGNAL("clicked()"), self.save)

        layout = QVBoxLayout()
        layout.addWidget(openButton)
        layout.addWidget(saveButton)
        layout.addWidget(dirButton)
        layout.addWidget(closeButton)
        self.setLayout(layout)

    def open(self):
        
        dir = "."

        fileObj = QFileDialog.getOpenFileName(self, __appname__ + " Open File Dialog", directory = dir, filter = "Text files (*.py)")
        print fileObj
        print type(fileObj)

        fileName = fileObj
        file = open(fileName, 'r')
        read = file.read()
        file.close()
        print read

    def save(self):
        
        dir = "."

        fileObj = QFileDialog.getSaveFileName(self, __appname__ + " Open File Dialog", directory = dir, filter = "Text files (*.py)")
        print fileObj
        print type(fileObj)

        contents = "Hello from Dusan"

        fileName = fileObj
        file = open(fileName, "w")
        file.write(contents)
        file.close()

app = QApplication(sys.argv)
program = Program()
program.show()
app.exec_()

