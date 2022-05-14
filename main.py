import sys
import os
import sys
import os
import keyboard
import threading
from time import strftime, localtime, sleep
from PyQt6.QtGui import QGuiApplication, QCursor
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal, QThread, QObject
from PyQt6 import QtWidgets

class Backend(QObject):    
    def __init__(self):
        QObject.__init__(self)

    updated = pyqtSignal(str, arguments=['updater'])
    def updater(self, curr_time):
        self.updated.emit(curr_time)

    def bootUp(self):
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()    

    def _bootUp(self):
        while True:
            curr_time = strftime("%H:%M:%S", localtime())
            self.updater(curr_time)
            sleep(0.1)

class MouseLoop(QThread):
    def run(self):
        count = 0
        while True:
            sleep(1)
            QCursor.setPos(100, 100)
            sleep(1)
            QCursor.setPos(150, 150)

def using_mouse_loop():
    app = QtWidgets.QApplication(sys.argv)
    thread = MouseLoop()
    thread.finished.connect(app.exit)
    thread.start()
    sys.exit(app.exec())

def keyHook(info):
    while True:
        if keyboard.is_pressed("q"):
            print("chau")
            os._exit(0)

keyboard.hook(keyHook)

QQuickWindow.setSceneGraphBackend('software')

app = QGuiApplication(sys.argv)
curr_time = strftime("%H:%M:%S", localtime())

engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')

back_end = Backend()
engine.rootObjects()[0].setProperty('backend', back_end)
back_end.bootUp()

using_mouse_loop()