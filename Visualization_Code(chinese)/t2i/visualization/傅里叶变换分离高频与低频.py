import cv2
import numpy as np
import os

def process_and_save_frequency_images(input_filename, output_dir, radius):
    # 读取彩色图像
    input_image_path = f'{input_filename}.png'
    image = cv2.imread(input_image_path)

    # 分离颜色通道
    b, g, r = cv2.split(image)

    # 对每个通道进行傅里叶变换
    f_transform_b = np.fft.fft2(b)
    f_transform_g = np.fft.fft2(g)
    f_transform_r = np.fft.fft2(r)

    # 对变换后的数据进行中心化处理
    f_transform_shifted_b = np.fft.fftshift(f_transform_b)
    f_transform_shifted_g = np.fft.fftshift(f_transform_g)
    f_transform_shifted_r = np.fft.fftshift(f_transform_r)

    rows, cols = image.shape[:2]
    crow, ccol = rows // 2, cols // 2

    # 创建一个掩码以过滤高频和低频部分
    mask = np.zeros((rows, cols), np.uint8)
    mask[crow - radius:crow + radius, ccol - radius:ccol + radius] = 1

    # 应用掩码来过滤高频和低频部分
    f_transform_shifted_low_b = f_transform_shifted_b * mask
    f_transform_shifted_low_g = f_transform_shifted_g * mask
    f_transform_shifted_low_r = f_transform_shifted_r * mask

    f_transform_shifted_high_b = f_transform_shifted_b * (1 - mask)
    f_transform_shifted_high_g = f_transform_shifted_g * (1 - mask)
    f_transform_shifted_high_r = f_transform_shifted_r * (1 - mask)

    # 进行逆傅里叶变换来还原图像
    low_frequency_b = np.fft.ifftshift(f_transform_shifted_low_b)
    low_frequency_g = np.fft.ifftshift(f_transform_shifted_low_g)
    low_frequency_r = np.fft.ifftshift(f_transform_shifted_low_r)
    low_frequency_image = np.zeros_like(image, dtype=np.uint8)
    low_frequency_image[:,:,0] = np.abs(np.fft.ifft2(low_frequency_b)).astype(np.uint8)
    low_frequency_image[:,:,1] = np.abs(np.fft.ifft2(low_frequency_g)).astype(np.uint8)
    low_frequency_image[:,:,2] = np.abs(np.fft.ifft2(low_frequency_r)).astype(np.uint8)

    high_frequency_b = np.fft.ifftshift(f_transform_shifted_high_b)
    high_frequency_g = np.fft.ifftshift(f_transform_shifted_high_g)
    high_frequency_r = np.fft.ifftshift(f_transform_shifted_high_r)
    high_frequency_image = np.zeros_like(image, dtype=np.uint8)
    high_frequency_image[:,:,0] = np.abs(np.fft.ifft2(high_frequency_b)).astype(np.uint8)
    high_frequency_image[:,:,1] = np.abs(np.fft.ifft2(high_frequency_g)).astype(np.uint8)
    high_frequency_image[:,:,2] = np.abs(np.fft.ifft2(high_frequency_r)).astype(np.uint8)

    # 保存高频和低频图像
    output_low_frequency_path = os.path.join(output_dir, f'{input_filename}_ftlow_{radius}.jpg')
    output_high_frequency_path = os.path.join(output_dir, f'{input_filename}_fthigh_{radius}.jpg')

    cv2.imwrite(output_low_frequency_path, low_frequency_image)
    cv2.imwrite(output_high_frequency_path, high_frequency_image)

# 使用示例
input_filename = '3-eps0.0'
output_directory = '.'  # 保存在当前目录，你可以指定其他目录
radius = 18 # 掩码半径的值
process_and_save_frequency_images(input_filename, output_directory, radius)
