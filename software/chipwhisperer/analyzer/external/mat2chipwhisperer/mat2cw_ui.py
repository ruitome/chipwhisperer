# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 474)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.info_tab = QtWidgets.QWidget()
        self.info_tab.setObjectName("info_tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.info_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 40, 471, 211))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.projectname = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectname.sizePolicy().hasHeightForWidth())
        self.projectname.setSizePolicy(sizePolicy)
        self.projectname.setObjectName("projectname")
        self.gridLayout_9.addWidget(self.projectname, 0, 2, 1, 1)
        self.label_numberpoints = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_numberpoints.setObjectName("label_numberpoints")
        self.gridLayout_9.addWidget(self.label_numberpoints, 3, 1, 1, 1)
        self.label_projectauthor = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_projectauthor.setObjectName("label_projectauthor")
        self.gridLayout_9.addWidget(self.label_projectauthor, 1, 1, 1, 1)
        self.projectauthor = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectauthor.sizePolicy().hasHeightForWidth())
        self.projectauthor.setSizePolicy(sizePolicy)
        self.projectauthor.setObjectName("projectauthor")
        self.gridLayout_9.addWidget(self.projectauthor, 1, 2, 1, 1)
        self.label_numbertraces = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_numbertraces.setObjectName("label_numbertraces")
        self.gridLayout_9.addWidget(self.label_numbertraces, 2, 1, 1, 1)
        self.numbertraces = QtWidgets.QLineEdit(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numbertraces.sizePolicy().hasHeightForWidth())
        self.numbertraces.setSizePolicy(sizePolicy)
        self.numbertraces.setObjectName("numbertraces")
        self.gridLayout_9.addWidget(self.numbertraces, 2, 2, 1, 1)
        self.numberpoints = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.numberpoints.setObjectName("numberpoints")
        self.gridLayout_9.addWidget(self.numberpoints, 3, 2, 1, 1)
        self.label_projectname = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_projectname.setObjectName("label_projectname")
        self.gridLayout_9.addWidget(self.label_projectname, 0, 1, 1, 1)
        self.next_button = QtWidgets.QPushButton(self.info_tab)
        self.next_button.setGeometry(QtCore.QRect(410, 320, 75, 23))
        self.next_button.setObjectName("next_button")
        self.tabWidget.addTab(self.info_tab, "")
        self.load_tab = QtWidgets.QWidget()
        self.load_tab.setObjectName("load_tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.load_tab)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupPT = QtWidgets.QGroupBox(self.load_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupPT.sizePolicy().hasHeightForWidth())
        self.groupPT.setSizePolicy(sizePolicy)
        self.groupPT.setObjectName("groupPT")
        self.gridLayout = QtWidgets.QGridLayout(self.groupPT)
        self.gridLayout.setObjectName("gridLayout")
        self.filePT = QtWidgets.QLineEdit(self.groupPT)
        self.filePT.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filePT.sizePolicy().hasHeightForWidth())
        self.filePT.setSizePolicy(sizePolicy)
        self.filePT.setObjectName("filePT")
        self.gridLayout.addWidget(self.filePT, 0, 0, 1, 1)
        self.button_load_pt = QtWidgets.QPushButton(self.groupPT)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_load_pt.sizePolicy().hasHeightForWidth())
        self.button_load_pt.setSizePolicy(sizePolicy)
        self.button_load_pt.setObjectName("button_load_pt")
        self.gridLayout.addWidget(self.button_load_pt, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupPT)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupCT = QtWidgets.QGroupBox(self.load_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupCT.sizePolicy().hasHeightForWidth())
        self.groupCT.setSizePolicy(sizePolicy)
        self.groupCT.setObjectName("groupCT")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupCT)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.fileCT = QtWidgets.QLineEdit(self.groupCT)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileCT.sizePolicy().hasHeightForWidth())
        self.fileCT.setSizePolicy(sizePolicy)
        self.fileCT.setObjectName("fileCT")
        self.gridLayout_2.addWidget(self.fileCT, 0, 0, 1, 1)
        self.button_load_ct = QtWidgets.QPushButton(self.groupCT)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_load_ct.sizePolicy().hasHeightForWidth())
        self.button_load_ct.setSizePolicy(sizePolicy)
        self.button_load_ct.setObjectName("button_load_ct")
        self.gridLayout_2.addWidget(self.button_load_ct, 0, 1, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupCT)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.groupKey = QtWidgets.QGroupBox(self.load_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupKey.sizePolicy().hasHeightForWidth())
        self.groupKey.setSizePolicy(sizePolicy)
        self.groupKey.setObjectName("groupKey")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupKey)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.fileKey = QtWidgets.QLineEdit(self.groupKey)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileKey.sizePolicy().hasHeightForWidth())
        self.fileKey.setSizePolicy(sizePolicy)
        self.fileKey.setObjectName("fileKey")
        self.gridLayout_3.addWidget(self.fileKey, 0, 0, 1, 1)
        self.button_load_key = QtWidgets.QPushButton(self.groupKey)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_load_key.sizePolicy().hasHeightForWidth())
        self.button_load_key.setSizePolicy(sizePolicy)
        self.button_load_key.setObjectName("button_load_key")
        self.gridLayout_3.addWidget(self.button_load_key, 0, 1, 1, 1)
        self.horizontalLayout_3.addWidget(self.groupKey)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.groupTraces = QtWidgets.QGroupBox(self.load_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupTraces.sizePolicy().hasHeightForWidth())
        self.groupTraces.setSizePolicy(sizePolicy)
        self.groupTraces.setObjectName("groupTraces")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupTraces)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.fileTraces = QtWidgets.QLineEdit(self.groupTraces)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileTraces.sizePolicy().hasHeightForWidth())
        self.fileTraces.setSizePolicy(sizePolicy)
        self.fileTraces.setObjectName("fileTraces")
        self.gridLayout_4.addWidget(self.fileTraces, 0, 0, 1, 1)
        self.button_load_traces = QtWidgets.QPushButton(self.groupTraces)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_load_traces.sizePolicy().hasHeightForWidth())
        self.button_load_traces.setSizePolicy(sizePolicy)
        self.button_load_traces.setObjectName("button_load_traces")
        self.gridLayout_4.addWidget(self.button_load_traces, 0, 1, 1, 1)
        self.horizontalLayout_4.addWidget(self.groupTraces)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.group_output = QtWidgets.QGroupBox(self.load_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_output.sizePolicy().hasHeightForWidth())
        self.group_output.setSizePolicy(sizePolicy)
        self.group_output.setObjectName("group_output")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.group_output)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.output_folder = QtWidgets.QLineEdit(self.group_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_folder.sizePolicy().hasHeightForWidth())
        self.output_folder.setSizePolicy(sizePolicy)
        self.output_folder.setObjectName("output_folder")
        self.gridLayout_10.addWidget(self.output_folder, 0, 0, 1, 1)
        self.output_folder_button = QtWidgets.QPushButton(self.group_output)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_folder_button.sizePolicy().hasHeightForWidth())
        self.output_folder_button.setSizePolicy(sizePolicy)
        self.output_folder_button.setObjectName("output_folder_button")
        self.gridLayout_10.addWidget(self.output_folder_button, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.group_output)
        self.back_button = QtWidgets.QPushButton(self.load_tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_button.sizePolicy().hasHeightForWidth())
        self.back_button.setSizePolicy(sizePolicy)
        self.back_button.setObjectName("back_button")
        self.verticalLayout_2.addWidget(self.back_button)
        self.tabWidget.addTab(self.load_tab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.convert_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.convert_button.sizePolicy().hasHeightForWidth())
        self.convert_button.setSizePolicy(sizePolicy)
        self.convert_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.convert_button.setObjectName("convert_button")
        self.verticalLayout.addWidget(self.convert_button, 0, QtCore.Qt.AlignHCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Matlab to Chipwhisperer"))
        self.label_numberpoints.setText(_translate("MainWindow", "Number of Points"))
        self.label_projectauthor.setText(_translate("MainWindow", "Project Autor"))
        self.label_numbertraces.setText(_translate("MainWindow", "Number of Traces"))
        self.label_projectname.setText(_translate("MainWindow", "Project Name"))
        self.next_button.setText(_translate("MainWindow", "Next"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.info_tab), _translate("MainWindow", "Project Info"))
        self.groupPT.setTitle(_translate("MainWindow", "Input Plaintexts"))
        self.button_load_pt.setText(_translate("MainWindow", "Load..."))
        self.groupCT.setTitle(_translate("MainWindow", "Output Ciphertexts"))
        self.button_load_ct.setText(_translate("MainWindow", "Load..."))
        self.groupKey.setTitle(_translate("MainWindow", "Input Known Key"))
        self.button_load_key.setText(_translate("MainWindow", "Load..."))
        self.groupTraces.setTitle(_translate("MainWindow", "Input Traces"))
        self.button_load_traces.setText(_translate("MainWindow", "Load..."))
        self.group_output.setTitle(_translate("MainWindow", "Folder Output"))
        self.output_folder_button.setText(_translate("MainWindow", "Load..."))
        self.back_button.setText(_translate("MainWindow", "Back"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.load_tab), _translate("MainWindow", "Load Files"))
        self.convert_button.setText(_translate("MainWindow", "Convert!"))

