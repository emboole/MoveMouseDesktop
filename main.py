import sys
import os
import keyboard
from PyQt6.QtWidgets import *
from MouseLoop import *

class Menu:
    def create_menu(self):
        app = QApplication(sys.argv)
        app.setQuitOnLastWindowClosed(False)
        icon = QIcon("images/mouse.png")
        tray = QSystemTrayIcon()
        tray.setIcon(icon)
        tray.setVisible(True)
        tray.setToolTip("asdasd") #tooltip

        # Context menu
        menu = QMenu()

        # Actions
        action = QAction("About")
        action.triggered.connect(self.button_clicked)
        menu.addAction(action)

        quit = QAction("Quit")
        quit.triggered.connect(app.quit)
        menu.addAction(quit)

        # Add the menu to the tray bar
        tray.setContextMenu(menu)
        using_mouse_loop(app)

    def button_clicked(self):
        dlg = QMessageBox()
        dlg.setWindowTitle("About")
        photo = (QPixmap("images/nico_jk_polaroid.png"))
        dlg.setText("That's me programming")
        dlg.setIconPixmap(QPixmap(photo))
        dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
        dlg.exec()

def using_menu(app):
    thread = Menu()
    thread.finished.connect(app.exit)
    thread.start()
    sys.exit(app.exec())

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
m = Menu()
m.create_menu()
