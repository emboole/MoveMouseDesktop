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
        dlg.setText("🔗 <a href='http://www.plw.com.ar'>PLW</a> (posiblemente no funcione)")
        dlg.setIconPixmap(QPixmap(photo))
        dlg.setInformativeText("Les dejo este easter egg con una foto mía a la gente que quiero, por si me muero. Asumo que <b>Leandro</b> es el único con capacidad y ganas para encontrarlo al día de hoy. <br/><br/><b>Pao y Leandro:</b> haganse cargo de kichis, <b>los estoy observando</b>  👁. Solo puedo confiarles esto a ustedes. Los quiero!<br/> <b>Leandro:</b> Mi broder, mi compañero de aventuras mundiales. Gracias a vos fuí a Japón, y en ese momento se completó una parte enorme de mi vida. Gracias por todas las aventuras bizarras, y por haber laburado conmigo en todos mis proyectos limados!<br/><b>Pao:</b>En los últimos años, que ya todos estabamos más maduros mentalmente, nos hicimos mucho más cercanos y pudimos hablar cosas mucho más profundas. Lamento no poder hacer ese viaje al sur, y me alegro que hayas podido jugar Zelda. Te quiero!<br/><b>Kichis</b>: Estoy muy orgulloso de vos! Sos tán más pilla de lo que fui, y tan inteligente. Usá esos superpoderes para ser feliz. La vida sigue, todos los días pasan cosas como esta. Apoyate en la gente que te quiere (Los tíos, Carli, tus amigos). Recordá que como no tenés hermanos, tus amigos cercanos lo son. Cuidado con los autos! Te amo<br/> <b>Carli:</b> Mi esposa!!! el amor de mi vida!Lamento que el camino haya sido tan corto, pero sin dudas el mejor de mi vida. Gracias por haberme hecho tan feliz y conocer el verdadero amor. Hacé el duelo lo que necesites, y sé que va a ser jodido, pero superalo y seguí con tu vida. Apoyate en tu gente cercana, valen oro! Te amo!<br/> <b>Emilio:</b> Tu nombre es sinónimo de toda la paz de Santa Fé. Sin vos mi infancia hubiera sido otra cosa, pero con vos, todo fue mágico cada año. No hagas huevadas, no fajes a nadie. Entiendo la sensación de no tener nada que perder. La vida sigue, todavía tenés buenas cartas, solo que no las podés ver porque están dadas vuelta en la mesa<br/><b>Mama:</b> Vieja, si no fuera por vos no hubiera llegado nunca a ser quien soy. Hiciste más por mí de lo que el deber requiere. Sé que es una mierda, debe ser el peor dolor del mundo. Pero tranqui, que no duele. Solo volví a ser una parte más del universo. Le mando saludos a Papá y a la Chela!<br/><b>Dev:</b> Broder, mi amigo, mi rival! El Hashirama de mi Madara, Paul y John. Sin dudas haberte conocido cambió el destino, tanto mío como de Leandro. Hubo un momento que los tres fuimos como espejos, mismos sueños, mismos ideales, mismas metas. Sos la influencia más grande que tuve<br/><b>PLW:</b> Bros! Mis vándalos, mis compañeros de cagadas. Por ustedes mi infancia fue la mejor que se pudo tener. Les escribo juntos porque somos inseparables. Les deseo una vida feliz y que sigan conectados entre uds. Inclusive al puto de Carlos que nos borró. Gracias Lalo, Andrés y Carlos. Leandro tiene las imagenes de la remera. <b>PLW FOREVER</b><br/><br/><b>TODOS: NOS VEMOS DEL OTRO LADO</b> NO TENGAN ARREPENTIMIENTOS CON RESPECTO A MÍ, ESTOY EN PAZ CON TODOS USTEDES. Hice todo rapido, espero que sea suficiente<br/> El sol siempre sale de vuelta! Nos vemos en el futuro. Nico.-<br/> Miren la serie del shogi (Sangatsu no lion)")
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
