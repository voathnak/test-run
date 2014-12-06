from PyQt4 import QtGui, uic
import sys

# replace 'c:/test.ui' with real path to ui-file created in QtDesigner

import os


uifile = os.path.dirname(__file__) + '/gui/test.ui'
print uifile
form, base = uic.loadUiType(uifile)


class testQtWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        # self.button = QtGui.QPushButton('pushButton', self)
        # self.button.clicked.connect(self.handleButton)
        self.ui = form()
        self.ui.setupUi(self)

        self.ui.get_pri_k_btn.clicked.connect(self.generate_private_key)
        # self.ui.get_pri_k_btn.clicked.connect(self.handleButton)



    def handleButton(self):
        print ('Hello World')
        self.ui.txt_send_string.setText("Hello World!")



def main():
    app = QtGui.QApplication(sys.argv)
    myapp = testQtWindow()
    myapp.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()