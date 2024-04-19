import sys
# 导入pyqt相关库
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QThread, QTimer
from PyQt5.QtWidgets import QApplication, QWidget
# 导入re库
import re
# 调用pyrt5生成的.ui文件转换得到的.py文件
import form
# 调用获取串口的库
import serial.tools.list_ports
# 调用线程相关的库
import threading
# 调用串口线程
from serial_thread import Serial_Qthread_function
from PyQt5.QtSerialPort import QSerialPortInfo


class MyMainWindow(QtWidgets.QMainWindow, form.Ui_MainWindow):
    def __init__(self) -> None:
        super(MyMainWindow, self).__init__()  # 初始化父类
        self.set_parameter = {}
        self.setupUi(self)                    # 调用Ui_MainWindow生成UI
        print("主线程id", threading.current_thread().ident)
        self.Ui_Init()                        # 连接按钮和对应函数
        # 主线程改变UI，串口数据的收发运行在新的线程里
        self.Serial_QThread = QtCore.QThread()  # 定义一个线程以供数据用，不影响UI更新
        self.Serial_Qthread_function = Serial_Qthread_function()
        self.Serial_Qthread_function.moveToThread(self.Serial_QThread)
        self.Serial_QThread.start()     # 开启新线程以传输串口数据
        self.Serial_Qthread_function.signal_Serialstart_function.connect(self.Serial_Qthread_function.Serial_Init_function)     #线程开启信号连接到串口初始化函数
        self.Serial_Qthread_function.signal_Serialstart_function.emit()     # 实例化w时，发送线程开启信号
        self.Serial_Qthread_function.signal_push_open_serial_button.connect(self.Serial_Qthread_function.slot_push_open_serial_button)  # 信号发送到槽函数slot中
        self.Serial_Qthread_function.signal_serial_button_pushed.connect(self.slot_signal_serial_button_pushed)  # 打开串口按钮处于按下状态信号
        self.Serial_Qthread_function.signal_update_textbrowser.connect(self.slot_update_textbrowser)
        self.search_COM()
        # 创建一个定时器，定时扫面串口
        #self.time_scan = QTimer()
        #self.time_scan.timeout.connect(self.search_COM)
        #self.time_scan.start(1000)

    def search_COM(self):                     # 搜索串口函数
        self.comboBox_port.clear()            # 清空port端口的下拉菜单
        port_list = list(serial.tools.list_ports.comports())    # 获取可用端口号，写在port_list列表中
        com_numbers = len(port_list)          # 可用端口个数
        #  定义了正则表达式[(](.* ?)[)]，提取方括号中的内容。re.S标志表示.可以匹配包括换行符在内的任意字符。
        p1 = re.compile(r'[(](.*?)[)]', re.S)
        for i in range(com_numbers):
            com_list = str(port_list[i])      # 将端口号转换为字符串形式
            com_name = re.findall(p1, com_list)  # 使用正则表达式p1提取com_list的所有符合p1的内容
            com_name = str(com_name)          # 匹配到的内容转换为字符串
            str_list = com_name.split("'")     # 根据单引号对com_name中的字符串进行分割
            self.comboBox_port.addItem(str_list[1])  # 添加strlist的第二项到port口的下拉菜单中

    def Ui_Init(self):
        self.open_serial_button.clicked.connect(self.open_serial)  # 按下“打开串口”按钮，执行对应函数
        self.clear_text_button.clicked.connect(self.clear_text)
        self.search_com_button.clicked.connect(self.search_COM)

    def open_serial(self):
        self.set_parameter['comboBox_port'] = self.comboBox_port.currentText()  # 发送串口号
        self.set_parameter['comboBox_baudrate'] = 256000
        self.set_parameter['comboBox_stopbits'] = 1
        self.set_parameter['comboBox_databits'] = 8
        self.set_parameter['comboBox_parity'] = 0
        # 此处可添加其他参数设置
        self.Serial_Qthread_function.signal_push_open_serial_button.emit(self.set_parameter)  # 发送“按下打开串口”的信号

    def clear_text(self):                     # 清空串口接受栏
        # self.textEdit.clear()
        self.textBrowser.clear()

    def slot_signal_serial_button_pushed(self, state):
        if state == 1:
            self.open_serial_button.setText("关闭串口")
        else:
            self.open_serial_button.setText("打开串口")

    def slot_update_textbrowser(self, data):
        Byte_data = bytes(data)
        view_data = ''
        for i in range(0, len(Byte_data)):
            view_data = view_data + '{:02x}'.format(Byte_data[i]) + ''
        self.textBrowser.insertPlainText(view_data)
        self.textBrowser.insertPlainText('\n')  # 换行
        # 滚动至最下方显示数据
        cursor = self.textBrowser.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        self.textBrowser.setTextCursor(cursor)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyMainWindow()
    w.show()
    app.exec_()



