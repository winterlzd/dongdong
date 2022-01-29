# encoding:utf-8
from Ui_aimain import Ui_MainWindow
from Ui_ai2 import Ui_about
from PyQt5 import QtCore, QtGui, QtWidgets
import sys, requests, json, webbrowser
class window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(window,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)
    def getinput(self):
        str = self.textEdit.toPlainText()
        return str
    def printf(self, mes):
            self.textBrowser.append(mes)  # 在指定的区域显示提示信息
            self.cursot = self.textBrowser.textCursor()
            self.textBrowser.moveCursor(self.cursot.End)
            QtWidgets.QApplication.processEvents()
    def website(self):
        webbrowser.open_new("http://47.108.139.27:2022")
    def help(self):
        webbrowser.open_new("http://47.108.139.27:2022/home/help.php")
    def donate(self):
        webbrowser.open_new("http://47.108.139.27:2022/home/don.php")
    def clickButton(self):
        window.printf(w, "You: " + window.getinput(w))
        header = {
            'user-agent': 'Mozilla/5.0 (Linux 15.0; Linux64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 zhenbei/1.0'
                }
        response = requests.post("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + str(window.getinput(w)), headers=header)
        response.encoding = 'utf-8'
        if response:
            text_json = json.loads(response.text)
            context = "%s"%text_json['content']
            window.printf(w, "DongDong: " + context)
class aboutwindow(QtWidgets.QMainWindow, Ui_about):
    def __init__(self):
        super(aboutwindow,self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w2 = aboutwindow()
    w = window()
    w.show()
    #w.menubar = QtWidgets.QMenuBar(Ui_MainWindow)
    w.send_button.clicked.connect(w.clickButton)
    w.action.triggered.connect(w.close)
    w.action_2.triggered.connect(w.website)
    w.action_3.triggered.connect(w.help)
    w.action_6.triggered.connect(w.donate)
    w.action_4.triggered.connect(w2.show)
    sys.exit(app.exec_())