from PyQt5 import QtWidgets


def display_dialog(__type, window_text, text):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(__type)
    msg.setWindowTitle(str(window_text))
    msg.setText(str(text))
    msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
    msg.exec_()


def load_pt(gui):
    filename = QtWidgets.QFileDialog.getOpenFileNames(caption='Load Plaintexts', filter='*.txt')
    if filename[0]:
        try:
            gui.filelist_pt = [x.encode() for x in filename[0] if not x.startswith("_")]
            if len(filename[0]) > 1:
                gui.filePT.setText(str(len(filename[0])) + " files selected")
            else:
                gui.filePT.setText(str(gui.filelist_pt[0]))
        except Exception as e:
            display_dialog(QtWidgets.QMessageBox.Warning, "Error importing " + filename, e)

def load_ct(gui):
    filename = QtWidgets.QFileDialog.getOpenFileNames(caption='Load Ciphertexts', filter='*.txt')
    if filename[0]:
        try:
            gui.filelist_ct = [x.encode() for x in filename[0] if not x.startswith("_")]
            if len(filename[0]) > 1:
                gui.fileCT.setText(str(len(filename[0])) + " files selected")
            else:
                gui.fileCT.setText(str(gui.filelist_ct[0]))
        except Exception as e:
            display_dialog(QtWidgets.QMessageBox.Warning, "Error importing " + filename, e)

def load_key(gui):
    filename = QtWidgets.QFileDialog.getOpenFileNames(caption='Load Keylist', filter='*.txt')
    if filename[0]:
        try:
            gui.filelist_keylist = [x.encode() for x in filename[0] if not x.startswith("_")]
            if len(filename[0]) > 1:
                gui.fileKey.setText(str(len(filename[0])) + " files selected")
            else:
                gui.fileKey.setText(str(gui.filelist_keylist[0]))
        except Exception as e:
            display_dialog(QtWidgets.QMessageBox.Warning, "Error importing " + filename, e)

def load_traces(gui):
    filename = QtWidgets.QFileDialog.getOpenFileNames(caption='Load Traces', filter='*.mat')
    if filename[0]:
        try:
            gui.filelist_traces = [x.encode() for x in filename[0] if not x.startswith("_")]
            if len(filename[0]) > 1:
                gui.fileTraces.setText(str(len(filename[0])) + " files selected")
            else:
                gui.fileTraces.setText(str(gui.filelist_traces[0]))
        except Exception as e:
            display_dialog(QtWidgets.QMessageBox.Warning, "Error importing " + filename, e)
