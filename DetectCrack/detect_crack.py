import cv2
import numpy as np


def detect_crack(src=None, dest=None):
    if not dest:
        dest = '/tmp/detect_crack_result.jpg'
    image = cv2.imread(src)
    blur = cv2.medianBlur(image, 7) #平滑
    gray = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY) #白黒 
    thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,3) #二値化

    canny = cv2.Canny(thresh, 120, 255, 1) #Canny法によるエッジ検出
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5)) #構造的要素（カーネル）作成
    opening = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel) #ノイズ除去のためのオープニング処理
    dilate = cv2.dilate(opening, kernel, iterations=2) #膨張

    cnts = cv2.findContours(dilate, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #輪郭検出
    cnts = cnts[0] if len(cnts) == 2 else cnts[1]
    
    min_area = 3000
    for c in cnts:
        area = cv2.contourArea(c)
        if area > min_area:
            cv2.drawContours(image, [c], -1, (36, 255, 12), 2)

    cv2.imwrite(dest, image)
    return(dest)
