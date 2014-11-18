from PyQt4 import QtGui, uic
import sys

# replace 'c:/test.ui' with real path to ui-file created in QtDesigner

import os

uifile = os.path.dirname(__file__) + '/test.ui'
print uifile
form, base = uic.loadUiType(uifile)


class testQtWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = form()
        self.ui.setupUi(self)


def main():
    app = QtGui.QApplication(sys.argv)
    myapp = testQtWindow()
    myapp.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()