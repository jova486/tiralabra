import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QHBoxLayout, QGroupBox, QDialog, QVBoxLayout, QPushButton, QRadioButton
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import pyqtSlot, QRect

from service import service


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'MelodyMaker'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 220
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createHorizontalLayout()

        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)

        self.show()

    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox("MelodyMaker Ui")
        layout = QHBoxLayout()

        file_open = QPushButton('Open file', self)
        file_open.clicked.connect(self.on_open)
        layout.addWidget(file_open)
        file_save = QPushButton('Save file', self)
        file_save.clicked.connect(self.on_save)
        layout.addWidget(file_save)

        radioButton_male = QRadioButton('use rythm of the file', self)
        #radioButton_male.setGeometry(QRect(180, 120, 95, 20))

        radioButton_male.toggled.connect(self.on_maleselected)
        layout.addWidget(radioButton_male)

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_open(self):
        self.openFileNameDialog()

    @pyqtSlot()
    def on_save(self):
        self.saveFileDialog()

    @pyqtSlot()
    def on_maleselected(self):
        service.use_original_rythm = not service.use_original_rythm

    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;midifiles (*.mid)", options=options)
        if fileName:
            service.open_file(fileName)

    def openFileNamesDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(
            self, "QFileDialog.getOpenFileNames()", "", "All Files (*);;midifiles (*.mid)", options=options)
        if files:
            print(files)

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self, "QFileDialog.getSaveFileName()", "", "All Files (*);;midifiles (*.mid)", options=options)
        if fileName:
            service.save_midi_file(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
