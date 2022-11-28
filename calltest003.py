import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QHBoxLayout, QPushButton
class closeApp(QMainWindow):
    def __init__(self):
        super(closeApp, self).__init__()
        self.resize(400, 300)
        self.setWindowTitle('退出应用程序')
        self.button1=QPushButton('退出')
        self.button1.clicked.connect(self.onButtonClick)
        self.layout=QHBoxLayout()
        self.layout.addWidget(self.button1)
        frame=QWidget()
        frame.setLayout(self.layout)   
        self.setCentralWidget(frame) 
    def onButtonClick(self):
        sender=self.sender()
        print(sender.text()+'按钮被按下')
        qApp=QApplication.instance()
        qApp.quit()

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin =closeApp()
    myWin.show()
    sys.exit(app.exec_())
