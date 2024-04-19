import sys
import PyQt5.QtWidgets as qw
from PyQt5.QtCore import QThread, pyqtSignal, QObject
import threading
from time import sleep
from PyQt5.QtSerialPort import QSerialPort


class Serial_Qthread_function(QObject):
    # 多线程用到的信号
    signal_Serialstart_function = pyqtSignal()  # 接受串口线程开启信号
    signal_push_open_serial_button = pyqtSignal(object)     # 接受按下开启串口按钮信号
    signal_serial_button_pushed = pyqtSignal(object)     # 串口按钮处于打开状态的信号
    signal_update_textbrowser = pyqtSignal(object)

    # 初始化函数
    def __init__(self, parent=None):
        super(Serial_Qthread_function, self).__init__(parent)
        self.state = 0  # 定义串口状态，0表示关闭，1表示打开，2表示错误

    def slot_push_open_serial_button(self, parameter):
        if self.state == 0:
            print(parameter)
            self.Serial.setPortName(parameter['comboBox_port'])
            self.Serial.setBaudRate(parameter['comboBox_baudrate'])
            self.Serial.setStopBits(parameter['comboBox_stopbits'])
            self.Serial.setDataBits(parameter['comboBox_databits'])
            self.Serial.setParity(parameter['comboBox_parity'])

            if self.Serial.open(QSerialPort.ReadWrite):
                print("串口打开成功")
                print("Baud rate:", self.Serial.baudRate)
                print("Data bits:", self.Serial.dataBits())
                print("Parity:", self.Serial.parity())
                print("Stop bits:", self.Serial.stopBits())
                print("Flow control:", self.Serial.flowControl())
                self.state = 1
                self.signal_serial_button_pushed.emit(self.state)  # 发送 按钮处于按下状态 信号
            else:
                print("串口打开失败")
                self.signal_serial_button_pushed.emit(self.state)
        else:
            self.state = 0
            self.Serial.close()
            self.signal_serial_button_pushed.emit(self.state)

    def Serial_receive_data(self):
        data = self.Serial.readAll()
    #    data_str = bytes(data).decode('Latin-1').strip()
        self.signal_update_textbrowser.emit(data)

    def Serial_Init_function(self):
        print("串口线程id", threading.current_thread().ident)
        self.Serial = QSerialPort()  # 创建一个串口实例
        self.Serial.readyRead.connect(self.Serial_receive_data)  # 数据准备就绪后，连接到串口接受函数

