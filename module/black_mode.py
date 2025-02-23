import ctypes
import os
import win32api
import win32con
import win32gui
from PySide2 import QtWidgets

taskbar_status = True  # 初始状态为显示任务栏


def wallpaper_functions(mode):
    global wallpaper_path

    # 获取当前用户的个人文件夹路径
    user_folder = os.path.expanduser('~')

    if mode == 'save':
        # 获取当前桌面壁纸路径
        key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_READ)
        wallpaper_path = win32api.RegQueryValueEx(key, "WallPaper")[0]
        win32api.RegCloseKey(key)

        print(f"壁纸 {wallpaper_path} 已保存")

        # 复制壁纸文件到个人文件夹下的Wallpapers子文件夹中
        if os.path.exists(wallpaper_path):
            wallpaper_name = os.path.basename(wallpaper_path)
            dest_path = os.path.join(user_folder, 'Wallpapers', wallpaper_name)

            # 如果目标目录不存在，则创建目录
            if not os.path.exists(os.path.dirname(dest_path)):
                os.makedirs(os.path.dirname(dest_path))

            # 复制壁纸文件到目标目录下
            if not os.path.exists(dest_path):
                os.system(f'copy "{wallpaper_path}" "{dest_path}"')

    elif mode == 'restore':
        # 获取保存的桌面壁纸文件名
        wallpaper_name = os.path.basename(wallpaper_path)
        if wallpaper_name:
            # 拼接出壁纸文件的本地路径
            wallpaper_local_path = os.path.join(user_folder, 'Wallpapers', wallpaper_name)

            if os.path.exists(wallpaper_local_path):
                # 设置桌面壁纸
                ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER, 0, wallpaper_local_path,
                                                           win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE)
                print("桌面壁纸已恢复！")
            else:
                print(f'壁纸文件 "{wallpaper_local_path}" 不存在！')
        else:
            print("未找到保存的壁纸路径，请先保存当前桌面壁纸！")


def set_black_wallpaper():
    # 定义 SPI_SETDESKWALLPAPER 常量
    SPI_SETDESKWALLPAPER = 20
    # 设置黑色背景颜色值（请注意顺序：红、绿、蓝）
    black_color_value = "0 0 0"
    # 调用 SystemParametersInfo 函数设置桌面背景为纯黑色
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, black_color_value, 0)
    print("桌面背景已切换为黑色")


def show_taskbar_rec(main_window):
    global taskbar_status
    # 获取任务栏窗口的句柄
    taskbar_hwnd = win32gui.FindWindow("Shell_traywnd", None)

    # 恢复任务栏
    win32gui.ShowWindow(taskbar_hwnd, win32con.SW_SHOW)
    taskbar_status = True  # 标记为显示任务栏
    main_window.ui.checkBox_show_taskbar.setChecked(taskbar_status)


def hide_taskbar_rec(main_window):
    global taskbar_status

    # 获取任务栏窗口的句柄
    taskbar_hwnd = win32gui.FindWindow("Shell_traywnd", None)

    # 隐藏任务栏
    win32gui.ShowWindow(taskbar_hwnd, win32con.SW_HIDE)
    taskbar_status = False  # 标记为隐藏任务栏
    main_window.ui.checkBox_show_taskbar.setChecked(taskbar_status)


def show_taskbar():
    global taskbar_status

    # 获取任务栏窗口的句柄
    taskbar_hwnd = win32gui.FindWindow("Shell_traywnd", None)

    # 恢复任务栏
    win32gui.ShowWindow(taskbar_hwnd, win32con.SW_SHOW)
    taskbar_status = True  # 标记为显示任务栏


def hide_taskbar():
    global taskbar_status

    # 获取任务栏窗口的句柄
    taskbar_hwnd = win32gui.FindWindow("Shell_traywnd", None)

    # 隐藏任务栏
    win32gui.ShowWindow(taskbar_hwnd, win32con.SW_HIDE)
    taskbar_status = False  # 标记为隐藏任务栏


def toggle_taskbar_rec(main_window):
    global taskbar_status

    if taskbar_status:
        hide_taskbar_rec(main_window)
    else:
        show_taskbar_rec(main_window)


# def special_toggle_taskbar(*text):
#     if text[0][:5] == '显示任务栏':
#         # print('翻转前的状态为', taskbar_status)
#         toggle_taskbar()
#         print('翻转后的状态为', taskbar_status)
def special_toggle_taskbar_rec(text, main_window):
    if text[:5] == '显示任务栏':
        toggle_taskbar_rec(main_window)
        print('翻转后的状态为', taskbar_status)


def tray_hide_taskbar_rec(main_window):
    main_window.ui.checkBox_show_taskbar.setChecked(False)
    hide_taskbar_rec(main_window)


def night_mode():
    wallpaper_functions('save')
    set_black_wallpaper()
    hide_taskbar()


def restore_mode():
    # 在新线程中执行还原壁纸操作
    show_taskbar()
    wallpaper_functions('restore')
