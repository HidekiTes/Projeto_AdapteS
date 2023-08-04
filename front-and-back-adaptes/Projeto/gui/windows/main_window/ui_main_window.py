# IMPORT QT CORE
from PySide6.QtCore import QRect
from qt_core import *

# Import Pages
from gui.pages.ui_pages import Ui_application_pages

# Import Custom Widgets
from gui.widgets.py_push_button import PyPushButton

from PySide6.QtGui import *
from ui import icones

# Main Window
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

        # SET INITIAL PARAMETERS
        # //////////////////////////////////////////////////////////
        parent.resize(1200, 720)
        parent.setMinimumSize(960, 540)

        # Create Central Widget
        # //////////////////////////////////////////////////////////
        self.central_frame=QFrame()

        #Create Main Layout
        self.main_layout = QHBoxLayout(self.central_frame)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)

        #LEFT MENU
        # //////////////////////////////////////////////////////////
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #212123")
        self.left_menu.setMinimumWidth(60)
        self.left_menu.setMaximumWidth(60)

        #Left Menu Layout
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)

        #Top Frame Menu
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(60)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame { background-color: red; }")

        #Top Frame Layout
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_top_layout.setSpacing(0)

        #Top BTNS
        self.toggle_button = PyPushButton(text="Ocultar Menu",
                                          icon_path="menu.svg")
        self.btn_1 = PyPushButton(text="Página Inicial",
                                  is_active=True,
                                  icon_path="home.svg")
        self.btn_2 = PyPushButton(text="Gerenciamento",
                                  icon_path="group.svg")

        #Add Btns to Layout
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.btn_1)
        self.left_menu_top_layout.addWidget(self.btn_2)

        #Menu Spacer
        # //////////////////////////////////////////////////////////
        self.left_menu_spacer = QSpacerItem(20,20, QSizePolicy.Minimum, QSizePolicy.Expanding)

        #Bottom Frame Menu
        # //////////////////////////////////////////////////////////
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(60)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame { background-color: red; }")

        #Bottom Frame Layout
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_bottom_layout.setSpacing(0)

        #Bottom BTNS
        self.settings_btn = PyPushButton(text="Configurações",
                                    icon_path="settings.svg")

        # Add Btns to Layout
        self.left_menu_bottom_layout.addWidget(self.settings_btn)

        # Add to Layout#
        #//////////////////////////////////////////////////////////
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)


        #Content
        self.content = QFrame()
        self.central_frame.setStyleSheet("background-color: #2E2E2E")

        # Content Layout
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)

        #Top Bar
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(60)
        self.top_bar.setMaximumHeight(60)
        self.top_bar.setStyleSheet("background-color: #171717; color: #535353")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(20,0,20,0)

        #Left Label
        self.top_label_left = QLabel("Adapte-S")
        self.top_label_left.setStyleSheet("font-family: Segoe UI; font-size: 24px; font-weight: bold; color: #535353")

        #Top Spacer
        self.top_spacer = QSpacerItem(20,20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        #Right Label
        self.top_label_right = QLabel("| Página Inicial")
        self.top_label_right.setStyleSheet("font-size: 12pt; color: #535353")

        # Add to Layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)

        # Application Pages
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("Font-size: 48px; color: #FFFFFF")
        self.ui_pages = Ui_application_pages()
        self.ui_pages.setupUi(self.pages)
        self.pages.setCurrentWidget(self.ui_pages.Home)

        # Add to Content Layout
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)

        # Add Widgets to App
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)

        # Set Central Widget
        parent.setCentralWidget(self.central_frame)

        # Connect signals to slots
        self.btn_1.clicked.connect(self.show_page_1)
        self.btn_2.clicked.connect(self.show_page_2)
        self.settings_btn.clicked.connect(self.show_page_3)
    def show_page_1(self):
        self.pages.setCurrentWidget(self.ui_pages.Home)
        self.update_right_label("Página Inicial")

    def show_page_2(self):
        self.pages.setCurrentWidget(self.ui_pages.page_2)
        self.update_right_label("Gerenciamento")
    def show_page_3(self):
        self.pages.setCurrentWidget(self.ui_pages.Config)
        self.update_right_label("Configurações")
    def update_right_label(self, text):
        self.top_label_right.setText(f"| {text}")

