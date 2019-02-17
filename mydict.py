# coding:utf-8
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QMainWindow
import sys
from mywin import Ui_MainWindow
class mywin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywin,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("学习英语 贵在坚持")
        self.resize(1500,1000)

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size=self.geometry()
        self.move((screen.width()-size.width())/2,(screen.height()-size.height())/2)

if __name__=="__main__":
    app=QApplication(sys.argv)
    win=mywin()
    win.show()
    win.center()
    sys.exit(app.exec_())


