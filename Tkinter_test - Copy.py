import sys
from PyQt4.QtGui import *

class Ui(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        graphicsView = QGraphicsView()
        graphicsView.setStyleSheet("border: 0px")

        grid = QGridLayout()
        grid.addWidget(graphicsView)

        self.setLayout(grid)

app = QApplication(sys.argv)
ui = Ui()
ui.show()
sys.exit(app.exec_())