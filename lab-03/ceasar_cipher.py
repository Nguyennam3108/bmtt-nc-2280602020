import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QMessageBox
from ui.ceasar import Ui_MainWindow
import requests

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui =Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.call_api_encrypt)
        self.ui.pushButton_2.clicked.connect(self.call_api_dencrypt)

    def call_api_encrypt(self):
        url="http://127.0.0.1:5000/api/ceasar/encrypt"   
        payload = {
            "plant_text":self.ui.textEdit.toPlainText(),
            "key":self.ui.textEdit_2.toPlainText(),
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit_3.setPlainText(data["encrypted_message"])

                msg=QMessageBox()
                msg=setIcon(QMessageBox.Information)
                msg.setText("Encrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" %e.message)
    def call_api_dencrypt(self):
        url = "http://127.0.0.1:5000.api/ceasar/decrypt"
        payload ={
            "cipher_text": self.ui.textEdit_3.toPlainText(),
            "key": self.ui.textEdit_2()
        }
        try:
            response = requests.post(url,json=payload)
            if response.status_code == 200:
                data = response.json()
                self.ui.textEdit.setText(data["decrypted_message"])


                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Decrypted Successfully")
                msg.exec_()
            else:
                print("Error while calling API")
        except requests.exceptions.RequestException as e:
            print("Error: %s" % e.message)

if __name__ =="__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())   