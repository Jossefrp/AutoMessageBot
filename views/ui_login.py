# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_v2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QWidget)

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(960, 540)
        LoginWindow.setMinimumSize(QSize(960, 540))
        LoginWindow.setMaximumSize(QSize(960, 540))
        icon = QIcon()
        icon.addFile(u"./assets/icons/img_app.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        LoginWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(480, 0, 480, 540))
        self.frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.425, y1:0.011, x2:0.745, y2:1, stop:0 rgba(55, 73, 97, 255), stop:1 rgba(36, 44, 57, 255));")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 70, 480, 51))
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255,0);\n"
"color: white;")
        self.start_button = QPushButton(self.frame)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setGeometry(QRect(119, 270, 242, 50))
        font = QFont()
        font.setBold(True)
        font.setItalic(False)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet(u"QPushButton{\n"
"	color: white;\n"
"    background-color: rgba(84, 185, 179, 255);\n"
"    border-style: outset;\n"
"    border-radius: 20px;\n"
"    font: bold 16px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(71, 155, 149);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.start_button.setCheckable(False)
        self.start_button.setAutoRepeat(False)
        self.start_button.setAutoExclusive(False)
        self.start_button.setAutoDefault(False)
        self.start_button.setFlat(True)
        self.info_button = QPushButton(self.frame)
        self.info_button.setObjectName(u"info_button")
        self.info_button.setGeometry(QRect(420, 470, 52, 52))
        self.info_button.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/login/info.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.info_button.setIcon(icon1)
        self.info_button.setIconSize(QSize(52, 52))
        self.info_button.setFlat(True)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 480, 540))
        self.frame_2.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.49, y1:0.006, x2:0.525, y2:1, stop:0 rgba(140, 229, 211, 255), stop:0.825 rgba(84, 185, 179, 255));\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.img_python = QLabel(self.frame_2)
        self.img_python.setObjectName(u"img_python")
        self.img_python.setGeometry(QRect(280, 170, 101, 61))
        self.img_python.setStyleSheet(u"background-color: rgb(255, 255, 255, 0%);")
        self.img_python.setPixmap(QPixmap(u"./assets/icons/login/python.png"))
        self.img_python.setScaledContents(True)
        self.title_text = QLabel(self.frame_2)
        self.title_text.setObjectName(u"title_text")
        self.title_text.setGeometry(QRect(0, 50, 480, 81))
        font1 = QFont()
        font1.setPointSize(18)
        self.title_text.setFont(font1)
        self.title_text.setStyleSheet(u"background-color: rgba(255, 255, 255, 0%);\n"
"color: rgb(255, 255, 255);")
        self.img_pc = QLabel(self.frame_2)
        self.img_pc.setObjectName(u"img_pc")
        self.img_pc.setGeometry(QRect(80, 170, 291, 181))
        self.img_pc.setStyleSheet(u"background-color: rgba(255, 255, 255, 0%);")
        self.img_pc.setPixmap(QPixmap(u"./assets/icons/login/pc.png"))
        self.img_pc.setScaledContents(True)
        self.linkd_button = QPushButton(self.frame_2)
        self.linkd_button.setObjectName(u"linkd_button")
        self.linkd_button.setGeometry(QRect(90, 406, 50, 50))
        self.linkd_button.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/login/linkdin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.linkd_button.setIcon(icon2)
        self.linkd_button.setIconSize(QSize(50, 50))
        self.linkd_button.setCheckable(False)
        self.linkd_button.setChecked(False)
        self.linkd_button.setAutoRepeat(False)
        self.linkd_button.setAutoRepeatDelay(300)
        self.linkd_button.setAutoRepeatInterval(100)
        self.linkd_button.setFlat(True)
        self.github_button = QPushButton(self.frame_2)
        self.github_button.setObjectName(u"github_button")
        self.github_button.setGeometry(QRect(90, 452, 50, 50))
        self.github_button.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/login/github.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.github_button.setIcon(icon3)
        self.github_button.setIconSize(QSize(60, 60))
        self.github_button.setAutoRepeat(False)
        self.github_button.setAutoDefault(False)
        self.github_button.setFlat(True)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(145, 422, 211, 22))
        font2 = QFont()
        font2.setPointSize(11)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"background-color: rgba(255, 255, 255,0%);\n"
"color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(145, 463, 211, 22))
        self.label_3.setStyleSheet(u"background-color: rgba(255, 255, 255,0%);\n"
"color: rgb(255, 255, 255);")
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(80, 380, 51, 22))
        font3 = QFont()
        font3.setPointSize(12)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"background-color: rgba(255, 255, 255,0%);\n"
"color: rgb(255, 255, 255);")
        self.title_text.raise_()
        self.img_pc.raise_()
        self.img_python.raise_()
        self.linkd_button.raise_()
        self.github_button.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        LoginWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoginWindow)

        self.github_button.setDefault(False)


        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"automessagebot", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline;\">Automessagebot</span></p></body></html>", None))
        self.start_button.setText(QCoreApplication.translate("LoginWindow", u"Iniciar", None))
        self.info_button.setText("")
        self.img_python.setText("")
        self.title_text.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p align=\"center\">Mandar mensajes a multiples <br/>personas nunca fue tan f\u00e1cil</p></body></html>", None))
        self.img_pc.setText("")
        self.linkd_button.setText("")
        self.github_button.setText("")
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"linkedin.com/in/jossef-ramos/", None))
        self.label_3.setText(QCoreApplication.translate("LoginWindow", u"github.com/Jossefrp", None))
        self.label_4.setText(QCoreApplication.translate("LoginWindow", u"Autor:", None))
    # retranslateUi

