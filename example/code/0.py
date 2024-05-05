import cv2
import numpy as np
import os
from PIL import Image, ImageEnhance

def adjust_image(image):
    # 调整色温
    # 这里我们假设色温的调整可以通过在B通道上添加一个偏移量来模拟
    b, g, r = cv2.split(image)
    b = b + 10  # 增加蓝色通道
    image = cv2.merge([b, g, r])

    # 使用PIL进行其他的调整
    image = Image.fromarray(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # 调整色调
    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(1.17)

    # 调整曝光度
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(0.5)

    # 调整对比度
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.35)

    # 调整清晰度
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(1.15)

    return image

# 图片文件夹路径
folder_path = "E:\\file\python\MyCode\example\data\\0"

img_path = folder_path

# 检查文件是否存在
if not os.path.exists(img_path):
    print(f"File does not exist: {img_path}")
else:
    # 检查文件权限
    if not os.access(img_path, os.R_OK):
        print(f"Cannot read file: {img_path}")
    else:
        # 尝试读取图像
        img = cv2.imread(img_path)
        if img is None:
            print(f"Could not read image with OpenCV: {img_path}")
        else:
            print(f"Image read successfully: {img_path}")

# 遍历文件夹内的所有图片
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        img_path = os.path.join(folder_path, filename)
        img = cv2.imread(img_path)

        # 调整图片
        adjusted_img = adjust_image(img)

        # 保存调整后的图片
        adjusted_img.save(os.path.join(folder_path, "adjusted_" + filename))
