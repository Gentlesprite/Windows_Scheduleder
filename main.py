# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2025/2/23 12:15
# File:main.py
import sys
import subprocess
import traceback
import threading
import logging
from datetime import datetime, timedelta

from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction

from module.ui import *
from module.black_mode import restore_mode, night_mode


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUi()
        self.m_flag = False
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.band()
        self.paths = ""
        self.textBrowser = QTextBrowser()
        self.setAcceptDrops(True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 背景透明
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.timer = QTimer()  # 创建 QTimer 实例
        self.timer.timeout.connect(self.updateTime)  # 将 QTimer 的超时信号与 update_time 函数连接起来
        self.start_time = None  # 添加这一行
        self.is_on_top = False  # 新增一个属性 is_on_top
        self.moveToCenterDisplay()
        self.clear_label_timer = QTimer(self)
        self.clear_label_timer.setSingleShot(True)  # 只触发一次
        self.clear_label_timer.timeout.connect(self.clearLabels)

    def initUi(self):
        self.moveToCenterDisplay()
        self.trayMenus()

    def band(self):
        '''
        self.ui.___ACTION___.triggered.connect(___FUNCTION___)
        self.ui.___BUTTON___.clicked.connect(___FUNCTION___)
        self.ui.___CCMB_BOX___.currentIndexChanged  .connect(___FUNCTION___)
        self.ui.___SPIN_BOX___.valueChanged.connect(___FUNCTION___)
        #自定义信号，属性名.connect(___FUNCTION___)
        '''
        self.ui.button_shutdwon.clicked.connect(self.shutdownTask)
        self.ui.button_cancel_shutdown.clicked.connect(self.cancelShutdownTask)
        self.ui.button_quit.clicked.connect(self.softwareExit)
        self.ui.button_mini.clicked.connect(self.softwareMinisize)
        self.ui.button_keep_top.clicked.connect(self.softwareKeepTopMode)
        self.ui.checkBox_auto_keep_top.stateChanged.connect(self.updateCheckBoxState)
        self.ui.checkBox_close_windows_tips.stateChanged.connect(self.updateCheckBoxState)
        self.ui.checkBox_night_mode.stateChanged.connect(self.updateCheckBoxState)
        self.ui.checkBox_show_taskbar.stateChanged.connect(self.toggleTaskbar)

    def toggleTaskbar(self):
        if not self.tray_show_taskbar.isChecked() and self.ui.checkBox_show_taskbar.isChecked():
            self.tray_show_taskbar.setChecked(True)
        toggle_taskbar()

    def softwareExit(self):
        try:
            self.close()
        except Exception as e:
            logging.error(f"关闭窗口时出现异常：{e}")
            logging.error(traceback.format_exc())
        finally:
            try:
                restore_mode()  # 退出软件进行恢复操作,以免对用户造成不必要麻烦
            except NameError:
                print("当前无需执行恢复操作")  # 处理对软件打开没有任何操作就关闭软件的报错情况
            finally:
                sys.exit()

    # 最小化
    def softwareMinisize(self):
        self.showMinimized()

    def trayMenus(self):  # 定义任务栏右边的图标
        # 加载 UI 文件
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        # 创建系统托盘图标和菜单
        tray_icon = QSystemTrayIcon(QIcon(':logo.ico'), self)
        tray_menu = QMenu(self)

        # 初始化 checkBox 状态

        self.ui.checkBox_night_mode.setChecked(True)
        self.ui.checkBox_auto_keep_top.setChecked(True)
        self.ui.checkBox_close_windows_tips.setChecked(True)
        self.ui.checkBox_show_taskbar.setChecked(True)
        self.tray_complex = {}
        self.tray_night_mode = QAction('夜间模式', self, checkable=True, data=self.ui.checkBox_night_mode)
        self.tray_complex['夜间模式'] = self.tray_night_mode

        self.tray_auto_keep_top = QAction('移至右上置顶', self, checkable=True, data=self.ui.checkBox_auto_keep_top)
        self.tray_complex["移至右上置顶"] = self.tray_auto_keep_top

        self.tray_show_taskbar = QAction('显示任务栏', self, checkable=True, data=self.ui.checkBox_show_taskbar)
        self.tray_complex['显示任务栏'] = self.tray_show_taskbar

        self.tray_close_windows_tips = QAction('关闭弹窗提示', self, checkable=True,
                                               data=self.ui.checkBox_close_windows_tips)
        self.tray_complex['关闭弹窗提示'] = self.tray_close_windows_tips

        # 初始化sub状态
        self.tray_night_mode.setChecked(True)
        self.tray_auto_keep_top.setChecked(True)
        self.tray_show_taskbar.setChecked(True)
        self.tray_close_windows_tips.setChecked(True)

        # 绑定菜单动作的 `triggered` 信号
        self.tray_night_mode.triggered.connect(self.updateCheckBoxState)
        self.tray_auto_keep_top.triggered.connect(self.updateCheckBoxState)
        self.tray_show_taskbar.triggered.connect(
            lambda: (special_hide_taskbar(self)))
        self.tray_close_windows_tips.triggered.connect(self.updateCheckBoxState)
        # 创建菜单项并添加到菜单
        sub_menu = QMenu("Sub Menu")
        sub_menu.addAction(self.tray_night_mode)
        sub_menu.addAction(self.tray_auto_keep_top)
        sub_menu.addAction(self.tray_show_taskbar)
        sub_menu.addAction(self.tray_close_windows_tips)

        checkbox_action = QAction("配置选项", self, checkable=True)
        checkbox_action.setMenu(sub_menu)
        tray_menu.addAction(checkbox_action)

        show_action = QAction("隐藏/显示", self)
        exit_action = QAction("关闭", self)
        shutdown_action = QAction("关机(当前配置)", self)
        cancel_shutdown_action = QAction("取消关机(当前配置)", self)
        tray_menu.addSeparator()
        tray_menu.addAction(shutdown_action)
        tray_menu.addAction(cancel_shutdown_action)
        tray_menu.addSeparator()
        tray_menu.addAction(show_action)
        tray_menu.addSeparator()
        tray_menu.addAction(exit_action)

        # 将菜单设置为系统托盘图标的上下文菜单
        tray_icon.setContextMenu(tray_menu)

        # 单击系统托盘图标时切换窗口显示/隐藏状态
        show_action.triggered.connect(lambda: self.show() if self.isHidden() else self.hide())
        cancel_shutdown_action.triggered.connect(self.cancelShutdownTask)
        shutdown_action.triggered.connect(self.shutdownTask)

        # 单击菜单项"Exit"时退出应用程序
        exit_action.triggered.connect(lambda: QApplication.quit())

        # 显示系统托盘图标并调整窗口大小
        tray_icon.show()
        # 定义一个成员方法来更新复选框状态

        # 点击任务栏图标显示应用程序窗口
        tray_icon.activated.connect(lambda
                                        reason: self.showNormal() if self.isMinimized() and reason == QSystemTrayIcon.Trigger else self.show() if self.isHidden() and reason == QSystemTrayIcon.Trigger else self.activateWindow() if reason == QSystemTrayIcon.Trigger else None)

    def softwareKeepTopMode(self):
        if self.is_on_top:
            # 使用 WinAPI 取消窗口置顶
            hwnd = self.winId()
            HWND_NOTOPMOST = -2
            SWP_NOMOVE = 0x0002
            SWP_NOSIZE = 0x0001
            flags = SWP_NOMOVE | SWP_NOSIZE
            ctypes.windll.user32.SetWindowPos(hwnd, HWND_NOTOPMOST, 0, 0, 0, 0, flags)

            # 修改按钮文本
            self.ui.button_keep_top.setText('♙')

            # 更新 is_on_top 属性
            self.is_on_top = False
        else:
            # 使用 WinAPI 设置窗口置顶
            hwnd = self.winId()
            HWND_TOPMOST = -1
            SWP_NOMOVE = 0x0002
            SWP_NOSIZE = 0x0001
            flags = SWP_NOMOVE | SWP_NOSIZE
            ctypes.windll.user32.SetWindowPos(hwnd, HWND_TOPMOST, 0, 0, 0, 0, flags)

            # 修改按钮文本
            self.ui.button_keep_top.setText('♟')

            # 更新 is_on_top 属性
            self.is_on_top = True

        # 重新显示窗口
        self.show()
        # 更新属性 is_on_top 的值

    # 重写鼠标事件
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def clearLabels(self):  # 清除软件上的提示框内容信息
        self.ui.label.clear()

    def tipsEvent(self, chose):
        if chose == 1:
            tips = QMessageBox.information(self, '提示',
                                           '你的电脑将在{}小时后关机！'.format(int(self.changeTime() / 3600)))
            return tips
        elif chose == 2:
            tips = QMessageBox.information(self, f'提示', '关机任务已取消！')
            return tips
        elif chose == 3:
            tips = QMessageBox.information(self, f'提示', '当前没有关机任务')
            return tips

    def updateCheckBoxState(self):
        sender_action = self.sender()
        text = sender_action.text()
        checkbox_list = [self.ui.checkBox_auto_keep_top, self.ui.checkBox_night_mode,
                         self.ui.checkBox_close_windows_tips]

        for checkbox in checkbox_list:
            if checkbox.text() == text:
                checkbox.setChecked(sender_action.isChecked())
                break
        if text in self.tray_complex:
            if sender_action.isChecked():
                self.tray_complex[text].setChecked(True)
            else:
                self.tray_complex[text].setChecked(False)

    def changeTime(self):
        time = self.ui.spinBox.value()
        unit = self.ui.comboBox.currentText()  # 获取 comboBox 中选中的单位
        if unit == "分":
            time *= 60
        elif unit == "时":
            time *= 60 * 60
        else:
            pass
        int_time = int(time)
        return int_time

    def beginTimer(self):
        self.timer.start(1000)
        self.start_time = datetime.now()  # 添加这一行

    def setBlackWallpaper(self):
        # 定义 SPI_SETDESKWALLPAPER 常量
        SPI_SETDESKWALLPAPER = 20
        # 设置黑色背景颜色值（请注意顺序：红、绿、蓝）
        black_color_value = "0 0 0"
        # 调用 SystemParametersInfo 函数设置桌面背景为纯黑色
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, black_color_value, 0)
        print("桌面背景已切换为黑色")

    def moveToRightAndUpDisplay(self):
        # 将窗口移动到右上角
        screens = QApplication.screens()  # 获取所有屏幕对象
        primary_screen = QApplication.primaryScreen()  # 获取主屏幕索引
        primary_screen_index = screens.index(primary_screen)  # 获取主屏幕索引在列表中的位置
        screen_rect = screens[primary_screen_index].geometry()  # 获取主屏幕几何信息
        window_rect = self.geometry()
        x = screen_rect.width() - window_rect.width()
        y = 0
        self.default_pos = (x, y)  # 记录窗口的默认位置
        self.setGeometry(x, y, window_rect.width(), window_rect.height())

    def moveToCenterDisplay(self):
        # 将窗口居中显示

        screens = QApplication.screens()  # 获取所有屏幕对象
        primary_screen = QApplication.primaryScreen()  # 获取主屏幕索引
        primary_screen_index = screens.index(primary_screen)  # 获取主屏幕索引在列表中的位置
        screen_rect = screens[primary_screen_index].geometry()  # 获取主屏幕几何信息

        window_rect = self.geometry()
        x = (screen_rect.width() - window_rect.width()) / 2
        y = (screen_rect.height() - window_rect.height()) / 2
        self.default_pos = (x, y)  # 记录窗口的默认位置
        self.setGeometry(x, y, window_rect.width(), window_rect.height())

    def shutdownTask(self):
        # 获取关机时间
        global shutdown_time, shutdown_time_str
        shutdown_time = datetime.now() + timedelta(seconds=self.changeTime())

        # 提示关机时间和当前时间
        current_time_str = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        shutdown_time_str = shutdown_time.strftime('%Y/%m/%d %H:%M:%S')
        shutdown_min = self.changeTime() // 60
        msg = f"当前时间：{current_time_str}\n预计关机时间：{shutdown_time_str}\n剩余时间：{shutdown_min}分钟"
        subprocess.call(f'shutdown -s -t {self.changeTime()}', shell=True)
        if not self.ui.checkBox_close_windows_tips.isChecked():
            QMessageBox.information(self, '提示', msg)
        self.beginTimer()
        if self.ui.checkBox_auto_keep_top.isChecked():
            self.moveToRightAndUpDisplay()
            if not self.is_on_top:  # 如果当前不是置顶状态
                self.softwareKeepTopMode()  # 切换为置顶状态
        if self.ui.checkBox_night_mode.isChecked():
            night_mode()
        if self.ui.checkBox_show_taskbar.isChecked():  # 任务栏隐藏
            self.ui.checkBox_show_taskbar.setChecked(False)
            toggle_taskbar()

        return 1

    def cancelShutdownTask(self):
        try:
            if subprocess.call('shutdown -a', shell=True) == 0:
                msg_cancel_task = '关机任务已取消!'
                if not self.ui.checkBox_close_windows_tips.isChecked():
                    QMessageBox.information(self, f'提示', msg_cancel_task)
                if self.ui.checkBox_auto_keep_top.isChecked():
                    self.moveToCenterDisplay()
                    if self.is_on_top:  # 如果当前是置顶状态
                        self.softwareKeepTopMode()  # 切换为非置顶状态
                    self.ui.label.setText('    ' + msg_cancel_task)
                if not self.ui.checkBox_show_taskbar.isChecked():
                    if not self.ui.checkBox_show_taskbar.checkState():
                        self.ui.checkBox_show_taskbar.setChecked(True)
                    show_taskbar()

                # 在新线程中执行还原壁纸操作
                restore_thread = threading.Thread(target=restore_mode)
                restore_thread.start()
                self.timer.stop()
            else:
                raise Exception("因为没有任何进行中的关机过程，所以无法中止系统关机。(1116)")
        except Exception as e:
            if "1116" in str(e):
                msg_no_task = '当前没有关机任务!'
                if not self.ui.checkBox_close_windows_tips.isChecked():
                    QMessageBox.information(self, f'提示', msg_no_task)
                else:
                    self.ui.label.setText('    ' + msg_no_task)
            else:
                traceback.print_exc()
        finally:
            # 启动一个定时器，在 3 秒后清除标签
            self.clear_label_timer.start(3000)

    def updateTime(self):
        current_time_str = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        remaining_time = (shutdown_time - datetime.now()).total_seconds()
        if remaining_time < 0:
            remaining_time = 0
        remaining_min = int(remaining_time // 60)
        remaining_sec = int(remaining_time % 60)
        msg = f"当前时间：{current_time_str}\n预计关机时间：{shutdown_time_str}\n剩余时间：{remaining_min}分{remaining_sec}秒"
        self.ui.label.setText(msg)


if __name__ == '__main__':
    app = QApplication([])
    app.setWindowIcon(QIcon(':logo.ico'))
    window = MainWindow()
    window.show()
    app.exec_()
