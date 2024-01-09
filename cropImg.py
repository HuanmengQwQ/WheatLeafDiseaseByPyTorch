from PIL import Image
import os


def resize_and_crop(img, target_size):
    # 计算缩放比例
    width, height = img.size
    min_side = min(width, height)
    scale = target_size / min_side

    # 缩放图像短边至目标大小，保持长宽比不变
    new_width = int(width * scale)
    new_height = int(height * scale)
    img = img.resize((new_width, new_height), Image.LANCZOS)

    # 计算剪切的区域
    left = (new_width - target_size) / 2
    top = (new_height - target_size) / 2
    right = (new_width + target_size) / 2
    bottom = (new_height + target_size) / 2

    # 剪切图像中心区域
    img = img.crop((left, top, right, bottom))

    return img


# 定义文件夹路径
folders = ['Brown_rust', 'Healthy', 'Septoria', 'Yellow_rust']
parent_directory = './data/wheat-leaf-disease/'

# 定义目标尺寸
target_size = 224

# 创建保存裁剪图片的文件夹
output_directory = './data/wheat-leaf-disease'
os.makedirs(output_directory, exist_ok=True)

# 遍历文件夹
for folder in folders:
    folder_path = os.path.join(parent_directory, folder)
    output_folder = os.path.join(output_directory, folder)

    # 创建输出文件夹
    os.makedirs(output_folder, exist_ok=True)

    # 遍历文件夹中的图片文件
    for filename in os.listdir(folder_path):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            # 读取原始图片
            img_path = os.path.join(folder_path, filename)
            original_img = Image.open(img_path)

            resized_img = resize_and_crop(original_img, target_size)

            # 构建保存路径
            output_path = os.path.join(output_folder, filename)

            # 保存裁剪后的图片
            resized_img.save(output_path)

print("裁剪并保存完成")
