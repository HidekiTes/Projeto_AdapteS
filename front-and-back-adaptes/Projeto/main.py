# IMPORT MODULES
import sys
import os
from PySide6.QtGui import *
from ui import resource


from PySide6.QtCore import QPropertyAnimation, QEasingCurve

# IMPORT QT CORE
from qt_core import *

# IMPORT MAIN WINDOW
from gui.windows.main_window.ui_main_window import UI_MainWindow

# MAIN WINDOW
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Definindo nome da janela
        self.setWindowTitle("Adapte-S")

        # Setup Main Window
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Toggle Button
        self.ui.toggle_button.clicked.connect(self.toggle_button)

        # Definição das trocas de telas
        self.ui.btn_1.clicked.connect(self.show_page_1)
        self.ui.btn_2.clicked.connect(self.show_page_2)
        self.ui.settings_btn.clicked.connect(self.show_page_3)

        # Exibição da Aplicação
        self.show()

    def reset_selection(self):
        for btn in self.ui.left_menu.findChildren(QPushButton):
            try:
                btn.set_active(False)
            except:
                pass


    #Definição dos direcionamentos para troca de telas
    def show_page_1(self):
        #print("clicado")
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.Home)
        self.ui.btn_1.set_active(True)
    def show_page_2(self):
        #print("clicado")
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.page_2)
        self.ui.btn_2.set_active(True)
    def show_page_3(self):
        # print("clicado")
        self.reset_selection()
        self.ui.pages.setCurrentWidget(self.ui.ui_pages.Config)
        self.ui.settings_btn.set_active(True)
    def toggle_button(self):
        # Obtém a largura do menu
        menu_width = self.ui.left_menu.width()

        # Verifica a largura
        width = 60
        if menu_width == 60:
            width = 240

        # Inicia a animação
        self.animation = QPropertyAnimation(self.ui.left_menu, b"minimumWidth")
        self.animation.setStartValue(menu_width)
        self.animation.setEndValue(width)
        self.animation.setDuration(500)
        self.animation.setEasingCurve(QEasingCurve.InOutCirc)
        self.animation.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
