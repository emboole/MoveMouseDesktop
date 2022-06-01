# # from PyQt6.QtGui import *
# import sys
# from PyQt6.QtWidgets import *
# from PyQt6.QtGui import *

# class Menu:
#     def create_menu(self, app):
#         # app = QApplication(sys.argv)
#         app.setQuitOnLastWindowClosed(False)
#         icon = QIcon("images/mouse.png")
#         tray = QSystemTrayIcon()
#         tray.setIcon(icon)
#         tray.setVisible(True)

#         # Context menu
#         menu = QMenu()

#         # Actions
#         action = QAction("About")
#         action.triggered.connect(self.button_clicked)
#         menu.addAction(action)

#         quit = QAction("Quit")
#         quit.triggered.connect(app.quit)
#         menu.addAction(quit)

#         # Add the menu to the tray bar
#         tray.setContextMenu(menu)

#     def button_clicked(self):
#         dlg = QMessageBox()
#         dlg.setWindowTitle("About")
#         # photo = (QPixmap("images/nico_jk_polaroid.png"))
#         dlg.setText("🔗 <a href='http://www.plw.com.ar'>Link to the site</a><br/>🔗 <a href='http://www.plw.com.ar'>link muy largo 2</a>")
#         # dlg.setIconPixmap(QPixmap(photo))
#         dlg.setInformativeText("<b>plw</b> es un sitio web que se aguanta los trapos y todos pueden sarandearme el canelon PLWplw dsasadf df dfs sdf sdf fdf sdfsdfdsfs SDFsdfñldsfñlksd fsSDorewjerewr EWRT SoReTeRo CaGoN sarandearme el canelon PLWplw dsasadf df dfs sdf sdf fdf sdfsdfdsfs SDFsdfñldsfñlksd fsSDorewjerewr EWRT SoReTeRo CaGoN sarandearme el canelon PLWplw dsasadf df dfs sdf sdf fdf sdfsdfdsfs SDFsdfñldsfñlksd fsSDorewjerewr EWRT SoReTeRo CaGoN sarandearme el canelon PLWplw dsasadf df dfs sdf sdf fdf sdfsdfdsfs SDFsdfñldsfñlksd fsSDorewjerewr EWRT SoReTeRo CaGoN")
#         # dlg.setDetailedText("The details are as follows:")
#         dlg.setStandardButtons(QMessageBox.StandardButton.Ok)
#         dlg.exec()