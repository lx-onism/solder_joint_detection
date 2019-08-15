# -*- coding: utf-8 -*-
import os
import random

trainval_percent = 1                  # 用于训练验证的数据比例
train_percent = 0.8                   # 用于训练验证的数据中，训练数据所占比例
xmlfilepath = '/PycharmProjects/lx/data/xml'                 # 标注信息xml文件路径 
txtsavepath = '/PycharmProjects/lx/data/Main'               # 文件保存路径
total_xml = os.listdir(xmlfilepath)

num=len(total_xml)
list=range(num)
tv=int(num*trainval_percent)
tr=int(tv*train_percent)
trainval= random.sample(list,tv)
train=random.sample(trainval,tr)

ftrainval = open('/PycharmProjects/lx/data/Main/trainval.txt', 'w')
ftest = open('/PycharmProjects/lx/data/Main/test.txt', 'w')
ftrain = open('/PycharmProjects/lx/data/Main/train.txt', 'w')
fval = open('/PycharmProjects/lx/data/Main/val.txt', 'w')

for i  in list:
    name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest .close()


