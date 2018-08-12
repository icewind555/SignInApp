# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignIn.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(935, 274)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(770, 0, 160, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Upgrade = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Upgrade.setObjectName("Add")
        self.verticalLayout.addWidget(self.Upgrade, 0, QtCore.Qt.AlignTop)
        self.Delete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Delete.setObjectName("Delete")
        self.verticalLayout.addWidget(self.Delete, 0, QtCore.Qt.AlignTop)
        self.Save = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Save.setObjectName("Save")
        self.verticalLayout.addWidget(self.Save, 0, QtCore.Qt.AlignTop)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.New = QtWidgets.QAction(MainWindow)
        self.New.setShortcutVisibleInContextMenu(False)
        self.New.setObjectName("New")
        self.New.triggered.connect(MainWindow.add_task)
        self.Reset = QtWidgets.QAction(MainWindow)
        self.Reset.setObjectName("Reset")
        self.Reset.triggered.connect(MainWindow.cls)
        self.Close = QtWidgets.QAction(MainWindow)
        self.Close.setShortcutVisibleInContextMenu(False)
        self.Close.setObjectName("Close")
        self.Close.triggered.connect(QtWidgets.qApp.quit)
        self.menu.addAction(self.New)
        self.menu.addAction(self.Reset)
        self.menu.addAction(self.Close)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.Upgrade.clicked.connect(MainWindow.add_task)
        self.Delete.clicked.connect(MainWindow.delete_task)
        self.Save.clicked.connect(MainWindow.save_status)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SignIn"))
        self.Upgrade.setText(_translate("MainWindow", "添加日程"))
        self.Delete.setText(_translate("MainWindow", "删除日程"))
        self.Save.setText(_translate("MainWindow", "保存"))
        self.menu.setTitle(_translate("MainWindow", "选项"))
        self.New.setText(_translate("MainWindow", "新建"))
        self.New.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.Reset.setText(_translate("MainWindow", "重置"))
        self.Close.setText(_translate("MainWindow", "关闭"))
        self.Close.setShortcut(_translate("MainWindow", "Alt+F4"))
