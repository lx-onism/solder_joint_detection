import xml.etree.ElementTree as ET
from os import getcwd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]
#sets=[('2007', 'test')]

classes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "l", "m", "n", "o", "p", "r", "s", "t", "y"]  # 待检测物体的所有类别


def convert_annotation(year, image_id, list_file):
    #in_file = open('VOCdevkit_1/VOC%s/Annotations/%s.xml'%(year, image_id))                 # xml文件路径
    in_file = open('/home/lixiang/PycharmProjects/lx/data/xml/%s.xml' % image_id)
    tree=ET.parse(in_file)

    root = tree.getroot()

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult)==1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        print(xmlbox.find('xmin').text)
        b = ((xmlbox.find('xmin').text), (xmlbox.find('ymin').text), (xmlbox.find('xmax').text), (xmlbox.find('ymax').text))
        list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))

wd = getcwd()

for year, image_set in sets:
    #image_ids = open('VOCdevkit_1/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    image_ids = open('/home/lixiang/PycharmProjects/lx/data/Main/%s.txt' % (image_set)).read().strip().split()         
    list_file = open('%s_%s.txt'%(year, image_set), 'w')                         # 生成的图片及标注信息文件路径
    for image_id in image_ids:
        list_file.write('%s/data/img/%s.png'%(wd, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

