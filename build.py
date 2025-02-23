# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2025/2/23 12:55
# File:build.py
import os

main = 'main.py'
icon_path = r'module\resources\logo.ico'
upx_dir = r'D:\env\upx\upx-4.2.4-win64'  # 替换为自己的upx目录。
version_file = os.path.join(os.getcwd(), 'file_version_info.txt')
if __name__ == '__main__':
    try:
        import PyInstaller.__main__
    except ImportError:
        print('使用pip install pyinstaller安装pyinstaller后重试。')
    PyInstaller.__main__.run([
        '--upx-dir', upx_dir,
        '-F',
        '-w',
        '-i', icon_path,
        '--version-file', version_file,
        main
    ])
