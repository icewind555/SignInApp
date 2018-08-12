# -*- coding: utf-8 -*-

"""

Let's start the project!

Author: IceWind
Last edited: August 2018

"""
import time
import json
import os

import sys
from ui.mainwindow import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox, \
    QInputDialog, QButtonGroup, QMessageBox, QSystemTrayIcon, \
    QMenu, QAction, qApp

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QIcon

ROOT = os.path.dirname(__file__)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.bg = QButtonGroup()
        self.bg.setExclusive(False)

        self.setupUi(self)
        # -------------托盘设置-------------
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(QIcon(os.path.join(ROOT, "ui/icon/icon.png")))
        self.tray_menu = QMenu(QApplication.desktop())
        self.reAct = QAction('打开', self, triggered=self.show)
        self.quitAct = QAction('退出', self, triggered=qApp.quit)
        self.tray_menu.addAction(self.reAct)
        self.tray_menu.addAction(self.quitAct)
        self.tray.setContextMenu(self.tray_menu)
        self.tray.show()
        self.tray.activated.connect(self.icon_activated)
        # -------------托盘结束-------------
        self.load_status()
        self.init_task()
        self.show()

    # 托盘图标触发
    def icon_activated(self, reason):
        if reason == QSystemTrayIcon.DoubleClick:
            if self.isHidden():
                self.show()
            else:
                self.hide()

    # 关闭事件
    def closeEvent(self, event):
        self.statusBar().showMessage("双击右下角图标最小化")
        reply = QMessageBox.question(self, '关闭', "确定要关闭应用吗？", QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    # 添加日程
    def add_task(self):
        text, ok = QInputDialog.getText(self, '添加日程', "请输入要添加的日程")
        cb = QCheckBox(text, self)
        if ok:
            self.bg.addButton(cb, -1)
            self.verticalLayout.addWidget(cb, 0, Qt.AlignCenter)
            task[text] = False

            reply = QMessageBox.question(self, '添加提醒', "是否要添加时间提醒？",
                                         QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            if reply == QMessageBox.Yes:
                self.notify()

    # 删除日程
    def delete_task(self):
        text, ok = QInputDialog.getText(self, '删除日程', "请输入要删除的日程")
        if ok:
            if text in task:
                task.pop(text)
                self.setupUi(self)
                self.init_task()
            else:
                QMessageBox.warning(self, "警告", "该日程不存在！")

    # 设置提醒时间
    def notify(self):
        hour, ok1 = QInputDialog.getInt(self, "设置小时", "请输入小时：", 12, 0, 24, 1)
        if ok1:
            minute, ok2 = QInputDialog.getInt(self, "设置分钟", "请输入分钟：", 00, 0, 59, 1)
            if ok2:
                timer = QTimer(self)
                timer.setSingleShot(True)
                h = int(time.strftime("%H", time.localtime()))
                m = int(time.strftime("%M", time.localtime()))
                if minute < m:
                    hour -= 1
                    minute += 60
                if hour < h:
                    QMessageBox.warning(self, "警告", "设置的时间有误！")
                else:
                    interval = ((hour-h)*3600 + (minute-m)*60)*1000
                    # print(interval)
                    timer.start(interval)
                    timer.timeout.connect(self.pop_up)

    # 消息弹窗
    def pop_up(self):
        # print("弹窗呢")
        self.tray.showMessage("任务提醒", "是时候去打卡了！")

    # 重置界面
    def cls(self):

        reply = QMessageBox.question(self, '重置', "你真的要重置吗？（保存的日程文件也会删除）",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.setupUi(self)
            # self.show()
            os.remove("data.json")

    # 保存数据
    def save_status(self):
        for btn in self.bg.buttons():
            if btn.isChecked():
                task[btn.text()] = True
            else:
                task[btn.text()] = False

        with open("data.json", "w") as f:
            json.dump(task, f)
            # print("储存成功")

    # 初始化日程
    def init_task(self):
        for text, status in task.items():
            cb = QCheckBox(text, self)
            self.bg.addButton(cb, -1)
            cb.setChecked(status)
            self.verticalLayout.addWidget(cb, 0, Qt.AlignCenter)

    # 读取json数据
    @staticmethod
    def load_status():
        if os.path.exists("data.json"):
            with open("data.json", 'r') as load_f:
                task.update(json.load(load_f))
                # self.init_task()
                # print(task)

    # TODO 统计数据


if __name__ == '__main__':
    task = {}
    app = QApplication(sys.argv)
    SignIn = MainWindow()
    sys.exit(app.exec_())
