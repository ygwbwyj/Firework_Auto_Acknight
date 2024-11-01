import time
from operator import truediv

import cv2
import pytesseract
import numpy as np


from pyauto_yg import move_and_click
from cv2_yg import search_rec
from ocr_yg import ocr_origin

def distance_2d(a,b):
    x=a[0] - b[0]
    y=a[1] - b[1]
    return (x * x + y * y) ** 0.5

#自定义实现
class Check:
    path = "imgs/temp/color/working.png"
    flag = False
    count = ""
    name = ""

    def __init__(self):

        #初始化OCR
        pytesseract.pytesseract.tesseract_cmd = r"OCR\tesseract.exe"

    #检测是否进入工作环境
    def check(self):
        location = search_rec(self.path, "imgs/temp/text/Lappland.png", (300,350), (500,570))
        return location

    #计算不重合的方块数量
    def calculate(self):
        #读取原图
        img = cv2.imread(self.path,1)

        cv2.imwrite("imgs/temp/color"+ "img.png", img)
        pazzle1 = np.zeros((5, 5), dtype=np.uint8)
        pazzle2 = np.zeros((5, 5), dtype=np.uint8)

        #pazzle1
        for i in range(5):
            for j in range(5):

                y1 = 200 + 37 * i
                y2 = 237 + 37 * i
                x1 = 115 + 37 * j
                x2 = 152 + 37 * j

                small = img[y1:y2, x1:x2]

                cv2.imwrite("imgs/temp/color/"+str(i) + str(j) + "2.png",small)

                avanger = np.average(small, axis=(0, 1))

                '''
                print((i,j))
                print(avanger)
                '''
                if avanger[1]<120:
                    pazzle1[i,j] = 1
                else:
                    pazzle1[i,j] = 0

        # pazzle2
        for i in range(5):
            for j in range(5):

                y1 = 420 + 37 * i
                y2 = 457 + 37 * i
                x1 = 108 + 37 * j
                x2 = 145 + 37 * j

                small = img[y1:y2, x1:x2]

                cv2.imwrite("imgs/temp/color/" + str(i) + str(j) + "2.png", small)

                avanger = np.average(small, axis=(0, 1))

                '''
                print((i, j))
                print(avanger)
                '''
                if avanger[1] < 140:
                    pazzle2[i, j] = 1
                else:
                    pazzle2[i, j] = 0


        result = pazzle1 | pazzle2
        self.count = str(sum(sum(result)))
        print(self.count)

    #根据count输入
    def keyin(self):
        coordinates = {
            '0': (130, 760),
            '1': (70, 840),
            '2': (175, 840),
            '3': (285, 840),
            '4': (400, 840),
            '5': (505, 840),
            '6': (130, 920),
            '7': (235, 920),
            '8': (340, 920),
            '9': (445, 920)
        }

        #输入
        for digit in self.count:
            x, y = coordinates[digit]
            move_and_click(x, y)
            time.sleep(0.1)

