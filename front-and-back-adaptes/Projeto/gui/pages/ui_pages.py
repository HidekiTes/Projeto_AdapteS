# -*- coding: utf-8 -*-
from PySide6.QtCore import *
from qt_core import *
from PySide6.QtGui import *
from ui import resource
# url(:/Icons/gui/icons/database_fill.svg


class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(1392, 832)
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.Home.setStyleSheet(u"background-color: rgb(46,46,46);")
        self.verticalLayout = QVBoxLayout(self.Home)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, -1, -1, -1)
        self.A_Titleblock_Home = QFrame(self.Home)
        self.A_Titleblock_Home.setObjectName(u"A_Titleblock_Home")
        self.A_Titleblock_Home.setMaximumSize(QSize(16777215, 100))
        self.A_Titleblock_Home.setStyleSheet(u"")
        self.A_Titleblock_Home.setFrameShape(QFrame.StyledPanel)
        self.A_Titleblock_Home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.A_Titleblock_Home)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(25, 0, -1, 0)
        self.TitleHome_Area_Txt = QFrame(self.A_Titleblock_Home)
        self.TitleHome_Area_Txt.setObjectName(u"TitleHome_Area_Txt")
        self.TitleHome_Area_Txt.setStyleSheet(u"background-color: rgb(46,46,46);")
        self.TitleHome_Area_Txt.setFrameShape(QFrame.StyledPanel)
        self.TitleHome_Area_Txt.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.TitleHome_Area_Txt)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 20, -1, -1)
        self.TitleHome_Lbl_saudacao = QLabel(self.TitleHome_Area_Txt)
        self.TitleHome_Lbl_saudacao.setObjectName(u"TitleHome_Lbl_saudacao")
        self.TitleHome_Lbl_saudacao.setStyleSheet(u"font-family: Segoe UI;\n"
"font-size: 30px;\n"
"color: white;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_6.addWidget(self.TitleHome_Lbl_saudacao)


        self.verticalLayout_4.addWidget(self.TitleHome_Area_Txt)


        self.verticalLayout.addWidget(self.A_Titleblock_Home)

        self.B_Body_Home = QFrame(self.Home)
        self.B_Body_Home.setObjectName(u"B_Body_Home")
        self.B_Body_Home.setFrameShape(QFrame.StyledPanel)
        self.B_Body_Home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.B_Body_Home)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(25, -1, -1, -1)
        self.BodyHome_Align_Content_1_2 = QFrame(self.B_Body_Home)
        self.BodyHome_Align_Content_1_2.setObjectName(u"BodyHome_Align_Content_1_2")
        self.BodyHome_Align_Content_1_2.setMaximumSize(QSize(16777215, 500))
        self.BodyHome_Align_Content_1_2.setStyleSheet(u"")
        self.BodyHome_Align_Content_1_2.setFrameShape(QFrame.StyledPanel)
        self.BodyHome_Align_Content_1_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.BodyHome_Align_Content_1_2)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.BodyHome_Campo_1 = QFrame(self.BodyHome_Align_Content_1_2)
        self.BodyHome_Campo_1.setObjectName(u"BodyHome_Campo_1")
        self.BodyHome_Campo_1.setStyleSheet(u"background-color: rgb(61,61,61);\n"
"border-radius: 5px;")
        self.BodyHome_Campo_1.setFrameShape(QFrame.StyledPanel)
        self.BodyHome_Campo_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.BodyHome_Campo_1)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.BH_Area_Titulo_1 = QFrame(self.BodyHome_Campo_1)
        self.BH_Area_Titulo_1.setObjectName(u"BH_Area_Titulo_1")
        self.BH_Area_Titulo_1.setMaximumSize(QSize(16777215, 50))
        self.BH_Area_Titulo_1.setStyleSheet(u"")
        self.BH_Area_Titulo_1.setFrameShape(QFrame.StyledPanel)
        self.BH_Area_Titulo_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.BH_Area_Titulo_1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.BH_Icone_Titulo_1 = QFrame(self.BH_Area_Titulo_1)
        self.BH_Icone_Titulo_1.setObjectName(u"BH_Icone_Titulo_1")
        self.BH_Icone_Titulo_1.setMaximumSize(QSize(50, 50))
        self.BH_Icone_Titulo_1.setStyleSheet(u"\n"
"background-image: url(:/newPrefix/gui/icons/database_fill.svg);\n"
"\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.BH_Icone_Titulo_1.setFrameShape(QFrame.StyledPanel)
        self.BH_Icone_Titulo_1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.BH_Icone_Titulo_1)

        self.BH_Campo_Titulo_1 = QFrame(self.BH_Area_Titulo_1)
        self.BH_Campo_Titulo_1.setObjectName(u"BH_Campo_Titulo_1")
        self.BH_Campo_Titulo_1.setMaximumSize(QSize(16777215, 50))
        self.BH_Campo_Titulo_1.setStyleSheet(u"")
        self.BH_Campo_Titulo_1.setFrameShape(QFrame.StyledPanel)
        self.BH_Campo_Titulo_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.BH_Campo_Titulo_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.BH_Titulo_1 = QLabel(self.BH_Campo_Titulo_1)
        self.BH_Titulo_1.setObjectName(u"BH_Titulo_1")
        self.BH_Titulo_1.setStyleSheet(u"font-family: Segoe UI;\n"
"font-size: 20px;\n"
"color: white;\n"
"font-weight: light;\n"
"")

        self.verticalLayout_8.addWidget(self.BH_Titulo_1)


        self.horizontalLayout_2.addWidget(self.BH_Campo_Titulo_1)


        self.verticalLayout_7.addWidget(self.BH_Area_Titulo_1)

        self.BH_Area_Campo_1 = QFrame(self.BodyHome_Campo_1)
        self.BH_Area_Campo_1.setObjectName(u"BH_Area_Campo_1")
        self.BH_Area_Campo_1.setStyleSheet(u"background-color: rgb(78,78,78);")
        self.BH_Area_Campo_1.setFrameShape(QFrame.StyledPanel)
        self.BH_Area_Campo_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.BH_Area_Campo_1)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")

        self.verticalLayout_7.addWidget(self.BH_Area_Campo_1)


        self.horizontalLayout.addWidget(self.BodyHome_Campo_1)

        self.BodyHome_Campo_2 = QFrame(self.BodyHome_Align_Content_1_2)
        self.BodyHome_Campo_2.setObjectName(u"BodyHome_Campo_2")
        self.BodyHome_Campo_2.setStyleSheet(u"background-color: rgb(61,61,61);\n"
"border-radius: 5px;")
        self.BodyHome_Campo_2.setFrameShape(QFrame.StyledPanel)
        self.BodyHome_Campo_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.BodyHome_Campo_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.BH_Area_Titulo_2 = QFrame(self.BodyHome_Campo_2)
        self.BH_Area_Titulo_2.setObjectName(u"BH_Area_Titulo_2")
        self.BH_Area_Titulo_2.setMaximumSize(QSize(16777215, 50))
        self.BH_Area_Titulo_2.setStyleSheet(u"")
        self.BH_Area_Titulo_2.setFrameShape(QFrame.StyledPanel)
        self.BH_Area_Titulo_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.BH_Area_Titulo_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BH_Icone_Titulo_2 = QFrame(self.BH_Area_Titulo_2)
        self.BH_Icone_Titulo_2.setObjectName(u"BH_Icone_Titulo_2")
        self.BH_Icone_Titulo_2.setMaximumSize(QSize(50, 50))
        self.BH_Icone_Titulo_2.setStyleSheet(u"\n"
"background-image: url(:/newPrefix/gui/icons/database_fill.svg);\n"
"\n"
"background-repeat: no-repeat;\n"
"background-position: center;\n"
"")
        self.BH_Icone_Titulo_2.setFrameShape(QFrame.StyledPanel)
        self.BH_Icone_Titulo_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.BH_Icone_Titulo_2)

        self.BH_Campo_Titulo_2 = QFrame(self.BH_Area_Titulo_2)
        self.BH_Campo_Titulo_2.setObjectName(u"BH_Campo_Titulo_2")
        self.BH_Campo_Titulo_2.setMaximumSize(QSize(16777215, 50))
        self.BH_Campo_Titulo_2.setStyleSheet(u"")
        self.BH_Campo_Titulo_2.setFrameShape(QFrame.StyledPanel)
        self.BH_Campo_Titulo_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.BH_Campo_Titulo_2)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.BH_Titulo_2 = QLabel(self.BH_Campo_Titulo_2)
        self.BH_Titulo_2.setObjectName(u"BH_Titulo_2")
        self.BH_Titulo_2.setStyleSheet(u"font-family: Segoe UI;\n"
"font-size: 20px;\n"
"color: white;\n"
"font-weight: light;\n"
"")

        self.verticalLayout_10.addWidget(self.BH_Titulo_2)


        self.horizontalLayout_3.addWidget(self.BH_Campo_Titulo_2)


        self.verticalLayout_9.addWidget(self.BH_Area_Titulo_2)

        self.BH_Area_Campo_2 = QFrame(self.BodyHome_Campo_2)
        self.BH_Area_Campo_2.setObjectName(u"BH_Area_Campo_2")
        self.BH_Area_Campo_2.setStyleSheet(u"background-color: rgb(78,78,78);")
        self.BH_Area_Campo_2.setFrameShape(QFrame.StyledPanel)
        self.BH_Area_Campo_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.BH_Area_Campo_2)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")

        self.verticalLayout_9.addWidget(self.BH_Area_Campo_2)


        self.horizontalLayout.addWidget(self.BodyHome_Campo_2)


        self.verticalLayout_2.addWidget(self.BodyHome_Align_Content_1_2)

        self.BodyHome_Align_Content_3 = QFrame(self.B_Body_Home)
        self.BodyHome_Align_Content_3.setObjectName(u"BodyHome_Align_Content_3")
        self.BodyHome_Align_Content_3.setStyleSheet(u"background-color: rgb(46,46,46);")
        self.BodyHome_Align_Content_3.setFrameShape(QFrame.StyledPanel)
        self.BodyHome_Align_Content_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.BodyHome_Align_Content_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.BodyHome_Campo_3 = QFrame(self.BodyHome_Align_Content_3)
        self.BodyHome_Campo_3.setObjectName(u"BodyHome_Campo_3")
        self.BodyHome_Campo_3.setStyleSheet(u"background-color: rgb(61,61,61);\n"
"border-radius: 5px;")
        self.BodyHome_Campo_3.setFrameShape(QFrame.StyledPanel)
        self.BodyHome_Campo_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.BodyHome_Campo_3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.BH_Area_Titulo_3 = QFrame(self.BodyHome_Campo_3)
        self.BH_Area_Titulo_3.setObjectName(u"BH_Area_Titulo_3")
        self.BH_Area_Titulo_3.setMaximumSize(QSize(16777215, 50))
        self.BH_Area_Titulo_3.setStyleSheet(u"")
        self.BH_Area_Titulo_3.setFrameShape(QFrame.StyledPanel)
        self.BH_Area_Titulo_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.BH_Area_Titulo_3)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.BH_Icone_Titulo_3 = QFrame(self.BH_Area_Titulo_3)
        self.BH_Icone_Titulo_3.setObjectName(u"BH_Icone_Titulo_3")
        self.BH_Icone_Titulo_3.setMaximumSize(QSize(50, 50))
        self.BH_Icone_Titulo_3.setStyleSheet(u"background-image: url(:/newPrefix/gui/icons/notifications_fill.svg);\n"
"background-repeat: no-repeat;\n"
"background-position: center;")
        self.BH_Icone_Titulo_3.setFrameShape(QFrame.StyledPanel)
        self.BH_Icone_Titulo_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.BH_Icone_Titulo_3)

        self.BH_Campo_Titulo_3 = QFrame(self.BH_Area_Titulo_3)
        self.BH_Campo_Titulo_3.setObjectName(u"BH_Campo_Titulo_3")
        self.BH_Campo_Titulo_3.setMaximumSize(QSize(16777215, 50))
        self.BH_Campo_Titulo_3.setStyleSheet(u"")
        self.BH_Campo_Titulo_3.setFrameShape(QFrame.StyledPanel)
        self.BH_Campo_Titulo_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.BH_Campo_Titulo_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.BH_Titulo_3 = QLabel(self.BH_Campo_Titulo_3)
        self.BH_Titulo_3.setObjectName(u"BH_Titulo_3")
        self.BH_Titulo_3.setStyleSheet(u"font-family: Segoe UI;\n"
"font-size: 20px;\n"
"color: white;\n"
"font-weight: light;\n"
"")

        self.verticalLayout_12.addWidget(self.BH_Titulo_3)


        self.horizontalLayout_4.addWidget(self.BH_Campo_Titulo_3)


        self.verticalLayout_11.addWidget(self.BH_Area_Titulo_3)

        self.BH_Area_Campos_Format = QFrame(self.BodyHome_Campo_3)
        self.BH_Area_Campos_Format.setObjectName(u"BH_Area_Campos_Format")
        self.BH_Area_Campos_Format.setStyleSheet(u"")
        self.BH_Area_Campos_Format.setFrameShape(QFrame.StyledPanel)
        self.BH_Area_Campos_Format.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.BH_Area_Campos_Format)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.BH_Area_Campo_3 = QFrame(self.BH_Area_Campos_Format)
        self.BH_Area_Campo_3.setObjectName(u"BH_Area_Campo_3")
        self.BH_Area_Campo_3.setEnabled(True)
        self.BH_Area_Campo_3.setStyleSheet(u"background-color: rgb(78,78,78);")
        self.BH_Area_Campo_3.setFrameShape(QFrame.StyledPanel)
        self.BH_Area_Campo_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.BH_Area_Campo_3)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")

        self.horizontalLayout_5.addWidget(self.BH_Area_Campo_3)

        self.BH_Area_Campo_4 = QFrame(self.BH_Area_Campos_Format)
        self.BH_Area_Campo_4.setObjectName(u"BH_Area_Campo_4")
        self.BH_Area_Campo_4.setStyleSheet(u"background-color: rgb(78,78,78);")
        self.BH_Area_Campo_4.setFrameShape(QFrame.StyledPanel)
        self.BH_Area_Campo_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.BH_Area_Campo_4)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")

        self.horizontalLayout_5.addWidget(self.BH_Area_Campo_4)


        self.verticalLayout_11.addWidget(self.BH_Area_Campos_Format)


        self.verticalLayout_3.addWidget(self.BodyHome_Campo_3)


        self.verticalLayout_2.addWidget(self.BodyHome_Align_Content_3)


        self.verticalLayout.addWidget(self.B_Body_Home)

        self.C_Footer_Home = QFrame(self.Home)
        self.C_Footer_Home.setObjectName(u"C_Footer_Home")
        self.C_Footer_Home.setMaximumSize(QSize(16777215, 40))
        self.C_Footer_Home.setStyleSheet(u"")
        self.C_Footer_Home.setFrameShape(QFrame.StyledPanel)
        self.C_Footer_Home.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.C_Footer_Home)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(25, 0, -1, 0)
        self.FooterHome_Area = QFrame(self.C_Footer_Home)
        self.FooterHome_Area.setObjectName(u"FooterHome_Area")
        self.FooterHome_Area.setStyleSheet(u"")
        self.FooterHome_Area.setFrameShape(QFrame.StyledPanel)
        self.FooterHome_Area.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.FooterHome_Area)


        self.verticalLayout.addWidget(self.C_Footer_Home)

        application_pages.addWidget(self.Home)
        self.A_Titleblock_Home.raise_()
        self.C_Footer_Home.raise_()
        self.B_Body_Home.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        application_pages.addWidget(self.page_2)
        self.Config = QWidget()
        self.Config.setObjectName(u"Config")
        self.Config.setStyleSheet(u"background-color: rgb(46,46,46);")
        self.verticalLayout_13 = QVBoxLayout(self.Config)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.A_Titleblock_Settings = QFrame(self.Config)
        self.A_Titleblock_Settings.setObjectName(u"A_Titleblock_Settings")
        self.A_Titleblock_Settings.setMaximumSize(QSize(16777215, 100))
        self.A_Titleblock_Settings.setStyleSheet(u"")
        self.A_Titleblock_Settings.setFrameShape(QFrame.StyledPanel)
        self.A_Titleblock_Settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.A_Titleblock_Settings)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(25, 0, -1, 0)
        self.TitleSettings_Area_Txt = QFrame(self.A_Titleblock_Settings)
        self.TitleSettings_Area_Txt.setObjectName(u"TitleSettings_Area_Txt")
        self.TitleSettings_Area_Txt.setStyleSheet(u"background-color: rgb(46,46,46);")
        self.TitleSettings_Area_Txt.setFrameShape(QFrame.StyledPanel)
        self.TitleSettings_Area_Txt.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.TitleSettings_Area_Txt)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 20, -1, -1)
        self.TitleSettings_Lbl_saudacao = QLabel(self.TitleSettings_Area_Txt)
        self.TitleSettings_Lbl_saudacao.setObjectName(u"TitleSettings_Lbl_saudacao")
        self.TitleSettings_Lbl_saudacao.setStyleSheet(u"font-family: Segoe UI;\n"
"font-size: 30px;\n"
"color: white;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_15.addWidget(self.TitleSettings_Lbl_saudacao)


        self.verticalLayout_14.addWidget(self.TitleSettings_Area_Txt)


        self.verticalLayout_13.addWidget(self.A_Titleblock_Settings)

        self.B_Body_Settings = QFrame(self.Config)
        self.B_Body_Settings.setObjectName(u"B_Body_Settings")
        self.B_Body_Settings.setFrameShape(QFrame.StyledPanel)
        self.B_Body_Settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.B_Body_Settings)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.Settings_ButtonBar = QFrame(self.B_Body_Settings)
        self.Settings_ButtonBar.setObjectName(u"Settings_ButtonBar")
        self.Settings_ButtonBar.setMaximumSize(QSize(16777215, 33))
        self.Settings_ButtonBar.setStyleSheet(u"")
        self.Settings_ButtonBar.setFrameShape(QFrame.StyledPanel)
        self.Settings_ButtonBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.Settings_ButtonBar)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.A_SettingsBtn_DBConnection = QPushButton(self.Settings_ButtonBar)
        self.A_SettingsBtn_DBConnection.setObjectName(u"A_SettingsBtn_DBConnection")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.A_SettingsBtn_DBConnection.sizePolicy().hasHeightForWidth())
        self.A_SettingsBtn_DBConnection.setSizePolicy(sizePolicy)
        self.A_SettingsBtn_DBConnection.setMinimumSize(QSize(275, 0))
        self.A_SettingsBtn_DBConnection.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(120, 120, 120, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush3 = QBrush(QColor(0, 0, 0, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.A_SettingsBtn_DBConnection.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        self.A_SettingsBtn_DBConnection.setFont(font)
        self.A_SettingsBtn_DBConnection.setAutoFillBackground(False)
        self.A_SettingsBtn_DBConnection.setStyleSheet(u"font-size: 18px;\n"
"background-color: rgb(120, 120, 120);")
        self.A_SettingsBtn_DBConnection.setCheckable(True)
        self.A_SettingsBtn_DBConnection.setChecked(True)
        self.A_SettingsBtn_DBConnection.setAutoDefault(False)
        self.A_SettingsBtn_DBConnection.setFlat(True)

        self.horizontalLayout_6.addWidget(self.A_SettingsBtn_DBConnection)

        self.B_SettingsBtn_GeralSettings = QPushButton(self.Settings_ButtonBar)
        self.B_SettingsBtn_GeralSettings.setObjectName(u"B_SettingsBtn_GeralSettings")
        sizePolicy.setHeightForWidth(self.B_SettingsBtn_GeralSettings.sizePolicy().hasHeightForWidth())
        self.B_SettingsBtn_GeralSettings.setSizePolicy(sizePolicy)
        self.B_SettingsBtn_GeralSettings.setMinimumSize(QSize(200, 0))
        self.B_SettingsBtn_GeralSettings.setMaximumSize(QSize(16777215, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.B_SettingsBtn_GeralSettings.setPalette(palette1)
        self.B_SettingsBtn_GeralSettings.setFont(font)
        self.B_SettingsBtn_GeralSettings.setAutoFillBackground(False)
        self.B_SettingsBtn_GeralSettings.setStyleSheet(u"font-size: 18px;\n"
"background-color: rgb(120, 120, 120);")
        self.B_SettingsBtn_GeralSettings.setCheckable(True)
        self.B_SettingsBtn_GeralSettings.setAutoDefault(False)
        self.B_SettingsBtn_GeralSettings.setFlat(True)

        self.horizontalLayout_6.addWidget(self.B_SettingsBtn_GeralSettings)

        self.C_SettingsBtn_Updates = QPushButton(self.Settings_ButtonBar)
        self.C_SettingsBtn_Updates.setObjectName(u"C_SettingsBtn_Updates")
        sizePolicy.setHeightForWidth(self.C_SettingsBtn_Updates.sizePolicy().hasHeightForWidth())
        self.C_SettingsBtn_Updates.setSizePolicy(sizePolicy)
        self.C_SettingsBtn_Updates.setMinimumSize(QSize(130, 0))
        self.C_SettingsBtn_Updates.setMaximumSize(QSize(16777215, 16777215))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.C_SettingsBtn_Updates.setPalette(palette2)
        self.C_SettingsBtn_Updates.setFont(font)
        self.C_SettingsBtn_Updates.setAutoFillBackground(False)
        self.C_SettingsBtn_Updates.setStyleSheet(u"font-size: 18px;\n"
"background-color: rgb(120, 120, 120);")
        self.C_SettingsBtn_Updates.setCheckable(True)
        self.C_SettingsBtn_Updates.setAutoRepeat(False)
        self.C_SettingsBtn_Updates.setAutoExclusive(False)
        self.C_SettingsBtn_Updates.setAutoRepeatDelay(100)
        self.C_SettingsBtn_Updates.setAutoRepeatInterval(0)
        self.C_SettingsBtn_Updates.setAutoDefault(False)
        self.C_SettingsBtn_Updates.setFlat(True)

        self.horizontalLayout_6.addWidget(self.C_SettingsBtn_Updates)

        self.A_SettingsSpacer = QSpacerItem(60, 13, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.A_SettingsSpacer)

        self.D_SettingsBtn_UseTerms = QPushButton(self.Settings_ButtonBar)
        self.D_SettingsBtn_UseTerms.setObjectName(u"D_SettingsBtn_UseTerms")
        sizePolicy.setHeightForWidth(self.D_SettingsBtn_UseTerms.sizePolicy().hasHeightForWidth())
        self.D_SettingsBtn_UseTerms.setSizePolicy(sizePolicy)
        self.D_SettingsBtn_UseTerms.setMinimumSize(QSize(145, 0))
        self.D_SettingsBtn_UseTerms.setMaximumSize(QSize(16777215, 16777215))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush3)
#endif
        self.D_SettingsBtn_UseTerms.setPalette(palette3)
        self.D_SettingsBtn_UseTerms.setFont(font)
        self.D_SettingsBtn_UseTerms.setAutoFillBackground(False)
        self.D_SettingsBtn_UseTerms.setStyleSheet(u"font-size: 18px;\n"
"background-color: rgb(120, 120, 120);")
        self.D_SettingsBtn_UseTerms.setCheckable(True)
        self.D_SettingsBtn_UseTerms.setChecked(False)
        self.D_SettingsBtn_UseTerms.setAutoDefault(False)
        self.D_SettingsBtn_UseTerms.setFlat(True)

        self.horizontalLayout_6.addWidget(self.D_SettingsBtn_UseTerms)


        self.verticalLayout_17.addWidget(self.Settings_ButtonBar)

        self.Settings_Area_Campo = QFrame(self.B_Body_Settings)
        self.Settings_Area_Campo.setObjectName(u"Settings_Area_Campo")
        self.Settings_Area_Campo.setMinimumSize(QSize(0, 575))
        self.Settings_Area_Campo.setStyleSheet(u"background-color: rgb(61,61,61);")
        self.Settings_Area_Campo.setFrameShape(QFrame.StyledPanel)
        self.Settings_Area_Campo.setFrameShadow(QFrame.Raised)

        self.verticalLayout_17.addWidget(self.Settings_Area_Campo)


        self.verticalLayout_13.addWidget(self.B_Body_Settings)

        self.C_Footer_Settings = QFrame(self.Config)
        self.C_Footer_Settings.setObjectName(u"C_Footer_Settings")
        self.C_Footer_Settings.setMaximumSize(QSize(16777215, 40))
        self.C_Footer_Settings.setStyleSheet(u"")
        self.C_Footer_Settings.setFrameShape(QFrame.StyledPanel)
        self.C_Footer_Settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.C_Footer_Settings)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(25, 0, -1, 0)
        self.frame_16 = QFrame(self.C_Footer_Settings)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setStyleSheet(u"")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)

        self.verticalLayout_16.addWidget(self.frame_16)


        self.verticalLayout_13.addWidget(self.C_Footer_Settings)

        application_pages.addWidget(self.Config)

        self.retranslateUi(application_pages)

        application_pages.setCurrentIndex(2)
        self.A_SettingsBtn_DBConnection.setDefault(False)
        self.C_SettingsBtn_Updates.setDefault(False)
        self.D_SettingsBtn_UseTerms.setDefault(False)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.TitleHome_Lbl_saudacao.setText(QCoreApplication.translate("application_pages", u"Seja Bem Vindo", None))
        self.BH_Titulo_1.setText(QCoreApplication.translate("application_pages", u"Informa\u00e7\u00f5es", None))
        self.BH_Titulo_2.setText(QCoreApplication.translate("application_pages", u"Informa\u00e7\u00f5es 2", None))
        self.BH_Titulo_3.setText(QCoreApplication.translate("application_pages", u"Campo com Personaliza\u00e7\u00e3o", None))
        self.TitleSettings_Lbl_saudacao.setText(QCoreApplication.translate("application_pages", u"Configura\u00e7\u00f5es", None))
        self.A_SettingsBtn_DBConnection.setText(QCoreApplication.translate("application_pages", u"Conex\u00e3o com Banco de Dados", None))
        self.B_SettingsBtn_GeralSettings.setText(QCoreApplication.translate("application_pages", u"Configura\u00e7\u00f5es gerais", None))
        self.C_SettingsBtn_Updates.setText(QCoreApplication.translate("application_pages", u"Atualiza\u00e7\u00f5es", None))
        self.D_SettingsBtn_UseTerms.setText(QCoreApplication.translate("application_pages", u"Termos de Uso", None))
    # retranslateUi

