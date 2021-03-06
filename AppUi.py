# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(939, 641)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        MainWindow.setFont(font)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setMouseTracking(False)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setAccessibleName("")
        MainWindow.setAccessibleDescription("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.sendArea = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2 = QtWidgets.QGroupBox(self.sendArea)
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sendArea.sizePolicy().hasHeightForWidth())
        self.sendArea.setSizePolicy(sizePolicy)
        self.sendArea.setObjectName("sendArea")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.sendArea)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 300))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setCheckable(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.editCmd1 = QtWidgets.QLineEdit(self.groupBox_2)
        self.btnSendCmd1 = QtWidgets.QPushButton(self.groupBox_2)
        self.editCmd2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.btnSendCmd2 = QtWidgets.QPushButton(self.groupBox_2)
        self.editCmd3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.btnSendCmd3 = QtWidgets.QPushButton(self.groupBox_2)
        self.editCmd4 = QtWidgets.QLineEdit(self.groupBox_2)
        self.btnSendCmd4 = QtWidgets.QPushButton(self.groupBox_2)
        self.editCmd5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.btnSendCmd5 = QtWidgets.QPushButton(self.groupBox_2)
        self.editCmd6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.btnSendCmd6 = QtWidgets.QPushButton(self.groupBox_2)
        self.editCmd7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.btnSendCmd7 = QtWidgets.QPushButton(self.groupBox_2)
        self.editCmd8 = QtWidgets.QLineEdit(self.groupBox_2)
        self.btnSendCmd8 = QtWidgets.QPushButton(self.groupBox_2)
        self.editCmd9 = QtWidgets.QLineEdit(self.groupBox_2)
        self.btnSendCmd9 = QtWidgets.QPushButton(self.groupBox_2)
        self.editCmd10 = QtWidgets.QLineEdit(self.groupBox_2)
        self.btnSendCmd10 = QtWidgets.QPushButton(self.groupBox_2)
        self.editInterval = QtWidgets.QLineEdit(self.sendArea)
        self.btnAutoSend = QtWidgets.QPushButton(self.sendArea)
        self.editSendData = QtWidgets.QTextEdit(self.sendArea)
        self.checkStringSend = QtWidgets.QCheckBox(self.sendArea)
        self.btnSend = QtWidgets.QPushButton(self.sendArea)
        self.btnSendCmd8.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSendCmd8.setObjectName("btnSendCmd8")
        self.gridLayout_3.addWidget(self.btnSendCmd8, 7, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 8, 0, 1, 1)
        self.editCmd9.setClearButtonEnabled(True)
        self.editCmd9.setObjectName("editCmd9")
        self.gridLayout_3.addWidget(self.editCmd9, 8, 1, 1, 1)
        self.btnSendCmd9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSendCmd9.setObjectName("btnSendCmd9")
        self.gridLayout_3.addWidget(self.btnSendCmd9, 8, 2, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 7, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 9, 0, 1, 1)
        self.editCmd8.setClearButtonEnabled(True)
        self.editCmd8.setObjectName("editCmd8")
        self.gridLayout_3.addWidget(self.editCmd8, 7, 1, 1, 1)
        self.editCmd7.setClearButtonEnabled(True)
        self.editCmd7.setObjectName("editCmd7")
        self.gridLayout_3.addWidget(self.editCmd7, 6, 1, 1, 1)
        self.btnSendCmd7.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSendCmd7.setObjectName("btnSendCmd7")
        self.gridLayout_3.addWidget(self.btnSendCmd7, 6, 2, 1, 1)
        self.btnSendCmd1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSendCmd1.setObjectName("btnSendCmd1")
        self.gridLayout_3.addWidget(self.btnSendCmd1, 0, 2, 1, 1)
        self.editCmd3.setClearButtonEnabled(True)
        self.editCmd3.setObjectName("editCmd3")
        self.gridLayout_3.addWidget(self.editCmd3, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.editCmd6.setClearButtonEnabled(True)
        self.editCmd6.setObjectName("editCmd6")
        self.gridLayout_3.addWidget(self.editCmd6, 5, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 5, 0, 1, 1)
        self.btnSendCmd6.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSendCmd6.setObjectName("btnSendCmd6")
        self.gridLayout_3.addWidget(self.btnSendCmd6, 5, 2, 1, 1)
        self.cmd1 = QtWidgets.QLabel(self.groupBox_2)
        self.cmd1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cmd1.setObjectName("cmd1")
        self.gridLayout_3.addWidget(self.cmd1, 0, 0, 1, 1)
        self.editCmd5.setClearButtonEnabled(True)
        self.editCmd5.setObjectName("editCmd5")
        self.gridLayout_3.addWidget(self.editCmd5, 4, 1, 1, 1)
        self.btnSendCmd4.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSendCmd4.setObjectName("btnSendCmd4")
        self.gridLayout_3.addWidget(self.btnSendCmd4, 3, 2, 1, 1)
        self.editCmd4.setClearButtonEnabled(True)
        self.editCmd4.setObjectName("editCmd4")
        self.gridLayout_3.addWidget(self.editCmd4, 3, 1, 1, 1)
        self.btnSendCmd5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSendCmd5.setObjectName("btnSendCmd5")
        self.gridLayout_3.addWidget(self.btnSendCmd5, 4, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 3, 0, 1, 1)
        self.btnSendCmd2.setMinimumSize(QtCore.QSize(0, 0))
        self.btnSendCmd2.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSendCmd2.setObjectName("btnSendCmd2")
        self.gridLayout_3.addWidget(self.btnSendCmd2, 1, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 4, 0, 1, 1)
        self.btnSendCmd3.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSendCmd3.setObjectName("btnSendCmd3")
        self.gridLayout_3.addWidget(self.btnSendCmd3, 2, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 6, 0, 1, 1)
        self.editCmd1.setClearButtonEnabled(True)
        self.editCmd1.setObjectName("editCmd1")
        self.gridLayout_3.addWidget(self.editCmd1, 0, 1, 1, 1)
        self.editCmd2.setClearButtonEnabled(True)
        self.editCmd2.setObjectName("editCmd2")
        self.gridLayout_3.addWidget(self.editCmd2, 1, 1, 1, 1)
        self.btnSendCmd10.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnSendCmd10.setObjectName("btnSendCmd10")
        self.gridLayout_3.addWidget(self.btnSendCmd10, 9, 2, 1, 1)
        self.editCmd10.setClearButtonEnabled(True)
        self.editCmd10.setObjectName("editCmd10")
        self.gridLayout_3.addWidget(self.editCmd10, 9, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 10, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.sendGrid = QtWidgets.QGridLayout()
        self.sendGrid.setObjectName("sendGrid")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkStringSend.sizePolicy().hasHeightForWidth())
        self.checkStringSend.setSizePolicy(sizePolicy)
        self.checkStringSend.setObjectName("checkStringSend")
        self.sendGrid.addWidget(self.checkStringSend, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.sendGrid.addItem(spacerItem1, 3, 1, 1, 1)
        self.editSendData.setTabChangesFocus(True)
        self.editSendData.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editSendData.sizePolicy().hasHeightForWidth())
        self.editSendData.setSizePolicy(sizePolicy)
        self.editSendData.setOverwriteMode(False)
        self.editSendData.setAcceptRichText(False)
        self.editSendData.setObjectName("editSendData")
        self.sendGrid.addWidget(self.editSendData, 2, 0, 1, 4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnSend.sizePolicy().hasHeightForWidth())
        self.btnSend.setSizePolicy(sizePolicy)
        self.btnSend.setObjectName("btnSend")
        self.sendGrid.addWidget(self.btnSend, 3, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.sendArea)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editInterval.sizePolicy().hasHeightForWidth())
        self.editInterval.setSizePolicy(sizePolicy)
        self.editInterval.setMaximumSize(QtCore.QSize(70, 16777215))
        self.editInterval.setSizeIncrement(QtCore.QSize(0, 0))
        self.editInterval.setBaseSize(QtCore.QSize(0, 0))
        self.editInterval.setMaxLength(10)
        self.editInterval.setClearButtonEnabled(False)
        self.editInterval.setObjectName("editInterval")
        self.horizontalLayout.addWidget(self.editInterval)
        self.label_5 = QtWidgets.QLabel(self.sendArea)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnAutoSend.sizePolicy().hasHeightForWidth())
        self.btnAutoSend.setSizePolicy(sizePolicy)
        self.btnAutoSend.setObjectName("btnAutoSend")
        self.horizontalLayout.addWidget(self.btnAutoSend)
        self.sendGrid.addLayout(self.horizontalLayout, 0, 0, 1, 4)
        self.verticalLayout_2.addLayout(self.sendGrid)
        self.gridLayout.addWidget(self.sendArea, 0, 2, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkStringReceive = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkStringReceive.sizePolicy().hasHeightForWidth())
        self.checkStringReceive.setSizePolicy(sizePolicy)
        self.checkStringReceive.setObjectName("checkStringReceive")
        self.gridLayout_2.addWidget(self.checkStringReceive, 1, 5, 1, 1)
        self.btnClearReceive = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnClearReceive.sizePolicy().hasHeightForWidth())
        self.btnClearReceive.setSizePolicy(sizePolicy)
        self.btnClearReceive.setObjectName("btnClearReceive")
        self.gridLayout_2.addWidget(self.btnClearReceive, 1, 6, 1, 1)
        self.editReceiveData = QtWidgets.QTextEdit(self.groupBox)
        self.editReceiveData.setReadOnly(True)
        self.editReceiveData.setObjectName("editReceiveData")
        self.gridLayout_2.addWidget(self.editReceiveData, 0, 0, 1, 7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 4, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.gridLayout_2.addWidget(self.label_17, 1, 0, 1, 1)
        self.receivedLength = QtWidgets.QLabel(self.groupBox)
        self.receivedLength.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.receivedLength.sizePolicy().hasHeightForWidth())
        self.receivedLength.setSizePolicy(sizePolicy)
        self.receivedLength.setText("")
        self.receivedLength.setAlignment(QtCore.Qt.AlignCenter)
        self.receivedLength.setObjectName("receivedLength")
        self.gridLayout_2.addWidget(self.receivedLength, 1, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 1, 2, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_4.setSpacing(12)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.btnOpenClose = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnOpenClose.sizePolicy().hasHeightForWidth())
        self.btnOpenClose.setSizePolicy(sizePolicy)
        self.btnOpenClose.setObjectName("btnOpenClose")
        self.gridLayout_4.addWidget(self.btnOpenClose, 0, 5, 1, 2)
        self.btnScanPort = QtWidgets.QPushButton(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnScanPort.sizePolicy().hasHeightForWidth())
        self.btnScanPort.setSizePolicy(sizePolicy)
        self.btnScanPort.setObjectName("btnScanPort")
        self.gridLayout_4.addWidget(self.btnScanPort, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem4, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 3, 1, 1)
        self.selectPort = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectPort.sizePolicy().hasHeightForWidth())
        self.selectPort.setSizePolicy(sizePolicy)
        self.selectPort.setObjectName("selectPort")
        self.gridLayout_4.addWidget(self.selectPort, 0, 2, 1, 1)
        self.selectByteSize = QtWidgets.QComboBox(self.groupBox_3)
        self.selectByteSize.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectByteSize.sizePolicy().hasHeightForWidth())
        self.selectByteSize.setSizePolicy(sizePolicy)
        self.selectByteSize.setObjectName("selectByteSize")
        self.gridLayout_4.addWidget(self.selectByteSize, 1, 2, 1, 1)
        self.selectParity = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectParity.sizePolicy().hasHeightForWidth())
        self.selectParity.setSizePolicy(sizePolicy)
        self.selectParity.setObjectName("selectParity")
        self.gridLayout_4.addWidget(self.selectParity, 1, 4, 1, 1)
        self.selectStopBits = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectStopBits.sizePolicy().hasHeightForWidth())
        self.selectStopBits.setSizePolicy(sizePolicy)
        self.selectStopBits.setObjectName("selectStopBits")
        self.gridLayout_4.addWidget(self.selectStopBits, 1, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 1, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 0, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 5, 1, 1)
        self.selectBaudrate = QtWidgets.QComboBox(self.groupBox_3)
        self.selectBaudrate.setObjectName("selectBaudrate")
        self.gridLayout_4.addWidget(self.selectBaudrate, 0, 4, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 1, 7, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_3)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "串口调试工具 — Dennic"))
        self.sendArea.setTitle(_translate("MainWindow", "数据发送区"))
        self.groupBox_2.setTitle(_translate("MainWindow", "十六进制命令"))
        self.btnSendCmd8.setText(_translate("MainWindow", "发送"))
        self.label_13.setText(_translate("MainWindow", "9:"))
        self.btnSendCmd9.setText(_translate("MainWindow", "发送"))
        self.label_12.setText(_translate("MainWindow", "8:"))
        self.label_14.setText(_translate("MainWindow", "10:"))
        self.btnSendCmd7.setText(_translate("MainWindow", "发送"))
        self.btnSendCmd1.setText(_translate("MainWindow", "发送"))
        self.label_6.setText(_translate("MainWindow", "2:"))
        self.label_10.setText(_translate("MainWindow", "6:"))
        self.btnSendCmd6.setText(_translate("MainWindow", "发送"))
        self.cmd1.setText(_translate("MainWindow", "1:"))
        self.btnSendCmd4.setText(_translate("MainWindow", "发送"))
        self.btnSendCmd5.setText(_translate("MainWindow", "发送"))
        self.label_7.setText(_translate("MainWindow", "3:"))
        self.label_8.setText(_translate("MainWindow", "4:"))
        self.btnSendCmd2.setText(_translate("MainWindow", "发送"))
        self.label_9.setText(_translate("MainWindow", "5:"))
        self.btnSendCmd3.setText(_translate("MainWindow", "发送"))
        self.label_11.setText(_translate("MainWindow", "7:"))
        self.btnSendCmd10.setText(_translate("MainWindow", "发送"))
        self.checkStringSend.setText(_translate("MainWindow", "字符串编码发送"))
        self.btnSend.setText(_translate("MainWindow", "发送"))
        self.label_4.setText(_translate("MainWindow", "自动发送周期"))
        self.editInterval.setText(_translate("MainWindow", "2000"))
        self.label_5.setText(_translate("MainWindow", "秒"))
        self.btnAutoSend.setText(_translate("MainWindow", "开始自动发送"))
        self.groupBox.setTitle(_translate("MainWindow", "数据接收区"))
        self.checkStringReceive.setText(_translate("MainWindow", "字符串解码显示"))
        self.btnClearReceive.setText(_translate("MainWindow", "清空接收缓冲区"))
        self.label_17.setText(_translate("MainWindow", "已接收:"))
        self.label_19.setText(_translate("MainWindow", "字节"))
        self.groupBox_3.setTitle(_translate("MainWindow", "打开/关闭串口"))
        self.btnOpenClose.setText(_translate("MainWindow", "打开串口"))
        self.btnScanPort.setText(_translate("MainWindow", "扫描可用串口"))
        self.label_2.setText(_translate("MainWindow", "校验位:"))
        self.label.setText(_translate("MainWindow", "数据位:"))
        self.label_16.setText(_translate("MainWindow", "波特率:"))
        self.label_3.setText(_translate("MainWindow", "停止位:"))
        self.receivedLength.setText(_translate("MainWindow", "0"))
