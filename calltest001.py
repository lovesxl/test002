import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
#from PyQt5.QtWidgets import QApplication,QMainwindow
from PyQt5.QtGui import QIcon
class mw(QMainWindow):
    def __init__(self):
        super(mw, self).__init__()
        self.setWindowTitle('主窗口')
        self.resize(400, 200)
        self.status=self.statusBar()
        self.status.showMessage('消息', 5000)
if __name__=='__main__':
    app=QApplication(sys.argv)
    app.setWindowIcon(QIcon('.\images\哆啦A梦.ico'))
    main=mw()
    main.show()
    print("faefda")
    sys.exit(app.exec_())
