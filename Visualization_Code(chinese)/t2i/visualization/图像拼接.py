import cv2
import numpy as np

def concatenate_images_horizontally(image_paths):
    # 读取所有图像并存储在一个列表中
    images = [cv2.imread(image_path) for image_path in image_paths]

    # 获取图像的高度和宽度
    height = images[0].shape[0]
    total_width = sum([image.shape[1] for image in images])

    # 创建一个空白的图像来存储拼接后的结果
    result_image = np.zeros((height, total_width, 3), dtype=np.uint8)

    # 初始化起始和结束列索引
    start_col = 0

    # 将每张图像拼接到结果图像中
    for image in images:
        end_col = start_col + image.shape[1]
        result_image[:, start_col:end_col, :] = image
        start_col = end_col

    return result_image

# 输入图像文件路径列表
# image_paths = ['3-eps0.4_ftlow_18.jpg','3-eps0.3_ftlow_18.jpg','3-eps0.2_ftlow_18.jpg','3-eps0.1_ftlow_18.jpg','3-eps0.05_ftlow_18.jpg','3-eps0.02_ftlow_18.jpg','3-eps0.0_ftlow_18.jpg']  # 用你的图像文件路径替换这里
image_paths = ['3-eps0.4_fthigh_18.jpg','3-eps0.3_fthigh_18.jpg','3-eps0.2_fthigh_18.jpg',
               '3-eps0.1_fthigh_18.jpg','3-eps0.05_fthigh_18.jpg','3-eps0.02_fthigh_18.jpg','3-eps0.0_fthigh_18.jpg']  # 用你的图像文件路径替换这里

#image_paths = ['2-eps0.4_ftlow.jpg','2-eps0.3_ftlow.jpg','2-eps0.2_ftlow.jpg','2-eps0.1_ftlow.jpg','2-eps0.0_ftlow.jpg']
#image_paths = ['2-eps0.4.png','2-eps0.3.png','2-eps0.2.png','2-eps0.1.png','2-eps0.0.png']
# image_paths = ['2-eps0.4_fthigh.jpg','2-eps0.3_fthigh.jpg','2-eps0.2_fthigh.jpg','2-eps0.1_fthigh.jpg','2-eps0.0_fthigh.jpg']
# image_paths = ['2-eps0.4_ftlow.jpg','2-eps0.3_ftlow.jpg','2-eps0.2_ftlow.jpg','2-eps0.1_ftlow.jpg','2-eps0.0_ftlow.jpg']

# 横向拼接图像
concatenated_image = concatenate_images_horizontally(image_paths)

# 保存拼接后的图像
cv2.imwrite('3_fthigh_18_concat.jpg', concatenated_image)