# -*- coding: utf-8 -*-

import serial
from SerialPort import SPOptions, SPSendThread, SPReceiveThread

class SerialPort(object):
    # __port = 'com1'
    # __baudrate = 9600
    # __parity=serial.PARITY_NONE
    # __stopbits=serial.STOPBITS_ONE
    # __bytesize=serial.EIGHTBITS

    # 是否以字符串发送/接收数据
    __sendString = False
    __receiveString = False

    def __init__(self):
        # 实例化串口类
        self.__serialPort = serial.Serial()
        # 实例化并启动发送/接收线程
        self.sendThread = SPSendThread.SendThread(self, self.__serialPort)
        self.receiveThread = SPReceiveThread.ReceiveThread(self, self.__serialPort)
        self.sendThread.setSendString(self.__sendString)
        self.receiveThread.setReceiveString(self.__receiveString)
        self.sendThread.start()
        self.receiveThread.start()

    # 打开串口
    def open(self):
        if self.isOpen():
            self.close()
        try:
            # print(self.__serialPort.port)
            # print(self.__serialPort.baudrate)
            # print(self.__serialPort.bytesize)
            # print(self.__serialPort.parity)
            # print(self.__serialPort.stopbits)
            self.__serialPort.open()
            return True, "串口打开成功！"
        except Exception as e:
            msg = "无法打开串口！"
            if str(e).find("PermissionError") >= 0:
                msg = "串口 {!r} 已被占用！".format(str(self.__serialPort.port).upper())
            return False , msg

    # 关闭串口
    def close(self):
        if self.isOpen():
            try:
                self.__serialPort.close()
                return True
            except:
                pass
        return False

    # 返回串口打开/关闭状态
    def isOpen(self):
        return self.__serialPort.isOpen()

    # 设置串口
    def setPort(self, port):
        try:
            self.__serialPort.port = port
            return True, "串口打开成功！"
        except Exception as e:
            msg = "串口打开失败！"
            if str(e).find("PermissionError") >= 0:
                msg = "串口 {!r} 已被占用！".format(str(self.__serialPort.port).upper())
            return False, msg

    # 获取当前串口
    def getPort(self):
        return self.__serialPort.port

    # 设置波特率
    def setBaudrate(self, b):
        self.__serialPort.baudrate = b

    # 设置校验位
    def setParity(self, p):
        self.__serialPort.parity = p

    # 设置数据位
    def setByteSize(self, b):
        self.__serialPort.bytesize = b

    # 设置停止位
    def setStopBits(self, s):
        self.__serialPort.stopbits = s

    # 设置发送字符串数据
    def setSendString(self,e):
        self.__sendString = e
        self.sendThread.setSendString(e)

    # 设置接收字符串数据
    def setReceiveString(self,e):
        self.__receiveString = e
        self.receiveThread.setReceiveString(e)

    # 获取可选 COM 口名称
    def getAvailablePortNames(self):
        result = []
        coms = ['COM%s' % i for i in range(1,257)]
        for port in coms:
            try:
                s = serial.Serial(port)
                s.close()
                result.append(port)
            except serial.SerialException as e:
                if str(e).find("PermissionError") >= 0:
                    result.append(port)
        if len(result) == 0:
            result.append("(无可用)")
        return result

    # 获取可选波特率名称
    def getBaudrateNames(self):
        return SPOptions.Baudrate.BAUDRATES

    # 获取可选校验位名称
    def getParityNames(self):
        return SPOptions.Parity.PARITY_NAMES

    # 获取可选数据位名称
    def getByteSizeNames(self):
        return SPOptions.ByteSize.BYTESIZE_NAMES

    # 获取可选停止位名称
    def getStopBitsNames(self):
        return SPOptions.StopBits.STOPBITS_NAMES



    # 数据数组转可读字符串
    def dataArrayToString(self,l):
    	s = ""
    	for i in l:
    		s += (str(i)+" ")
    	return s

    # 字节转十六进制字符串
    def byteToHexString(self,b):
    	h = hex(b)
    	h = h.replace("0x","")
    	if len(h) == 1:
    		h = "0" + h
    	return h.upper()

    # 十六进制字符串转字节数组
    def hexStringToByteArray(self, s):
        try:
            data = s.split()
            hexData = []
            for b in data:
                hexData.append(int(b,16))
            dataBytes =  bytes(hexData)
            return dataBytes
        except:
            return None
