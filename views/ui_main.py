# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'main.ui'
##
# Created by: Qt User Interface Compiler version 6.7.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
                               QHeaderView, QLabel, QMainWindow, QProgressBar,
                               QPushButton, QRadioButton, QSizePolicy, QStackedWidget,
                               QTableWidget, QTableWidgetItem, QTextEdit, QWidget)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(960, 540)
        MainWindow.setMinimumSize(QSize(960, 540))
        MainWindow.setMaximumSize(QSize(960, 540))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(960, 540))
        self.centralwidget.setMaximumSize(QSize(960, 540))
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 960, 540))
        self.stackedWidget.setMinimumSize(QSize(960, 540))
        self.stackedWidget.setMaximumSize(QSize(960, 540))
        self.stackedWidget.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.stackedWidget.setFrameShape(QFrame.NoFrame)
        self.select_column = QWidget()
        self.select_column.setObjectName(u"select_column")
        self.select_column.setMinimumSize(QSize(960, 540))
        self.select_column.setMaximumSize(QSize(960, 540))
        self.label_2 = QLabel(self.select_column)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(65, 44, 771, 51))
        self.label_2.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);")
        self.select_number_frame = QFrame(self.select_column)
        self.select_number_frame.setObjectName(u"select_number_frame")
        self.select_number_frame.setGeometry(QRect(130, 120, 700, 110))
        self.select_number_frame.setFrameShape(QFrame.StyledPanel)
        self.select_number_frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.select_number_frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 701, 111))
        self.select_number = QGridLayout(self.gridLayoutWidget)
        self.select_number.setObjectName(u"select_number")
        self.select_number.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.gridLayoutWidget)
        self.radioButton.setObjectName(u"radioButton")

        self.select_number.addWidget(self.radioButton, 0, 0, 1, 1)

        self.label_9 = QLabel(self.select_column)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(65, 240, 771, 51))
        self.label_9.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);")
        self.select_columns_frame = QFrame(self.select_column)
        self.select_columns_frame.setObjectName(u"select_columns_frame")
        self.select_columns_frame.setGeometry(QRect(130, 297, 700, 110))
        self.select_columns_frame.setFrameShape(QFrame.StyledPanel)
        self.select_columns_frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_3 = QWidget(self.select_columns_frame)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(0, 0, 701, 111))
        self.select_columns = QGridLayout(self.gridLayoutWidget_3)
        self.select_columns.setObjectName(u"select_columns")
        self.select_columns.setContentsMargins(0, 0, 0, 0)
        self.checkBox = QCheckBox(self.gridLayoutWidget_3)
        self.checkBox.setObjectName(u"checkBox")

        self.select_columns.addWidget(self.checkBox, 0, 0, 1, 1)

        self.start_button_3 = QPushButton(self.select_column)
        self.start_button_3.setObjectName(u"start_button_3")
        self.start_button_3.setGeometry(QRect(365, 442, 230, 50))
        font = QFont()
        font.setPointSize(15)
        self.start_button_3.setFont(font)
        self.start_button_3.setStyleSheet(u"QPushButton{\n"
                                          "	background-color: rgb(79, 117, 255);\n"
                                          "border-radius: 20px;\n"
                                          "color: white;\n"
                                          "}\n"
                                          "QPushButton:hover{\n"
                                          "	background-color: rgb(76, 163, 255);\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          "background-color: rgb(79, 117, 255);\n"
                                          "}")
        self.stackedWidget.addWidget(self.select_column)
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.main.setMinimumSize(QSize(960, 540))
        self.main.setMaximumSize(QSize(960, 540))
        self.main_frame = QFrame(self.main)
        self.main_frame.setObjectName(u"main_frame")
        self.main_frame.setGeometry(QRect(0, 0, 960, 540))
        self.main_frame.setMinimumSize(QSize(960, 540))
        self.main_frame.setMaximumSize(QSize(960, 540))
        self.main_frame.setAutoFillBackground(False)
        self.main_frame.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.main_frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(65, 44, 391, 51))
        self.label.setStyleSheet(u"background-color: rgba(255, 255, 255, 0);")
        self.message_text = QTextEdit(self.main_frame)
        self.message_text.setObjectName(u"message_text")
        self.message_text.setGeometry(QRect(65, 100, 830, 64))
        self.message_text.setAutoFillBackground(True)
        self.message_text.setStyleSheet(u"resize:none;\n"
                                        "color: black;\n"
                                        "background-color: rgb(217, 217, 217);")
        self.message_text.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.message_text.setTabChangesFocus(False)
        self.start_main_button = QPushButton(self.main_frame)
        self.start_main_button.setObjectName(u"start_main_button")
        self.start_main_button.setGeometry(QRect(365, 442, 230, 50))
        self.start_main_button.setFont(font)
        self.start_main_button.setStyleSheet(u"QPushButton{\n"
                                             "	background-color: rgb(79, 117, 255);\n"
                                             "border-radius: 20px;\n"
                                             "color: white;\n"
                                             "}\n"
                                             "QPushButton:hover{\n"
                                             "	background-color: rgb(76, 163, 255);\n"
                                             "}\n"
                                             "QPushButton:pressed{\n"
                                             "background-color: rgb(79, 117, 255);\n"
                                             "}")
        self.tableWidget = QTableWidget(self.main_frame)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(190, 191, 578, 216))
        sizePolicy = QSizePolicy(
            QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(2000, 2000))
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
                                       "	background-color: rgb(255, 255, 255);\n"
                                       "gridline-color: rgb(0,206,151);\n"
                                       "font-size: 12px;\n"
                                       "}\n"
                                       "QHeaderView::section{\n"
                                       "	background-color: rgb(46, 112, 255);\n"
                                       "border: 1px solid rgb(0,0,0);\n"
                                       "font-size: 12px;\n"
                                       "}\n"
                                       "QTableWidget:QTableCornerButton::section{\n"
                                       "	background-color: rgb(0,0,0);\n"
                                       "border: 1px solid rgb(0,206,151);\n"
                                       "}")
        self.tableWidget.setFrameShadow(QFrame.Raised)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(199)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.stackedWidget.addWidget(self.main)
        self.load_browser = QWidget()
        self.load_browser.setObjectName(u"load_browser")
        self.load_browser.setMaximumSize(QSize(960, 540))
        self.browser_frame = QFrame(self.load_browser)
        self.browser_frame.setObjectName(u"browser_frame")
        self.browser_frame.setGeometry(QRect(0, 0, 960, 540))
        self.browser_frame.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.browser_frame.setFrameShape(QFrame.StyledPanel)
        self.browser_frame.setFrameShadow(QFrame.Raised)
        self.whatsapp_label = QLabel(self.browser_frame)
        self.whatsapp_label.setObjectName(u"whatsapp_label")
        self.whatsapp_label.setGeometry(QRect(405, 170, 150, 150))
        self.whatsapp_label.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);")
        self.whatsapp_label.setPixmap(
            QPixmap(u"assets/icons/main/whatsapp.png"))
        self.whatsapp_label.setScaledContents(True)
        self.label_8 = QLabel(self.browser_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(65, 44, 391, 51))
        self.label_8.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);")
        self.stackedWidget.addWidget(self.load_browser)
        self.load_qr = QWidget()
        self.load_qr.setObjectName(u"load_qr")
        self.load_qr.setMinimumSize(QSize(960, 540))
        self.load_qr.setMaximumSize(QSize(960, 540))
        self.label_4 = QLabel(self.load_qr)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(405, 170, 150, 150))
        self.label_4.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);")
        self.label_4.setPixmap(QPixmap(u"assets/icons/main/whatsapp.png"))
        self.label_4.setScaledContents(True)
        self.label_5 = QLabel(self.load_qr)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(65, 44, 461, 51))
        self.label_6 = QLabel(self.load_qr)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(65, 379, 301, 31))
        self.start_qr_button = QPushButton(self.load_qr)
        self.start_qr_button.setObjectName(u"start_qr_button")
        self.start_qr_button.setGeometry(QRect(365, 431, 230, 50))
        self.start_qr_button.setFont(font)
        self.start_qr_button.setStyleSheet(u"QPushButton{\n"
                                           "	background-color: rgb(79, 117, 255);\n"
                                           "border-radius: 20px;\n"
                                           "color: white;\n"
                                           "}\n"
                                           "QPushButton:hover{\n"
                                           "	background-color: rgb(76, 163, 255);\n"
                                           "}\n"
                                           "QPushButton:pressed{\n"
                                           "background-color: rgb(79, 117, 255);\n"
                                           "}")
        self.stackedWidget.addWidget(self.load_qr)
        self.main_run = QWidget()
        self.main_run.setObjectName(u"main_run")
        self.main_run.setMinimumSize(QSize(960, 540))
        self.main_run.setMaximumSize(QSize(960, 540))
        self.main_run_frame = QFrame(self.main_run)
        self.main_run_frame.setObjectName(u"main_run_frame")
        self.main_run_frame.setGeometry(QRect(0, 0, 960, 540))
        self.main_run_frame.setMinimumSize(QSize(960, 540))
        self.main_run_frame.setMaximumSize(QSize(960, 540))
        self.main_run_frame.setAutoFillBackground(False)
        self.main_run_frame.setStyleSheet(
            u"background-color: rgb(66, 66, 66);")
        self.main_run_frame.setFrameShape(QFrame.StyledPanel)
        self.main_run_frame.setFrameShadow(QFrame.Sunken)
        self.label_10 = QLabel(self.main_run_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(65, 44, 391, 51))
        self.label_10.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);")
        self.message_text_2 = QTextEdit(self.main_run_frame)
        self.message_text_2.setObjectName(u"message_text_2")
        self.message_text_2.setGeometry(QRect(65, 100, 830, 64))
        self.message_text_2.setAutoFillBackground(True)
        self.message_text_2.setStyleSheet(u"resize:none;\n"
                                          "color: black;\n"
                                          "background-color: rgb(217, 217, 217);")
        self.message_text_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.message_text_2.setTabChangesFocus(False)
        self.stop_button = QPushButton(self.main_run_frame)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(133, 428, 45, 45))
        self.stop_button.setFont(font)
        self.stop_button.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);")
        icon = QIcon()
        icon.addFile(u"assets/icons/main/boton-detener.png",
                     QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.stop_button.setIcon(icon)
        self.stop_button.setIconSize(QSize(45, 45))
        self.stop_button.setFlat(True)
        self.tableWidget_2 = QTableWidget(self.main_run_frame)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(190, 191, 578, 216))
        sizePolicy.setHeightForWidth(
            self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy)
        self.tableWidget_2.setMaximumSize(QSize(2000, 2000))
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "gridline-color: rgb(0,206,151);\n"
                                         "font-size: 12px;\n"
                                         "}\n"
                                         "QHeaderView::section{\n"
                                         "	background-color: rgb(46, 112, 255);\n"
                                         "border: 1px solid rgb(0,0,0);\n"
                                         "font-size: 12px;\n"
                                         "}\n"
                                         "QTableWidget:QTableCornerButton::section{\n"
                                         "	background-color: rgb(0,0,0);\n"
                                         "border: 1px solid rgb(0,206,151);\n"
                                         "}")
        self.tableWidget_2.setFrameShadow(QFrame.Raised)
        self.tableWidget_2.horizontalHeader().setVisible(True)
        self.tableWidget_2.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_2.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(199)
        self.tableWidget_2.horizontalHeader().setHighlightSections(True)
        self.tableWidget_2.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_2.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_2.verticalHeader().setVisible(True)
        self.progressBar = QProgressBar(self.main_run_frame)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(194, 429, 572, 44))
        self.progressBar.setValue(24)
        self.stackedWidget.addWidget(self.main_run)
        self.finish = QWidget()
        self.finish.setObjectName(u"finish")
        self.finish.setMinimumSize(QSize(960, 540))
        self.finish.setMaximumSize(QSize(960, 540))
        self.finish_frame = QFrame(self.finish)
        self.finish_frame.setObjectName(u"finish_frame")
        self.finish_frame.setGeometry(QRect(0, 0, 960, 540))
        self.finish_frame.setMinimumSize(QSize(960, 540))
        self.finish_frame.setMaximumSize(QSize(960, 540))
        self.finish_frame.setAutoFillBackground(False)
        self.finish_frame.setStyleSheet(u"background-color: rgb(66, 66, 66);")
        self.finish_frame.setFrameShape(QFrame.StyledPanel)
        self.finish_frame.setFrameShadow(QFrame.Sunken)
        self.label_11 = QLabel(self.finish_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(65, 44, 391, 51))
        self.label_11.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);")
        self.tableWidget_3 = QTableWidget(self.finish_frame)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(180, 150, 578, 216))
        sizePolicy.setHeightForWidth(
            self.tableWidget_3.sizePolicy().hasHeightForWidth())
        self.tableWidget_3.setSizePolicy(sizePolicy)
        self.tableWidget_3.setMaximumSize(QSize(2000, 2000))
        self.tableWidget_3.setStyleSheet(u"QTableWidget{\n"
                                         "	background-color: rgb(255, 255, 255);\n"
                                         "gridline-color: rgb(0,206,151);\n"
                                         "font-size: 12px;\n"
                                         "}\n"
                                         "QHeaderView::section{\n"
                                         "	background-color: rgb(46, 112, 255);\n"
                                         "border: 1px solid rgb(0,0,0);\n"
                                         "font-size: 12px;\n"
                                         "}\n"
                                         "QTableWidget:QTableCornerButton::section{\n"
                                         "	background-color: rgb(0,0,0);\n"
                                         "border: 1px solid rgb(0,206,151);\n"
                                         "}")
        self.tableWidget_3.setFrameShadow(QFrame.Raised)
        self.tableWidget_3.horizontalHeader().setVisible(True)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(199)
        self.tableWidget_3.horizontalHeader().setHighlightSections(True)
        self.tableWidget_3.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_3.verticalHeader().setVisible(True)
        self.restar_button = QPushButton(self.finish_frame)
        self.restar_button.setObjectName(u"restar_button")
        self.restar_button.setGeometry(QRect(602, 417, 230, 50))
        self.restar_button.setFont(font)
        self.restar_button.setStyleSheet(u"QPushButton{\n"
                                         "	background-color: rgb(79, 117, 255);\n"
                                         "border-radius: 20px;\n"
                                         "color: white;\n"
                                         "}\n"
                                         "QPushButton:hover{\n"
                                         "	background-color: rgb(76, 163, 255);\n"
                                         "}\n"
                                         "QPushButton:pressed{\n"
                                         "background-color: rgb(79, 117, 255);\n"
                                         "}")
        self.close_button = QPushButton(self.finish_frame)
        self.close_button.setObjectName(u"close_button")
        self.close_button.setGeometry(QRect(162, 417, 230, 50))
        self.close_button.setFont(font)
        self.close_button.setStyleSheet(u"QPushButton{\n"
                                        "	background-color: rgb(79, 117, 255);\n"
                                        "border-radius: 20px;\n"
                                        "color: white;\n"
                                        "}\n"
                                        "QPushButton:hover{\n"
                                        "	background-color: rgb(76, 163, 255);\n"
                                        "}\n"
                                        "QPushButton:pressed{\n"
                                        "background-color: rgb(79, 117, 255);\n"
                                        "}")
        self.stackedWidget.addWidget(self.finish)
        self.error = QWidget()
        self.error.setObjectName(u"error")
        self.label_12 = QLabel(self.error)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(65, 44, 391, 51))
        self.label_12.setStyleSheet(
            u"background-color: rgba(255, 255, 255, 0);")
        self.error_frame = QFrame(self.error)
        self.error_frame.setObjectName(u"error_frame")
        self.error_frame.setGeometry(QRect(65, 110, 801, 301))
        self.error_frame.setFrameShape(QFrame.StyledPanel)
        self.error_frame.setFrameShadow(QFrame.Raised)
        self.stackedWidget.addWidget(self.error)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head><body><p><span style=\" font-size:18pt; color:#ffffff;\">Elija la columna en la que se encuentran los n\u00fameros de tel\u00e9fono</span></p></body></html>", None))
        self.radioButton.setText(QCoreApplication.translate(
            "MainWindow", u"RadioButton", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Elija las columnas que ser\u00e1n visibles en la pr\u00f3xima tabla</span></p></body></html>", None))
        self.checkBox.setText(QCoreApplication.translate(
            "MainWindow", u"CheckBox", None))
        self.start_button_3.setText(
            QCoreApplication.translate("MainWindow", u"Continuar", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Ingrese el mensaje que se enviar\u00e1</span></p></body></html>", None))
        self.message_text.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Ingrese el texto que mandara.", None))
        self.start_main_button.setText(
            QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.whatsapp_label.setText("")
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Abriendo Whatsapp Web</span></p></body></html>", None))
        self.label_4.setText("")
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Escanear el c\u00f3digo QR de Whatsapp Web</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Una vez escaneado, presionar continuar.</span></p></body></html>", None))
        self.start_qr_button.setText(
            QCoreApplication.translate("MainWindow", u"Continuar", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Enviando mensajes</span></p></body></html>", None))
        self.message_text_2.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                               "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                               "p, li { white-space: pre-wrap; }\n"
                                                               "</style></head><body style=\" font-family:'Noto Sans'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                               "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Texto mandado</p></body></html>", None))
        self.message_text_2.setPlaceholderText(QCoreApplication.translate(
            "MainWindow", u"Ingrese el texto que mandara.", None))
        self.stop_button.setText("")
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">Mensajes enviados</span></p></body></html>", None))
        self.restar_button.setText(
            QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.close_button.setText(
            QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_12.setText(QCoreApplication.translate(
            "MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt; color:#ffffff;\">!Ha ocurrido un error!</span></p></body></html>", None))
    # retranslateUi
