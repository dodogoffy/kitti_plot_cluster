# txt_to_xml.py
# encoding:utf-8
# 根据一个给定的XML Schema，使用DOM树的形式从空白文件生成一个XML
from xml.dom.minidom import Document
import cv2
import os

def generate_xml(img_name, split_lines, img_size, class_ind, annotations_path):
    doc = Document()  # 创建DOM文档对象

    annotation = doc.createElement('annotation')
    doc.appendChild(annotation)

    title = doc.createElement('folder')
    title_text = doc.createTextNode('KITTI')
    title.appendChild(title_text)
    annotation.appendChild(title)

    title = doc.createElement('filename')
    title_text = doc.createTextNode(img_name)
    title.appendChild(title_text)
    annotation.appendChild(title)

    source = doc.createElement('source')
    annotation.appendChild(source)

    title = doc.createElement('database')
    title_text = doc.createTextNode('The KITTI Database')
    title.appendChild(title_text)
    source.appendChild(title)

    title = doc.createElement('annotation')
    title_text = doc.createTextNode('KITTI')
    title.appendChild(title_text)
    source.appendChild(title)

    size = doc.createElement('size')
    annotation.appendChild(size)

    title = doc.createElement('width')
    title_text = doc.createTextNode(str(img_size[1]))
    title.appendChild(title_text)
    size.appendChild(title)

    title = doc.createElement('height')
    title_text = doc.createTextNode(str(img_size[0]))
    title.appendChild(title_text)
    size.appendChild(title)

    title = doc.createElement('depth')
    title_text = doc.createTextNode(str(img_size[2]))
    title.appendChild(title_text)
    size.appendChild(title)

    for split_line in split_lines:
        line=split_line.strip().split()
        if line[0] in class_ind:
            object = doc.createElement('object')
            annotation.appendChild(object)

            title = doc.createElement('name')
            title_text = doc.createTextNode(line[0])
            title.appendChild(title_text)
            object.appendChild(title)

            bndbox = doc.createElement('bndbox')
            object.appendChild(bndbox)
            title = doc.createElement('xmin')
            title_text = doc.createTextNode(str(int(float(line[4]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('ymin')
            title_text = doc.createTextNode(str(int(float(line[5]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('xmax')
            title_text = doc.createTextNode(str(int(float(line[6]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)
            title = doc.createElement('ymax')
            title_text = doc.createTextNode(str(int(float(line[7]))))
            title.appendChild(title_text)
            bndbox.appendChild(title)

    # 将DOM对象doc写入文件
    # f = open('Annotations/'+name+'.xml','w')
    # f = open('/media/ExtHDD/cc/datasets/kitti_2d_detection/data_preprocess/Voc_kitti/Annotations/' + name + '.xml', 'w')
    # f = open('D:\ws_pycharm\kitti_data_processing\data_origin/trainval/voc_kitti_trainval\Annotations/' + name + '.xml', 'w')
    f = open(annotations_path + img_name[:-4] + '.xml', 'w')
    f.write(doc.toprettyxml(indent = ''))
    f.close()

if __name__ == '__main__':
    class_ind=('Car', 'Pedestrian', 'Cyclist')
    # cur_dir=os.getcwd()
    # labels_dir=os.path.join(cur_dir,'label_2')
    # labels_dir = '/media/ExtHDD/cc/datasets/kitti_2d_detection/data_preprocess/Labels_modified'
    # labels_dir = 'D:\ws_pycharm\kitti_data_processing\data_origin/trainval\label_2_modified'

    trainval_txt = 'E:\py-projects\SSD-TF\converter\kitti_voc\kittivoc_trainval\ImageSets\Main/trainval.txt'
    test_txt = 'E:\py-projects\SSD-TF\converter\kitti_voc\kittivoc_test\ImageSets\Main/test.txt'

    labels_path = 'E:\py-projects\SSD-TF\converter\kitti_2d_detection\label_2_modified'

    with open(test_txt, 'r') as f:
        for line in f.readlines():
            # print(line)
            line = line.strip()  # 去掉每行头尾空白
            if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
                continue
            label_txt_path = os.path.join(labels_path, line + '.txt')
            f = open(label_txt_path)
            split_lines = f.readlines()
            img_name = line + '.jpg'
            img_path = os.path.join('E:\py-projects\SSD-TF\converter\kitti_2d_detection\image_2_jpg', img_name)  # 路径需要自行修改
            img_size = cv2.imread(img_path).shape
            annotations_path = 'E:\py-projects\SSD-TF\converter\kitti_voc\kittivoc_test\Annotations/'
            generate_xml(img_name, split_lines, img_size, class_ind, annotations_path)

    with open(trainval_txt, 'r') as f:
        for line in f.readlines():
            # print(line)
            line = line.strip()  # 去掉每行头尾空白
            if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
                continue
            label_txt_path = os.path.join(labels_path, line + '.txt')
            f = open(label_txt_path)
            split_lines = f.readlines()
            img_name = line + '.jpg'
            img_path = os.path.join('E:\py-projects\SSD-TF\converter\kitti_2d_detection\image_2_jpg', img_name)  # 路径需要自行修改
            img_size = cv2.imread(img_path).shape
            annotations_path = 'E:\py-projects\SSD-TF\converter\kitti_voc\kittivoc_trainval\Annotations/'
            generate_xml(img_name, split_lines, img_size, class_ind, annotations_path)

print('all txts has converted into xmls')