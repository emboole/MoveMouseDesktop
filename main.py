import sys
import os
import keyboard
from time import sleep
from PyQt6.QtCore import QThread
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

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

def button_clicked():
    dlg = QMessageBox()
    dlg.setWindowTitle("About")
    # photo = (QPixmap("images/nico_jk_polaroid.png"))
    dlg.setText("🔗 <a href='http://www.plw.com.ar'>Link to the site</a><br/>🔗 <a href='http://www.plw.com.ar'>link muy largo 2</a>")
    # dlg.setIconPixmap(QPixmap(photo))
    dlg.setInformativeText("<b>plw</b> es un sitio web que se aguanta los trapos y todos pueden sarandearme el canelon PLWplw dsasadf df dfs sdf sdf fdf sdfsdfdsfs SDFsdfñldsfñlksd fsSDorewjerewr EWRT SoReTeRo CaGoN sarandearme el canelon PLWplw dsasadf df dfs sdf sdf fdf sdfsdfdsfs SDFsdfñldsfñlksd fsSDorewjerewr EWRT SoReTeRo CaGoN sarandearme el canelon PLWplw dsasadf df dfs sdf sdf fdf sdfsdfdsfs SDFsdfñldsfñlksd fsSDorewjerewr EWRT SoReTeRo CaGoN sarandearme el canelon PLWplw dsasadf df dfs sdf sdf fdf sdfsdfdsfs SDFsdfñldsfñlksd fsSDorewjerewr EWRT SoReTeRo CaGoN")
    # dlg.setDetailedText("The details are as follows:")
    dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
    dlg.exec()

def create_menu():
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    icon = QIcon("images/mouse.png")
    tray = QSystemTrayIcon()
    tray.setIcon(icon)
    tray.setVisible(True)

    # Context menu
    menu = QMenu()

    # Actions
    action = QAction("About")
    action.triggered.connect(button_clicked)
    menu.addAction(action)

    quit = QAction("Quit")
    quit.triggered.connect(app.quit)
    menu.addAction(quit)

    # Add the menu to the tray bar
    tray.setContextMenu(menu)
    using_mouse_loop(app)

def using_mouse_loop(app):
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
create_menu()