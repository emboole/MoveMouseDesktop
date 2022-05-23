from time import sleep
from PyQt6.QtCore import QThread
from PyQt6.QtGui import *

class MouseLoop(QThread):
    def run(self):
        while True:
            pos = QCursor.pos()
            for i in range(0, 20):
                QCursor.setPos(pos.x() + i + 1, pos.y() + i + 1)
                sleep(0.02)  

            pos = QCursor.pos()
            for i in range(0, 20):
                QCursor.setPos(pos.x() - i - 1, pos.y() - i - 1)
                sleep(0.02)
                
            sleep(5)
