import time
from PyQt5 import QtCore

class ReceiveThread(QtCore.QThread):
    # 接收到数据的信号槽
    received = QtCore.pyqtSignal(str)
    # 发生错误的信号槽
    error = QtCore.pyqtSignal(str)

    __flag = False

    def __init__(self, spCore, serialPort, parent=None):
        super(ReceiveThread, self).__init__(parent)
        self.__spCore = spCore
        self.__serialPort = serialPort
        self.__dataBuffer = b""

    def stop(self):
        self.__flag = False

    # 设置是否以字符串接收
    def setReceiveString(self, e):
        self.__isReceiveString = e
        data = self.__decodeData(self.__dataBuffer)
        self.received.emit(data)

    # 获取接收缓冲区长度
    def getReceivedLength(self):
        return len(bytes(self.__dataBuffer))

    # 清空接收缓冲区
    def clearReceiveBuffer(self):
        self.__dataBuffer = b""
        data = self.__decodeData(self.__dataBuffer)
        self.received.emit(data)

    def __decodeData(self, rawData):
        data = ""
        if self.__isReceiveString:
            # 尝试以 gbk编码集 解码，如果失败再用 iso-8859-1编码集 解码
            try:
                data = rawData.decode("gbk")
            except UnicodeDecodeError:
                data = rawData.decode("iso-8859-1")
        else:
            data = self.__spCore.dataArrayToString([self.__spCore.byteToHexString(x) for x in bytes(rawData)])
        return data

    def run(self):
        self.__flag = True
        while self.__flag:
            if self.__serialPort.isOpen():
                try:
                    if self.__serialPort.inWaiting() > 0:
                        rawData = self.__serialPort.read(self.__serialPort.inWaiting())
                        self.__dataBuffer += rawData
                        data = self.__decodeData(self.__dataBuffer)
                        self.received.emit(data)
                except:
                    pass
                time.sleep(0.001)
            else:
                time.sleep(0.5)
