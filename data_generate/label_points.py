# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os

imgpath = '/home/lx/Desktop/realsense/color_imgs/46.png'    # 图片路径

img = cv2.imread(imgpath)
path = imgpath.split('.')
num = 0
def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):         # 检测鼠标左键点击动作，若发生动作，则将鼠标所在位置的图像坐标存到'label.txt'文件中，并在图片中显示该点
    if event == cv2.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        print(xy)
        global num
        num += 1
        f = open('label.txt', 'a')               # 点坐标保存文件路径
        f.write(str(x)+' '+str(y)+' ')
        f.close()
        cv2.circle(img, (x, y), 1, (0, 0, 255), thickness=-1)
        #cv2.putText(img, xy, (x, y), cv2.FONT_HERSHEY_PLAIN, 1.0, (0, 0, 255), 1)
        cv2.imshow('image', img)

with open('label.txt', 'a') as f:
    f.writelines(imgpath+' ')
    f.close()
cv2.namedWindow("image")
cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
cv2.imshow('image', img)

while True:
    key = cv2.waitKey(1)
    if key & 0xFF == ord('s'):   #在标注完所有正样本后按‘s’键记录正样本个数
        print(num)
        global final_num
        final_num = num
    if key & 0xFF == ord('q') or key == 27:  #按q键或ESC键保存正样本个数并结束程序
        f = open('label.txt', 'a')
        f.write(str(final_num)+'\n')
        f.close()
        cv2.destroyAllWindows()
        break
