import cv2

path = "imgs/temp/color/working.png"

'''
def save():

    #彩色读取
    img = cv2.imread(path,1)

    path_save = "imgs/temp/text/Lappland.png"

    cv2.imwrite(path_save,img[360:540,320:470]) 
    '''

def save1():

    #彩色读取
    img = cv2.imread(path,1)

    path_save = "imgs/temp/text/pazzle1.png"

    cv2.imwrite(path_save,img[200:385,115:300])


def save():

    #彩色读取
    img = cv2.imread(path,1)

    path_save = "imgs/temp/text/pazzle2.png"

    cv2.imwrite(path_save,img[420:605,108:293])

if __name__ == '__main__':
    save()
