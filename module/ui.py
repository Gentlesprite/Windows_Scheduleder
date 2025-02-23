# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowsjznfuf.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(432, 272)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(4000, 400))
        font = QFont()
        font.setPointSize(9)
        Form.setFont(font)
        Form.setStyleSheet(u"")
        Form.setInputMethodHints(Qt.ImhNone)
        self.button_shutdwon = QPushButton(Form)
        self.button_shutdwon.setObjectName(u"button_shutdwon")
        self.button_shutdwon.setGeometry(QRect(40, 180, 151, 71))
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.button_shutdwon.sizePolicy().hasHeightForWidth())
        self.button_shutdwon.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setFamily(u"\u9ed1\u4f53")
        font1.setPointSize(20)
        font1.setBold(False)
        font1.setWeight(50)
        self.button_shutdwon.setFont(font1)
        self.button_shutdwon.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(111, 111, 111);\n"
"border-radius:15px; \n"
"color:rgb(0, 0, 0);}\n"
"QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(130, 130, 130, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{padding-top:7px;\n"
"padding-left:7px;}")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 50, 191, 91))
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setFont(font1)
        self.label_2.setFocusPolicy(Qt.NoFocus)
        self.label_2.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.bkgd = QLabel(Form)
        self.bkgd.setObjectName(u"bkgd")
        self.bkgd.setGeometry(QRect(0, 0, 431, 271))
        self.bkgd.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 255));\n"
"border-top-right-radius: 25px;\n"
"border-bottom-right-radius: 25px;\n"
"border-top-left-radius: 25px;\n"
"border-bottom-left-radius: 25px")
        self.bkgd.setFrameShape(QFrame.StyledPanel)
        self.button_mini = QPushButton(Form)
        self.button_mini.setObjectName(u"button_mini")
        self.button_mini.setGeometry(QRect(330, 10, 41, 41))
        font2 = QFont()
        font2.setFamily(u"Arial")
        font2.setPointSize(13)
        self.button_mini.setFont(font2)
        self.button_mini.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 255, 0);\n"
"border-radius:15px; \n"
"color:rgb(0, 0, 0);}\n"
"QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(16, 136, 47, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{padding-top:7px;\n"
"padding-left:7px;}")
        self.button_quit = QPushButton(Form)
        self.button_quit.setObjectName(u"button_quit")
        self.button_quit.setGeometry(QRect(380, 10, 41, 41))
        font3 = QFont()
        font3.setFamily(u"Arial")
        font3.setPointSize(9)
        self.button_quit.setFont(font3)
        self.button_quit.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 0 , 0);\n"
"border-radius:15px; \n"
"color:rgb(0, 0, 0);}\n"
"QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{padding-top:7px;\n"
"padding-left:7px;}")
        self.button_cancel_shutdown = QPushButton(Form)
        self.button_cancel_shutdown.setObjectName(u"button_cancel_shutdown")
        self.button_cancel_shutdown.setGeometry(QRect(230, 180, 151, 71))
        sizePolicy1.setHeightForWidth(self.button_cancel_shutdown.sizePolicy().hasHeightForWidth())
        self.button_cancel_shutdown.setSizePolicy(sizePolicy1)
        font4 = QFont()
        font4.setFamily(u"\u9ed1\u4f53")
        font4.setPointSize(20)
        font4.setBold(False)
        font4.setItalic(False)
        font4.setWeight(50)
        self.button_cancel_shutdown.setFont(font4)
        self.button_cancel_shutdown.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(111, 111, 111);\n"
"border-radius:15px; \n"
"color:rgb(0, 0, 0);}\n"
"QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(130, 130, 130, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{padding-top:7px;\n"
"padding-left:7px;}")
        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(210, 70, 91, 51))
        font5 = QFont()
        font5.setFamily(u"\u9ed1\u4f53")
        font5.setPointSize(20)
        self.spinBox.setFont(font5)
        self.spinBox.setStyleSheet(u"\n"
"QSpinBox\n"
"{\n"
"	border:1px solid #242424;\n"
"border-radius:15px; \n"
"background-color: rgb(111, 111, 111);\n"
"}\n"
" \n"
"QSpinBox::up-button,QDoubleSpinBox::down-button::QDoubleSpinBox::vaule\n"
"{\n"
"	width:0px;\n"
"	vaule:none;\n"
"}\n"
"QSpinBox::up-button, QSpinBox::down-button {\n"
"    width: 0px;\n"
"}")
        self.spinBox.setMaximum(9999)
        self.spinBox.setStepType(QAbstractSpinBox.DefaultStepType)
        self.spinBox.setValue(240)
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(310, 70, 71, 51))
        self.comboBox.setFont(font5)
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    border: 1px solid #242424;\n"
"    border-radius: 15px;\n"
"    background-color: rgb(111, 111, 111);\n"
"}\n"
"")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 271, 91))
        font6 = QFont()
        font6.setFamily(u"\u9ed1\u4f53")
        font6.setPointSize(8)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.button_keep_top = QPushButton(Form)
        self.button_keep_top.setObjectName(u"button_keep_top")
        self.button_keep_top.setGeometry(QRect(280, 10, 41, 41))
        self.button_keep_top.setFont(font2)
        self.button_keep_top.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(255, 255, 0);\n"
"border-radius:15px; \n"
"color:rgb(0, 0, 0);}\n"
"QPushButton:hover{background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(255, 255, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:pressed{padding-top:7px;\n"
"padding-left:7px;}")
        self.checkBox_auto_keep_top = QCheckBox(Form)
        self.checkBox_auto_keep_top.setObjectName(u"checkBox_auto_keep_top")
        self.checkBox_auto_keep_top.setEnabled(True)
        self.checkBox_auto_keep_top.setGeometry(QRect(230, 130, 241, 16))
        font7 = QFont()
        font7.setFamily(u"\u9ed1\u4f53")
        font7.setPointSize(9)
        self.checkBox_auto_keep_top.setFont(font7)
        self.checkBox_auto_keep_top.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.checkBox_auto_keep_top.setChecked(True)
        self.checkBox_close_windows_tips = QCheckBox(Form)
        self.checkBox_close_windows_tips.setObjectName(u"checkBox_close_windows_tips")
        self.checkBox_close_windows_tips.setGeometry(QRect(230, 150, 181, 16))
        self.checkBox_close_windows_tips.setFont(font7)
        self.checkBox_close_windows_tips.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.checkBox_close_windows_tips.setChecked(True)
        self.checkBox_night_mode = QCheckBox(Form)
        self.checkBox_night_mode.setObjectName(u"checkBox_night_mode")
        self.checkBox_night_mode.setEnabled(True)
        self.checkBox_night_mode.setGeometry(QRect(100, 130, 121, 16))
        self.checkBox_night_mode.setFont(font7)
        self.checkBox_night_mode.setStyleSheet(u"color:rgb(255, 255, 255);")
        self.checkBox_night_mode.setChecked(False)
        self.bkgd.raise_()
        self.button_shutdwon.raise_()
        self.label_2.raise_()
        self.button_quit.raise_()
        self.button_mini.raise_()
        self.button_cancel_shutdown.raise_()
        self.spinBox.raise_()
        self.comboBox.raise_()
        self.label.raise_()
        self.button_keep_top.raise_()
        self.checkBox_auto_keep_top.raise_()
        self.checkBox_close_windows_tips.raise_()
        self.checkBox_night_mode.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u8ba1\u5212\u5173\u673a", None))
        self.button_shutdwon.setText(QCoreApplication.translate("Form", u"\u5173\u673a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5173\u673a\u65f6\u95f4", None))
        self.bkgd.setText("")
        self.button_mini.setText(QCoreApplication.translate("Form", u"\ufe63", None))
        self.button_quit.setText(QCoreApplication.translate("Form", u"\u00d7", None))
        self.button_cancel_shutdown.setText(QCoreApplication.translate("Form", u"\u53d6\u6d88", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u5206", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u65f6", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"\u79d2", None))

        self.label.setText("")
        self.button_keep_top.setText(QCoreApplication.translate("Form", u"\u2659", None))
        self.checkBox_auto_keep_top.setText(QCoreApplication.translate("Form", u"\u79fb\u81f3\u53f3\u4e0a\u7f6e\u9876", None))
        self.checkBox_close_windows_tips.setText(QCoreApplication.translate("Form", u"\u5173\u95ed\u5f39\u7a97\u63d0\u793a", None))
        self.checkBox_night_mode.setText(QCoreApplication.translate("Form", u"\u591c\u665a\u6a21\u5f0f", None))
    # retranslateUi

