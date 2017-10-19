# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from AppUi import Ui_MainWindow

class ViewController(object):

    def __init__(self, window):
        self.__window = window
        self.__ui = Ui_MainWindow()
        self.__ui.setupUi(window)
        self.__ui.editSendData.setFocus()

    # 初始化串口选项内容列表
    def initComboBox(self, serialPort):
        self.__ui.selectPort.addItems(serialPort.getAvailablePortNames())
        self.__ui.selectBaudrate.addItems(serialPort.getBaudrateNames())
        self.__ui.selectByteSize.addItems(serialPort.getByteSizeNames())
        self.__ui.selectStopBits.addItems(serialPort.getStopBitsNames())
        self.__ui.selectParity.addItems(serialPort.getParityNames())
        self.initSelections()

    # 更新可用串口选项列表
    def refreshAvailablePort(self, ports):
        self.__ui.selectPort.clear()
        self.__ui.selectPort.addItems(ports)
        self.__ui.selectPort.update()


    # 初始化串口选项
    def initSelections(self):
        self.__ui.selectPort.setCurrentIndex(0)
        self.__ui.selectBaudrate.setCurrentIndex(4)
        self.__ui.selectParity.setCurrentIndex(2)
        self.__ui.selectByteSize.setCurrentIndex(3)
        self.__ui.selectStopBits.setCurrentIndex(0)

    # 事件绑定
    def bindEvents(self, handler):
        self.__ui.editSendData.textChanged.connect(handler.inputSendData)
        self.__ui.btnOpenClose.clicked.connect(handler.clickOpenClose)
        self.__ui.selectPort.currentIndexChanged.connect(handler.selectPort)
        self.__ui.selectBaudrate.currentIndexChanged.connect(handler.selectBaudrate)
        self.__ui.selectParity.currentIndexChanged.connect(handler.selectParity)
        self.__ui.selectByteSize.currentIndexChanged.connect(handler.selectByteSize)
        self.__ui.selectStopBits.currentIndexChanged.connect(handler.selectStopBits)
        self.__ui.checkStringSend.stateChanged.connect(handler.checkStringSend)
        self.__ui.checkStringReceive.stateChanged.connect(handler.checkStringReceive)
        self.__ui.btnClearReceive.clicked.connect(handler.clickClearReceive)
        self.__ui.btnSend.clicked.connect(handler.clickSend)
        self.__ui.btnAutoSend.clicked.connect(handler.clickAutoSend)
        self.__ui.btnScanPort.clicked.connect(handler.clickScanPort)

        self.__ui.editCmd1.returnPressed.connect(lambda: handler.clickSendCmd(1))
        self.__ui.editCmd2.returnPressed.connect(lambda: handler.clickSendCmd(2))
        self.__ui.editCmd3.returnPressed.connect(lambda: handler.clickSendCmd(3))
        self.__ui.editCmd4.returnPressed.connect(lambda: handler.clickSendCmd(4))
        self.__ui.editCmd5.returnPressed.connect(lambda: handler.clickSendCmd(5))
        self.__ui.editCmd6.returnPressed.connect(lambda: handler.clickSendCmd(6))
        self.__ui.editCmd7.returnPressed.connect(lambda: handler.clickSendCmd(7))
        self.__ui.editCmd8.returnPressed.connect(lambda: handler.clickSendCmd(8))
        self.__ui.editCmd9.returnPressed.connect(lambda: handler.clickSendCmd(9))
        self.__ui.editCmd10.returnPressed.connect(lambda: handler.clickSendCmd(10))
        self.__ui.btnSendCmd1.clicked.connect(lambda: handler.clickSendCmd(1))
        self.__ui.btnSendCmd2.clicked.connect(lambda: handler.clickSendCmd(2))
        self.__ui.btnSendCmd3.clicked.connect(lambda: handler.clickSendCmd(3))
        self.__ui.btnSendCmd4.clicked.connect(lambda: handler.clickSendCmd(4))
        self.__ui.btnSendCmd5.clicked.connect(lambda: handler.clickSendCmd(5))
        self.__ui.btnSendCmd6.clicked.connect(lambda: handler.clickSendCmd(6))
        self.__ui.btnSendCmd7.clicked.connect(lambda: handler.clickSendCmd(7))
        self.__ui.btnSendCmd8.clicked.connect(lambda: handler.clickSendCmd(8))
        self.__ui.btnSendCmd9.clicked.connect(lambda: handler.clickSendCmd(9))
        self.__ui.btnSendCmd10.clicked.connect(lambda: handler.clickSendCmd(10))

    # 更新串口打开/关闭状态
    def openOrCloseSerialPort(self, e):
        self.__ui.btnOpenClose.setText("打开串口" if not e else "关闭串口")

    # 更新串口打开/关闭状态
    def startOrEndAutoSend(self, e):
        self.__ui.btnAutoSend.setText("开始自动发送" if not e else "停止自动发送")
        self.__ui.editSendData.setEnabled(not e)
        self.__ui.editInterval.setEnabled(not e)

    # 根据 objectName 设置 QComboBox 当前选择项
    def setSelectedIndex(self, objectName, i):
        return self.__window.findChild(QtWidgets.QComboBox, objectName).setCurrentIndex(i)
    # 根据 objectName 设置 QComboBox 当前选择内容
    def setSelectedText(self, objectName, t):
        return self.__window.findChild(QtWidgets.QComboBox, objectName).setCurrentText(t)
    # 根据 objectName 获取 QComboBox 当前选择项
    def getSelectedIndex(self, objectName):
        return self.__window.findChild(QtWidgets.QComboBox, objectName).currentIndex()
    # 根据 objectName 获取 QComboBox 当前选择内容
    def getSelectedText(self, objectName):
        return self.__window.findChild(QtWidgets.QComboBox, objectName).currentText()

    # 根据 objectName 获取 QCheckBox 当前状态
    def getCheckedStatus(self, objectName):
        return self.__window.findChild(QtWidgets.QCheckBox, objectName).isChecked()

    # 获取和设置接收数据内容
    def getReceivedText(self):
        return self.__window.findChild(QtWidgets.QTextEdit, "editReceiveData").toPlainText()
    def setReceivedText(self, text):
        self.__window.findChild(QtWidgets.QTextEdit, "editReceiveData").setPlainText(text)
        self.__window.findChild(QtWidgets.QTextEdit, "editReceiveData").moveCursor(QtGui.QTextCursor.End)
    # 清空接收数据
    def clearReceivedData(self):
        self.__window.findChild(QtWidgets.QTextEdit, "editReceiveData").setText("")

    def setReceivedLength(self, l):
        self.__window.findChild(QtWidgets.QLabel, "receivedLength").setText(str(l))

    # 获取和设置发送数据内容
    def getSendText(self):
        return self.__window.findChild(QtWidgets.QTextEdit, "editSendData").toPlainText()
    def setSendText(self, text):
        self.__window.findChild(QtWidgets.QTextEdit, "editSendData").setPlainText(text)
    # 获取和设置发送数据内容光标
    def getSendTextCursor(self):
        return self.__window.findChild(QtWidgets.QTextEdit, "editSendData").textCursor()
    def setSendTextCursor(self, cursor):
        self.__window.findChild(QtWidgets.QTextEdit, "editSendData").setTextCursor(cursor)

    # 获取十六进制命令数据内容
    def getCmdText(self, i):
        return self.__window.findChild(QtWidgets.QLineEdit, "editCmd" + str(i)).text()

    # 获取自动发送间隔内容
    def getAutoSendInterval(self):
        return self.__window.findChild(QtWidgets.QLineEdit, "editInterval").text()
