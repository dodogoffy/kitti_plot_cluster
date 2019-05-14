import os
import shutil

trainval_txt = 'E:\py-projects\SSD-TF\converter\kitti_voc\kittivoc_trainval\ImageSets\Main/trainval.txt'
test_txt = 'E:\py-projects\SSD-TF\converter\kitti_voc\kittivoc_test\ImageSets\Main/test.txt'

jpg_path = 'E:\py-projects\SSD-TF\converter\kitti_2d_detection\image_2_jpg'
trainval_jpg_path = 'E:\py-projects\SSD-TF\converter\kitti_voc\kittivoc_trainval\JPEGImages'
test_jpg_path = 'E:\py-projects\SSD-TF\converter\kitti_voc\kittivoc_test\JPEGImages'

with open(trainval_txt, 'r') as f:
    for line in f.readlines():
        # print(line)
        line = line.strip()  # 去掉每行头尾空白
        if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
            continue
        source_jpg_path = os.path.join(jpg_path, line + '.jpg')
        target_jpg_path = os.path.join(trainval_jpg_path, line + '.jpg')
        shutil.copyfile(source_jpg_path, target_jpg_path)

with open(test_txt, 'r') as f:
    for line in f.readlines():
        # print(line)
        line = line.strip()  # 去掉每行头尾空白
        if not len(line) or line.startswith('#'):  # 判断是否是空行或注释行
            continue
        source_jpg_path = os.path.join(jpg_path, line + '.jpg')
        target_jpg_path = os.path.join(test_jpg_path, line + '.jpg')
        shutil.copyfile(source_jpg_path, target_jpg_path)

print('done.')
