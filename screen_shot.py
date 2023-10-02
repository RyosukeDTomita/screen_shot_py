# coding: utf-8
"""
windows: スクリーンショットをクリップボードに保存し，これをペイントに貼り付ける
linux: スクリーンショットをクリップボードに保存する。(ubuntuで主に開発を行ったため動作確認に使用)
"""
import os
import pyautogui
import subprocess
import time
from PIL import ImageGrab
import win32clipboard


def main():
    # スクリーンショットをとる
    screen_shot = ImageGrab.grab()
    screen_shot.save('tmp.png')

    os_type = os_detect()
    # クリップボードに保存してwindowsの場合はペイントに貼り付けるためにclip.exeを使う。
    if os_type == 'windows':
        print("windows")
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_BITMAP, screen_shot.tobytes())
        win32clipboard.CloseClipboard()
        # ペイントを起動
        subprocess.Popen('mspaint.exe')
        time.sleep(3)  # ペイント起動待ち
        # pyautogutでペイントに自動で貼り付け
        pyautogui.hotkey('ctrl', 'v')  # 貼り付け
    else:
        # linuxの場合はclip.exeの代わりにxclipを使う。ペイントは開かない。
        print("linux")
        subprocess.run(['xclip', '-selection', 'clipboard', '-t', 'image/png', '-i', 'tmp.png'])


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
