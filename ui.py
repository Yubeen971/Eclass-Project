import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui

wasClicked = False
class FirstWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = "CSV Path Chosen"
        self.success = "Quiz Transferred Successfully!"
        self.bye = "Please Choose a CSV Path"
        self.button = QtWidgets.QPushButton("Choose the path to your csv file")
        self.button2 = QtWidgets.QPushButton("Move Quiz Data")
        self.text = QtWidgets.QLabel("Welcome to the Quiz Relocator", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.button2)

        self.button.clicked.connect(self.onClicked)
        self.button2.clicked.connect(self.onMoveClick)
    
    def onClicked(self):
        self.text.setText(self.hello)
        wasClicked = True
        print(wasClicked)
        return wasClicked
    
    def onMoveClick(self):
        if (wasClicked == True):
            self.text.setText(self.success)
        else:
            self.text.setText(self.bye)


if (__name__ == "__main__"):
    app = QtWidgets.QApplication([])

    widget = FirstWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec())