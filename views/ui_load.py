# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'load_file.ui'
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

class Ui_LoadWindow(object):
    def setupUi(self, LoadWindow):
        if not LoadWindow.objectName():
            LoadWindow.setObjectName(u"LoadWindow")
        LoadWindow.resize(960, 540)
        LoadWindow.setMaximumSize(QSize(960, 540))
        self.centralwidget = QWidget(LoadWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QSize(960, 540))
        self.centralwidget.setMaximumSize(QSize(960, 540))
        self.centralwidget.setAutoFillBackground(True)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setGeometry(QRect(0, 0, 960, 540))
        self.frame.setMinimumSize(QSize(960, 540))
        self.frame.setMaximumSize(QSize(960, 540))
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet(u"background-color: rgb(17, 27, 33);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setEnabled(True)
        self.label.setGeometry(QRect(0, 143, 960, 31))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(365, 340, 230, 50))
        font1 = QFont()
        font1.setPointSize(14)
        self.pushButton.setFont(font1)
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 168, 132);\n"
"	color: rgb(223, 243, 237);\n"
"border-radius: 25px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(6, 207, 156);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color: rgb(0, 168, 132);\n"
"}")
        self.pushButton.setFlat(False)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(420, 195, 120, 75))
        self.label_2.setPixmap(QPixmap(u"./assets/icons/loadFile/excel.png"))
        self.label_2.setScaledContents(True)
        LoadWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(LoadWindow)

        QMetaObject.connectSlotsByName(LoadWindow)
    # setupUi

    def retranslateUi(self, LoadWindow):
        LoadWindow.setWindowTitle(QCoreApplication.translate("LoadWindow", u"automessagebot", None))
        self.label.setText(QCoreApplication.translate("LoadWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; color:#dff3ed;\">Sube un archivo de excel para extraer los datos</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("LoadWindow", u"Subir archivo", None))
        self.label_2.setText("")
    # retranslateUi

