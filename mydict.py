# coding:utf-8
from PyQt5.QtWidgets import QDesktopWidget,QApplication,QMainWindow
import sys
from mywin import Ui_MainWindow
from dlgtest import Ui_Dialog_test

class testdlg(Ui_Dialog_test):
    def __init__(self):
        super(testdlg, self).__init__()
        self.setupUi(self)

class mywin(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mywin,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("学习英语 贵在坚持")
        self.resize(1120,800)
        self.testdlg=testdlg();


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


