import time
from PyQt5 import QtCore
import queue

class SendThread(QtCore.QThread):
    # 自动发送的信号槽
    autoSendError = QtCore.pyqtSignal(str)
    # 发生错误的信号槽
    error = QtCore.pyqtSignal(str)

    __flag = False
    __isAutoSend = False

    def __init__(self, spCore, serialPort, parent=None):
        super(SendThread, self).__init__(parent)
        self.__spCore = spCore
        self.__serialPort = serialPort
        self.__sendQueue = queue.Queue()

    def stop(self):
        self.__flag = False

    # 设置是否以字符串发送
    def setSendString(self, e):
        self.__isSendString = e

    # 开始自动发送
    def startAutoSend(self, data, interval):
        self.__autoSendData = data
        self.__autoSendInterval = interval
        self.__isAutoSend = True
    # 停止自动发送
    def stopAutoSend(self):
        self.__isAutoSend = False

    # 获取自动发送状态
    def isAutoSend(self):
        return self.__isAutoSend

    # 发送数据， 添加到发送队列
    def sendData(self, data):
        try:
            if not self.__serialPort.isOpen():
                return False, "串口未打开！"
            if self.__isSendString:
                dataBytes = data.encode("gb2312")
            else:
                dataBytes = self.__spCore.hexStringToByteArray(data)
                if not dataBytes:
                    return False, "请正确输入HEX格式数据，如“FF C0 A3”。"
            self.__sendQueue.put(dataBytes)
            return True, "发送成功！"
        except:
            return False, "发送失败！"

    def sendCmd(self, data):
        try:
            if not self.__serialPort.isOpen():
                return False, "串口未打开！"
            dataBytes = self.__spCore.hexStringToByteArray(data)
            if not dataBytes:
                return False, "请正确输入HEX格式数据，如“FF C0 A3”。"
            self.__sendQueue.put(dataBytes)
            return True, "发送成功！"
        except:
            return False, "发送失败！"

    def run(self):
        self.__flag = True
        lastSendTime = 0
        while self.__flag:

            # 自动发送
            if self.__isAutoSend:
                nowTime = time.time()*1000
                if nowTime - lastSendTime >= self.__autoSendInterval:
                    lastSendTime = nowTime
                    success, msg = self.sendData(self.__autoSendData)
                    if not success:
                        self.stopAutoSend()
                        self.autoSendError.emit(msg)

            if self.__serialPort.isOpen():
                if not self.__sendQueue.empty():
                    try:
                        self.__serialPort.write(self.__sendQueue.get())
                    except:
                        pass
                time.sleep(0.001)
            else:
                time.sleep(0.5)
