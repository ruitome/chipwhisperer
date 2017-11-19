import sys
#from chipwhisperer.analyzer.extenal.mat2chipwhisperer.mat2cw_ui import *
#from chipwhisperer.analyzer.extenal.mat2chipwhisperer.ctcw import *
#from chipwhisperer.analyzer.extenal.mat2chipwhisperer.load_files import *
from mat2cw_ui import *
from ctcw import CTCW
from load_files import *

from PyQt5 import QtWidgets, QtGui

class Matlab2CW(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(Matlab2CW, self).__init__(parent)
        self.setupUi(self)
        self.next_button.clicked.connect(self.next_tab)
        self.back_button.clicked.connect(self.previous_tab)
        self.convert_button.setDisabled(True)
        self.button_load_pt.clicked.connect(lambda: load_pt(self))
        self.button_load_ct.clicked.connect(lambda: load_ct(self))
        self.button_load_key.clicked.connect(lambda: load_key(self))
        self.button_load_traces.clicked.connect(lambda: load_traces(self))
        self.output_folder_button.clicked.connect(self.select_output_folder)
        self.filePT.textChanged.connect(self.check_parameters)
        self.fileCT.textChanged.connect(self.check_parameters)
        self.fileKey.textChanged.connect(self.check_parameters)
        self.fileTraces.textChanged.connect(self.check_parameters)
        self.output_folder.textChanged.connect(self.check_parameters)
        self.PROJECT_NAME = ""
        self.PROJECT_AUTHOR = ""
        self.NUMBER_TRACES = 0
        self.NUMBER_POINTS = 0
        self.filelist_pt = ""
        self.filelist_ct = ""
        self.filelist_keylist = ""
        self.filelist_traces = ""
        self.output_folder_path = ""
        self.convert_button.clicked.connect(self.convert)


    def next_tab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() +1)

    def previous_tab(self):
        self.tabWidget.setCurrentIndex(self.tabWidget.currentIndex() - 1)

    def set_project_info(self):
        self.PROJECT_NAME = str(self.projectname.text())
        self.PROJECT_AUTHOR = str(self.projectauthor.text())
        if self.numbertraces.text() != "":
            self.NUMBER_TRACES = int(self.numbertraces.text())

        if self.numberpoints.text() != "":
            self.NUMBER_POINTS = int(self.numberpoints.text())

    def check_parameters(self):
        self.set_project_info()
        if ((len(self.PROJECT_NAME) > 0) and (len(self.PROJECT_AUTHOR) > 0) and (self.NUMBER_TRACES > 0)
            and (self.NUMBER_POINTS > 0) and (len(self.filelist_pt) > 0) and (len(self.filelist_ct) > 0)
            and (len(self.filelist_keylist) > 0) and len(self.output_folder_path) > 0) and (len(self.filelist_traces) > 0) :
            self.convert_button.setDisabled(False)


    def select_output_folder(self):
        self.output_folder_path = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")) + "/"
        self.output_folder.setText(self.output_folder_path)

    def convert(self):
        try:
            self.ctcw = CTCW(self.PROJECT_NAME, self.PROJECT_AUTHOR,  self.NUMBER_TRACES, self.NUMBER_POINTS,
                                  self.output_folder_path)
            self.ctcw.config_gen()
            self.ctcw.load_traces(self.filelist_traces)
            self.ctcw.load_plaintexts(self.filelist_pt)
            self.ctcw.load_ciphertexts(self.filelist_ct)
            self.ctcw.load_key(self.filelist_keylist)
            self.ctcw.load_keylist(self.filelist_keylist)
            self.ctcw.cwp_gen()
        except Exception as e:
            display_dialog(QtWidgets.QMessageBox.Warning, "Error", e)
        else:
            display_dialog(QtWidgets.QMessageBox.Information, "Done", "Done!")

def main():
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
        form = Matlab2CW()
        form.show()
        app.exec_()

if __name__ == "__main__":
    main()