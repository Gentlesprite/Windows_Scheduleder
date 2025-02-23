# coding=UTF-8
# Author:Gentlesprite
# Software:PyCharm
# Time:2025/2/23 12:55
# File:build.py
import os
import shutil

software_name = 'scheduleder'
main = 'main.py'
icon_path = r'module\resources\logo.ico'
upx_dir = r'module\bin\upx.exe'
version_file = os.path.join(os.getcwd(), 'file_version_info.txt')
if __name__ == '__main__':
    try:
        import PyInstaller.__main__

        PyInstaller.__main__.run([
            '--upx-dir', upx_dir,
            '-F',
            '-w',
            '-i', icon_path,
            '--version-file', version_file,
            '--name', software_name,
            main
        ])
    except ImportError:
        print('使用pip install pyinstaller安装pyinstaller后重试。')
    finally:
        build_dir = os.path.join(os.getcwd(), 'build')
        if os.path.exists(build_dir):
            shutil.rmtree(build_dir)
