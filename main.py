import time

import win32gui
from PyQt5.QtWidgets import QApplication
import sys

from check_yg import Check
from pyauto_yg import move_and_click

def find_hwnd_enum(hwnd, result_list):
    # 获取窗口标题
    title = win32gui.GetWindowText(hwnd)
    if title:  # 确保窗口有标题
        result_list.append((hwnd, title))

def find_hwnd():
    window_handles = []
    win32gui.EnumWindows(find_hwnd_enum, window_handles)
    for hwnd, title in window_handles:
        print(f'句柄：{hwnd}\t 应用程序：{title}')
    return window_handles

# 启动窗口
def start(hwnd_name):
    hwnd = win32gui.FindWindow(None, hwnd_name)

    '''
    #置顶窗口然后再取消置顶
    if hwnd:
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
    '''

    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()

    # 创建一次旅程
    trval = Check()

    # 主循环
    while hwnd:

        #截取目标图像
        img = screen.grabWindow(hwnd).toImage()
        img.save("imgs/temp/color/working.png")

        #检查拉普兰德
        flag : None = trval.check()

        #如果是第二次检查到，则当前关卡并未结束，退出
        if flag and trval.flag:
            pass
        #游戏结算
        elif not flag:
            break
        #确认进行游戏
        else:
            trval.flag = True

            #休息一下（
            time.sleep(4)

            #重新截取图像
            img = screen.grabWindow(hwnd).toImage()
            img.save("imgs/temp/color/working.png")

            #计算不重复的方格数量
            trval.calculate()

            #输入
            trval.keyin()

        time.sleep(1)


if __name__ == '__main__':
    #find_hwnd()

    name = "MuMu模拟器12"
    while True:
        start(name)