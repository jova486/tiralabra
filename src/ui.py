"""
Created on Fri Jan 14 18:26:35 2022

@author: jovajova
"""
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QFileDialog, QGridLayout, QGroupBox, QVBoxLayout, QPushButton, QCheckBox, QListWidget


from PyQt5.QtCore import pyqtSlot

from service import service


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Melodymaker'
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

        file_open_melody = QPushButton('Melodiatiedosto', self)
        file_open_rythm = QPushButton('Rytmitiedosto', self)
        file_open_melody.clicked.connect(self.on_open_melody)
        file_open_rythm.clicked.connect(self.on_open_rythm)

        file_save = QPushButton('Tallenna', self)
        file_save.clicked.connect(self.on_save)

        self.file_melody_label = QLabel(self)
        self.file_melody_label.setText("Melodia: ")
        self.file_rythm_label = QLabel(self)
        self.file_rythm_label.setText("Rytmi:")

        self.radioButton_use_rythm = QCheckBox(
            'Käytä alkuperäistä rytmiä', self)
        self.radioButton_use_rythm.toggled.connect(self.on_use_rythm_selected)

        Vbox1 = QVBoxLayout()
        Vbox2 = QVBoxLayout()
        Vbox1.addWidget(file_open_melody)
        Vbox1.addWidget(file_open_rythm)
        Vbox1.addWidget(file_save)

        Vbox2.addWidget(self.file_melody_label)
        Vbox2.addWidget(self.file_rythm_label)
        Vbox2.addWidget(self.radioButton_use_rythm)

        self.listWidged = QListWidget()

        windowLayout = QGridLayout()
        windowLayout.addWidget(self.horizontalGroupBox, 2, 1)
        windowLayout.addWidget(self.listWidged, 2, 2)
        horizontalGroupBox2 = QGroupBox()
        horizontalGroupBox3 = QGroupBox()

        horizontalGroupBox2.setLayout(Vbox1)
        horizontalGroupBox3.setLayout(Vbox2)

        windowLayout.addWidget(horizontalGroupBox2, 1, 1)
        windowLayout.addWidget(horizontalGroupBox3, 1, 2)
        self.setLayout(windowLayout)

        self.show()

    def createHorizontalLayout(self):
        self.horizontalGroupBox = QGroupBox()
        layout = QVBoxLayout()

        self.time_signature_qlabel = QLabel(self)
        self.time_signature_qlabel.setText("Tahtilaji = 4/4")
        self.markov_depth_qlabel = QLabel(self)
        self.markov_depth_qlabel.setText("ketjun aste = 2")

        self.time_signature_combo = QComboBox(self)
        self.time_signature_combo.addItem("4/4")
        self.time_signature_combo.addItem("3/4")
        self.time_signature_combo.addItem("2/4")
        self.time_signature_combo.addItem("6/8")
        self.time_signature_combo.addItem("5/8")
        self.time_signature_combo.activated[str].connect(
            self.on_time_signature_combo_Changed)

        self.markov_depth_combo = QComboBox(self)
        self.markov_depth_combo.addItem("1")
        self.markov_depth_combo.addItem("2")
        self.markov_depth_combo.addItem("3")
        self.markov_depth_combo.addItem("4")
        self.markov_depth_combo.setCurrentIndex(1)

        self.markov_depth_combo.activated[str].connect(
            self.on_markov_depth_combo_Changed)

        self.reset_trie = QPushButton('Tyhjennä muisti', self)
        self.reset_trie.clicked.connect(self.on_reset_trie)

        layout.addWidget(self.time_signature_combo)
        layout.addWidget(self.time_signature_qlabel)
        layout.addWidget(self.markov_depth_combo)
        layout.addWidget(self.markov_depth_qlabel)
        layout.addWidget(self.reset_trie)

        self.horizontalGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_open_melody(self):
        self.openFileNameDialog("melody")

    @pyqtSlot()
    def on_open_rythm(self):
        self.openFileNameDialog("rythm")

    def on_show_filelist(self):
        self.listWidged.clear()
        for file in service.midifile_name_melody_array:
            self.listWidged.addItem(file)

    @pyqtSlot()
    def on_save(self):
        self.saveFileDialog()

    @pyqtSlot()
    def on_time_signature_combo_Changed(self):
        text = self.time_signature_combo.currentText()
        self.time_signature_qlabel.setText("Tahtilaji = " + text)
        service.set_time_signature(text)
        self.time_signature_qlabel.adjustSize()

    @pyqtSlot()
    def on_reset_trie(self):
        service.reset_trie()
        self.on_show_filelist()

    @pyqtSlot()
    def on_markov_depth_combo_Changed(self):
        text = self.markov_depth_combo.currentText()
        self.markov_depth_qlabel.setText("markov syvyys = " + text)
        service.set_markov_depth(text)
        self.time_signature_qlabel.adjustSize()

    def on_use_rythm_selected(self):
        service.use_original_rythm = not service.use_original_rythm

    def openFileNameDialog(self, text):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "Avaa midi file " + text, "", "midifiles (*.mid)", options=options)
        if fileName:
            if text == "melody":
                self.file_melody_label.setText("Melodia: " + fileName)

            else:
                self.file_rythm_label.setText("Rytmi:" + fileName)

            service.add_file_name(fileName, text)
        self.on_show_filelist()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(
            self, "Tallenna midi tiedosto", "", "midifiles (*.mid)", options=options)
        if fileName:
            service.save_midi_file(fileName)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
