import cv2
import numpy as np

#在一个圆形范围内查找图像,返回找到的图像的位置（大图找小图）
#原图，小图，圆心，半径
def search_cir(img_path,template_path,center,r):
    img = cv2.imread(img_path)
    template = cv2.imread(template_path)

    #蒙版，匹配
    mask = np.zeros(img.shape[:2], dtype="uint8")
    cv2.circle(mask, center, r, 255, -1)
    img_masked = cv2.bitwise_and(img, img, mask=mask)
    result = cv2.matchTemplate(img_masked, template, cv2.TM_CCORR_NORMED)

    #根据阈值选择匹配的图像
    threshold = 0.9
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    #print(locations)
    return locations

#在矩形区域匹配图像
#原图，小图，左上坐标，右下坐标
def search_rec(img_path, template_path, a, b):
    # 读取原图和模板图
    img = cv2.imread(img_path)
    template = cv2.imread(template_path)

    if img is None or template is None:
        print("Error: 图片读取失败，请检查路径。")
        return []

    # 创建蒙版，匹配
    mask = np.zeros(img.shape[:2], dtype="uint8")
    cv2.rectangle(mask, a, b, 255, -1)  # a 和 b 应该是 (x1, y1) 和 (x2, y2)

    # 应用蒙版
    img_masked = cv2.bitwise_and(img, img, mask=mask)

    # 显示蒙版图像
    '''
    cv2.imshow("Masked Image", img_masked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  # 添加关闭所有窗口的函数
    '''

    # 模板匹配
    result = cv2.matchTemplate(img_masked, template, cv2.TM_CCORR_NORMED)

    # 根据阈值选择匹配的图像
    threshold = 0.95
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    return locations





