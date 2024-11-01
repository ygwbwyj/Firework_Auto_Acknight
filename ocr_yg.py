import pytesseract
from PIL import Image

def ocr_origin(path):
    #设置路径
    pytesseract.pytesseract.tesseract_cmd = r"OCR\tesseract.exe"

    # 打开要识别的图片
    image = Image.open(path)

    # 使用pytesseract调用image_to_string方法进行识别，传入要识别的图片(png格式)，lang='chi_sim'是设置为中文识别，
    text = pytesseract.image_to_string(image, lang='chi_sim')
    return text


