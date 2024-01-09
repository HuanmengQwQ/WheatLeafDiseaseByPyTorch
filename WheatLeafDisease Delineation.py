import random
import shutil
from PIL import Image
import os

# 将原数据图片PNG和JFIF格式图片转为JPG格式
original_folder = "./data/wheat-leaf-disease/"
output_folder = "./data/wheat-leaf-disease/"

# 创建目标文件夹
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍历原始文件夹中的所有文件
for filename in os.listdir(original_folder):
    # 构建文件的完整路径
    file_path = os.path.join(original_folder, filename)

    # 检查文件是否为图像文件（PNG、JFIF）
    if filename.lower().endswith((".png", ".jfif")):
        # 构建目标文件的完整路径
        output_path = os.path.join(output_folder, filename)

        # 复制文件到目标文件夹
        shutil.copy2(file_path, output_path)

        # 如果文件是PNG或JFIF，将其转换为JPEG
        if filename.lower().endswith((".png", ".jfif")):
            img = Image.open(output_path)

            # 检查图像模式并转换为RGB
            if img.mode == 'RGBA':
                img = img.convert('RGB')

            # 保存图像为JPEG
            img.save(output_path, 'JPG')

            print(f"Converted and saved: {filename} to {os.path.basename(output_path)}")
        else:
            print(f"Copied: {filename} to {os.path.basename(output_path)}")

print("转化完成.")


# 创建保存图像的文件夹
def makedir(new_dir):
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
random.seed(1)

# 1.确定原图像数据集路径
dataset_dir = "./data/wheat-leaf-disease/cropImg"  ##原始数据集路径
# 2.确定数据集划分后保存的路径
split_dir = "./data/wheat-leaf-disease/after"  ##划分后保存路径
train_dir = os.path.join(split_dir, "train")
valid_dir = os.path.join(split_dir, "val")
test_dir = os.path.join(split_dir, "test")
# 3.确定将数据集划分为训练集，验证集，测试集的比例
train_pct = 0.8
valid_pct = 0
test_pct = 0.2
# 4.划分
for root, dirs, files in os.walk(dataset_dir):
    for sub_dir in dirs: # 遍历0，1，2，3，4，5...9文件夹
        imgs = os.listdir(os.path.join(root, sub_dir)) # 展示目标文件夹下所有的文件名
        imgs = list(filter(lambda x: x.endswith('.jpg'), imgs)) # 取到所有以.jpg结尾的文件
        random.shuffle(imgs)  # 乱序图片路径
        img_count = len(imgs)  # 计算图片数量
        train_point = int(img_count * train_pct)
        valid_point = int(img_count * (train_pct + valid_pct))

        for i in range(img_count):
            if i < train_point:  # 保存0-train_point的图片到训练集
                out_dir = os.path.join(train_dir, sub_dir)
            elif i < valid_point:  # 保存train_point-valid_point的图片到验证集
                out_dir = os.path.join(valid_dir, sub_dir)
            else:  #  保存valid_point-结束的图片到测试集
                out_dir = os.path.join(test_dir, sub_dir)
            makedir(out_dir) # 创建文件夹
            target_path = os.path.join(out_dir, imgs[i]) # 指定目标保存路径
            src_path = os.path.join(dataset_dir, sub_dir, imgs[i])  #指定目标原图像路径
            shutil.copy(src_path, target_path)  # 复制图片

        print('Class:{}, train:{}, valid:{}, test:{}'.format(sub_dir, train_point, valid_point-train_point,
                                                             img_count-valid_point))
