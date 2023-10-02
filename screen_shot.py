# coding: utf-8
"""
スクリーンショットをクリップボードに保存し，これをペイントに貼り付ける
"""
import os
import pyautogui
import subprocess
import time
from PIL import ImageGrab, Image
import win32clipboard


def main():
    # スクリーンショットをとる
    screen_shot = ImageGrab.grab()
    screen_shot.save('tmp.png')

    # クリップボードに保存
    os_type = os_detect()
    if os_type == 'windows':
        print("windows")
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_BITMAP, screen_shot.tobytes())
        win32clipboard.CloseClipboard()
    else:
        print("linux")
        subprocess.run(['xclip', '-selection', 'clipboard', '-t', 'image/png', '-i', 'tmp.png'])

    # ペイントを起動
    # subprocess.Popen('mspaint.exe')
    time.sleep(3)  # ペイント起動待ち

    # ペイントに貼り付け
    pyautogui.hotkey('ctrl', 'v')  # 貼り付け


def os_detect() -> str:
    """
    OSを判別する

    Returns:
        osの種類
    """
    os_name = os.name
    # windowsの場合
    if os_name == 'nt':
        return 'windows'
    # linuxの場合
    elif os_name == 'posix':
        return 'linux'
    else:
        raise ValueError('サポートしていないOSです')


if __name__ == '__main__':
    main()
