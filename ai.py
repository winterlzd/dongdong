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
        if w.radioButton_2.isChecked() == True:
            header = {
                'user-agent': 'Mozilla/5.0 (Linux 15.0; Linux64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 zhenbei/1.0'
                    }
            response = requests.post("http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + str(window.getinput(w)), headers=header)
            response.encoding = 'utf-8'
            if response:
                text_json = json.loads(response.text)
                context = "%s"%text_json['content']
                window.printf(w, "DongDong: " + context)
        elif w.radioButton.isChecked() == True:
            baidu_server = 'https://aip.baidubce.com/oauth/2.0/token?'  #获取token的server
            grant_type = 'client_credentials'
            client_id = 'lRxQBBuyQDt2dvirlwF3tvzO' #API KEY
            client_secret = 'KPxi6W4XbyYAQRdEIBG2I1cGXuGIWEU9' #Secret KEY   
            #合成请求token的url
            url = baidu_server+'grant_type='+grant_type+'&client_id='+client_id+'&client_secret='+client_secret

            #获取token
            res = requests.get(url).text
            data = json.loads(res)  #将json格式转换为字典格式
            token = data['access_token']

            access_token = token

            url = 'https://aip.baidubce.com/rpc/2.0/unit/service/v3/chat?access_token=' + access_token
            said = str(window.getinput(w))
            said.encode('utf-8')
            post_data = "{\"version\":\"3.0\",\"service_id\":\"S64708\",\"session_id\":\"\",\"log_id\":\"7758521\",\"skill_id\":\"1137807\",\"request\":{\"terminal_id\":\"88888\",\"query\":\"" + said + "\"}}"
            post_data.encode('utf-8')
            print('post_data:',post_data)
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            response = requests.post(url, data=post_data.encode('utf-8'), headers=headers)
            response.encoding = 'utf-8'
            if response:
                #print (response.json())
                text_json = json.loads(response.text)
                context = "%s"%text_json['result']['context']['SYS_PRESUMED_HIST'][1]
                window.printf(w, "DongDong: "+ context)

    
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