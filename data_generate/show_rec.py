# -*- coding: utf-8 -*-

import cv2
import numpy as np

def show_rec1(num):
    f = open('label_1.txt').readlines()
    file = f[num]
    file = file.strip().split()
    img = cv2.imread(file[0])
    pos_rec_point = [(int(file[i]), int(file[i+1])) for i in range(1, 2*int(file[-1]), 2)]       # 正样本集
    neg_rec = [(int(file[i]), int(file[i+1])) for i in range(1+2*int(file[-1]), len(file)-1, 2)]   # 负样本集
    y_point = [int(file[i+1]) for i in range(1, 2*int(file[-1]), 2)]
    d = open('data.txt', 'a')                                                      # 保存数据的文件路径
    d.write(file[0] + ' ')
    # 根据正样本个数生成不同大小的b_box
    if int(file[-1]) > 8:                                                         
        for i in range(len(y_point)-1):
            if i > 0:
                c1 = y_point[i+1]- y_point[i]
                c2 = y_point[i] - y_point[i-1]
                if np.abs(np.abs(c1)-np.abs(c2)) > 20:
                    global h
                    h = i
                    print(h)
        pos_rec_point1 = pos_rec_point[:h]
        pos_rec_point2 = pos_rec_point[h:]
        print(pos_rec_point1, pos_rec_point2)
        for i in range(len(pos_rec_point1)):
            bias = 30                        # b_box的边长/2
            b = open('bias.txt', 'a')
            b.write(str(2*bias)+' ')
            b.close()
            x = pos_rec_point1[i][0]
            y = pos_rec_point1[i][1]
            left_top = (max(x - bias, 1), max(y - bias, 1))
            right_bottom = (min(x + bias, img.shape[1] - 1), min(y + bias, img.shape[0] - 1))    # 防止边界框超出图像
            d.write(str(left_top[0]) + ' ' + str(left_top[1]) + ' ' + str(right_bottom[0]) + ' ' + str(
                right_bottom[1]) + ' '+str(x)+' '+str(y)+' ')                         # 将bbox左上角，右下角坐标及中心点坐标存入data.txt
            cv2.rectangle(img, left_top, right_bottom, (0, 0, 255), 1)                # 在图片中画框以检查框大小是否合适
        for i in range(len(pos_rec_point2)):
            if i == len(pos_rec_point2)-1:
                sub = pos_rec_point2[i - 1][0] - pos_rec_point2[i][0]
            else:
                sub = pos_rec_point2[i+1][0] - pos_rec_point2[i][0]
            bias = np.abs(sub)//2 - 6
            b = open('bias.txt', 'a')
            b.write(str(2*bias) + '\n')
            b.close()
            x = pos_rec_point2[i][0]
            y = pos_rec_point2[i][1]
            left_top = (max(x - bias, 1), max(y - bias, 1))
            right_bottom = (min(x + bias, img.shape[1] - 1), min(y + bias, img.shape[0] - 1))
            d.write(str(left_top[0]) + ' ' + str(left_top[1]) + ' ' + str(right_bottom[0]) + ' ' + str(
                right_bottom[1]) + ' '+str(x)+' '+str(y)+' ')
            cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
            cv2.rectangle(img, left_top, right_bottom, (0, 0, 255), 1)
    else:
        for i in range(len(pos_rec_point)):
            if i == len(pos_rec_point)-1:
                sub = pos_rec_point[i - 1][0] - pos_rec_point[i][0]
            else:
                sub = pos_rec_point[i+1][0] - pos_rec_point[i][0]
            bias = 40
            b = open('bias.txt', 'a')
            b.write(str(2 * bias) + '\n')
            b.close()
            x = pos_rec_point[i][0]
            y = pos_rec_point[i][1]
            left_top = (max(x - bias, 1), max(y - bias, 1))
            right_bottom = (min(x + bias, img.shape[1] - 1), min(y + bias, img.shape[0] - 1))
            d.write(str(left_top[0]) + ' ' + str(left_top[1]) + ' ' + str(right_bottom[0]) + ' ' + str(
                right_bottom[1]) + ' '+str(x)+' '+str(y)+' ')
            cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
            cv2.rectangle(img, left_top, right_bottom, (0, 0, 255), 1)
    # 将负样本信息存入data.txt，若无负样本可注释掉
    for i in range(0, len(neg_rec), 2):
        d.write(str(neg_rec[i][0])+' '+str(neg_rec[i][1])+' '+str(neg_rec[i+1][0])+' '+str(neg_rec[i+1][1])+' '+'0 0'+' ')
        cv2.rectangle(img, neg_rec[i], neg_rec[i+1], (0, 255, 0), 1)
    d.write(file[-1]+'\n') #记录焊接点（正样本）的个数，若label.txt中没有记录个数，请注释掉
    d.close()
    '''取消注释以逐张图片查看生成的矩形框效果，按下'n'键会自动查看下一张图片。注意：查看的同时会生成矩形框数据。若不需要该功能，请在查看前将相关程序注释掉'''
    # cv2.imshow(str(num), img)
    # while True:
    #     key = cv2.waitKey(1)
    #     if key & 0xFF == ord('n'):
    #         cv2.destroyAllWindows()
    #         num += 1
    #         show_rec1(num)
    #     if key & 0xFF == ord('q') or key == 27:
    #         cv2.destroyAllWindows()
    #         break


for j in range(45):  #自动为每张图片中的点生成一个矩形框并将其坐标存入data.txt中，'45'为总的图片张数，按实际情况进行修改
    show_rec1(j)

'''取消注释以逐张图片查看生成的矩形框效果，注：需要将show_rec1函数中的注释部分取消注释'''
#show_rec1(0)
