import pyautogui
import pygetwindow as gw

def move_and_click(x,y):
    window_title = "MuMu模拟器12"
    window = gw.getWindowsWithTitle(window_title)[0]  # 获取窗口对象

    # 获取窗口左上角的屏幕坐标
    w_x = window.left
    w_y = window.top

    pyautogui.moveTo(x+w_x, y+w_y)
    pyautogui.click()

