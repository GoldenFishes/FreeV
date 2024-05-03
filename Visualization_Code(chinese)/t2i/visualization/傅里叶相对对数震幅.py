# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.signal import savgol_filter
#
# def calculate_log_amplitude(image_path):
#     # 读取彩色图像
#     image = plt.imread(image_path)
#     # 将图像转换为灰度图像
#     gray_image = np.mean(image, axis=2)
#     # 计算傅立叶变换
#     f_transform = np.fft.fft2(gray_image)
#     f_transform_shifted = np.fft.fftshift(f_transform)
#     # 计算频谱振幅
#     amplitude = np.abs(f_transform_shifted)
#     # 计算相对对数振幅
#     log_amplitude = np.log1p(amplitude)
#     # 获取频率轴
#     height, width = gray_image.shape
#     freq_x = np.fft.fftfreq(width)
#     # 计算频率范围从0.0π到1.0π对应的索引范围
#     start_freq_index = int(width / 2)
#     end_freq_index = int(width / 2 + width / 2)
#     # 提取相对对数振幅的子集
#     log_amplitude_subset = log_amplitude[:, start_freq_index:end_freq_index]
#     freq_x_subset = freq_x[start_freq_index:end_freq_index]
#     return freq_x_subset, log_amplitude_subset[0]
#
# def smooth_and_plot(image_paths,n=4):
#     plt.figure(figsize=(10, 5))
#     for i, image_path in enumerate(image_paths):
#         freq_x, log_amplitude = calculate_log_amplitude(image_path)
#         alpha = (i + 1) / len(image_paths)  # 调整透明度
#
#         # 使用Savitzky-Golay滤波进行平滑处理，增加平滑的力度
#         smoothed_log_amplitude = savgol_filter(log_amplitude, window_length=21, polyorder=1)
#
#         # 绘制平滑前的曲线
#         # plt.plot(freq_x * np.pi, log_amplitude, label=f'{image_path} (Original)', alpha=alpha, color='gray')
#
#         # 绘制平滑后的曲线
#         plt.plot(freq_x * np.pi, smoothed_log_amplitude, label=f'{image_path} (Smoothed)', alpha=alpha, color='blue')
#
#     plt.xlabel('Frequency (0.0π to 1.0π)')
#     plt.ylabel('Log Amplitude')
#     plt.title('Frequency vs Log Amplitude (Original vs Smoothed)')
#     plt.grid()
#     plt.legend()
#     plt.show()
#
#
# # 示例调用函数
# # image_paths = ['7-eps0.9.png',
# #                '7-eps0.8.png',
# #                '7-eps0.7.png',
# #                '7-eps0.6.png',
# #                '7-eps0.5.png',
# #                '7-eps0.4.png',
# #                '7-eps0.3.png',
# #                '7-eps0.2.png',
# #                '7-eps0.1.png',
# #                '7-eps0.0.png']  # 替换为您的图像文件路径列表
# image_paths = ['0-eps0.8.png',
#                '0-eps0.6.png',
#                '0-eps0.4.png',
#                '0-eps0.2.png',
#                '0-eps0.0.png']  # 替换为您的图像文件路径列表
#
# smooth_and_plot(image_paths,n=8)
#
# # plt.figure(figsize=(10, 5))
# # for i, image_path in enumerate(image_paths):
# #     freq_x, log_amplitude = calculate_log_amplitude(image_path)
# #     alpha = (i + 1) / len(image_paths)  # 调整透明度
# #     plt.plot(freq_x * np.pi, log_amplitude, label=image_path, alpha=alpha, color='blue')
# #
# # plt.xlabel('Frequency (0.0π to 1.0π)')
# # plt.ylabel('Log Amplitude')
# # plt.title('Frequency vs Log Amplitude')
# # plt.grid()
# # plt.legend()
# # plt.show()

##  代码2---------------------------------------------------------------------------------
#
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
#
# def calculate_and_plot_fourier_log_amplitude(input_filename):
#     # 读取图像
#     image = cv2.imread(input_filename, cv2.IMREAD_GRAYSCALE)
#
#     # 进行傅里叶变换
#     fourier_transform = np.fft.fft2(image)
#
#     # 计算傅里叶变换的幅度
#     amplitude = np.abs(fourier_transform)
#
#     # 计算对数震幅
#     log_amplitude = np.log(amplitude + 1)  # 添加1以避免对数中出现零值
#
#     # 获取图像的宽度
#     image_width = image.shape[1]
#
#     # 计算频率轴上的值
#     frequency_values = np.fft.fftfreq(image_width)
#
#     # 重新排列频率轴和对数震幅，使其从0.0Π到1.0Π排列
#     sorted_indices = np.argsort(frequency_values)
#     frequency_values = frequency_values[sorted_indices] * np.pi  # 缩放为0.0Π到1.0Π
#     log_amplitude = log_amplitude[:, sorted_indices]
#
#     # 创建横坐标的数组，从0.0Π到1.0Π
#     x_values = np.linspace(0, np.pi, len(log_amplitude[0]))
#
#     # 绘制曲线图
#     plt.plot(x_values, log_amplitude[0])  # 绘制第一行的数据，你可以根据需要选择其他行
#     plt.xlabel('Frequency (radians)')
#     plt.ylabel('Log Amplitude')
#     plt.title('Fourier Log Amplitude')
#     plt.grid(True)
#
#     # 构建保存的文件名
#     output_filename = input_filename.replace('.png', '-fourier_log_amplitude.png')
#
#     # 保存图像为文件
#     plt.savefig(output_filename)
#
#     # 显示曲线图
#     plt.show()
#
# # 使用示例
# input_filename = '0-eps1.0.png'
# calculate_and_plot_fourier_log_amplitude(input_filename)

# --------------------批量----0.0-0.1raids绝对对数震动频率

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.cm import get_cmap
#
#
# def calculate_fourier_log_amplitude(image):
#     # 进行傅里叶变换
#     fourier_transform = np.fft.fft2(image)
#
#     # 计算傅里叶变换的幅度
#     amplitude = np.abs(fourier_transform)
#
#     # 计算对数震幅
#     log_amplitude = np.log(amplitude + 1)  # 添加1以避免对数中出现零值
#
#     # 获取图像的宽度
#     image_width = image.shape[1]
#
#     # 计算频率轴上的值
#     frequency_values = np.fft.fftfreq(image_width)
#
#     # 重新排列频率轴和对数震幅，使其从0.0Π到1.0Π排列
#     sorted_indices = np.argsort(frequency_values)
#     frequency_values = frequency_values[sorted_indices] * np.pi  # 缩放为0.0Π到1.0Π
#     log_amplitude = log_amplitude[:, sorted_indices]
#
#     return log_amplitude[0], frequency_values
#
#
# def plot_multiple_fourier_log_amplitudes(image_filenames):
#     plt.figure(figsize=(8, 6))
#
#     # 获取蓝色渐变颜色映射
#     cmap = get_cmap('Blues')
#
#     for i, filename in enumerate(image_filenames):
#         # 读取图像
#         image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
#
#         # 计算傅里叶对数震幅
#         log_amplitude, frequency_values = calculate_fourier_log_amplitude(image)
#
#         # 设置线条颜色为蓝色渐变
#         color = cmap(i / len(image_filenames))
#
#         # 绘制曲线，使用蓝色渐变颜色，并限制横坐标范围
#         plt.plot(frequency_values, log_amplitude, color=color, label=filename)
#
#     # 限制横坐标范围为0.0到1.0
#     plt.xlim(0.0, 1.0)
#
#     plt.xlabel('Frequency (radians)')
#     plt.ylabel('Log Amplitude')
#     plt.title('Multiple Fourier Log Amplitudes')
#     plt.grid(True)
#     plt.legend()
#     plt.show()
#
# # 使用示例
# image_filenames = ["0-eps1.0.png", "0-eps0.9.png", "0-eps0.8.png",
#                    "0-eps0.7.png", "0-eps0.6.png", "0-eps0.5.png",
#                    "0-eps0.4.png", "0-eps0.3.png", "0-eps0.2.png",
#                    "0-eps0.1.png", "0-eps0.0.png"]
# plot_multiple_fourier_log_amplitudes(image_filenames)

# --------------------批量----相对对数震动频率

# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.cm import get_cmap
#
#
# def calculate_relative_log_frequency(image):
#     # 进行傅里叶变换
#     fourier_transform = np.fft.fft2(image)
#
#     # 计算傅里叶变换的幅度
#     amplitude = np.abs(fourier_transform)
#
#     # 计算相对对数震频
#     relative_log_frequency = np.log(amplitude + 1) - np.log(amplitude[0, 0] + 1)  # 相对于0点的对数震频
#
#     # 获取图像的宽度
#     image_width = image.shape[1]
#
#     # 计算频率轴上的值
#     frequency_values = np.fft.fftfreq(image_width)
#
#     # 重新排列频率轴和相对对数震频，使其从0.0Π到1.0Π排列
#     sorted_indices = np.argsort(frequency_values)
#     frequency_values = frequency_values[sorted_indices] * np.pi  # 缩放为0.0Π到1.0Π
#     relative_log_frequency = relative_log_frequency[:, sorted_indices]
#
#     return relative_log_frequency[0], frequency_values
#
#
# def plot_multiple_relative_log_frequencies(image_filenames):
#     plt.figure(figsize=(8, 6))
#
#     # 获取蓝色渐变颜色映射
#     cmap = get_cmap('Blues')
#
#     for i, filename in enumerate(image_filenames):
#         # 读取图像
#         image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
#
#         # 计算相对对数震频
#         relative_log_frequency, frequency_values = calculate_relative_log_frequency(image)
#
#         # 设置线条颜色为蓝色渐变
#         color = cmap(i / len(image_filenames))
#
#         # 绘制曲线，使用蓝色渐变颜色
#         plt.plot(frequency_values, relative_log_frequency, color=color, label=filename)
#
#     plt.xlabel('Frequency (radians)')
#     plt.ylabel('Relative Log Frequency')
#     plt.title('Multiple Relative Log Frequencies')
#     plt.grid(True)
#     plt.legend()
#     plt.show()
#
#
# # 使用示例
# image_filenames = ["0-eps1.0.png", "0-eps0.9.png", "0-eps0.8.png",
#                    "0-eps0.7.png", "0-eps0.6.png", "0-eps0.5.png",
#                    "0-eps0.4.png", "0-eps0.3.png", "0-eps0.2.png",
#                    "0-eps0.1.png", "0-eps0.0.png"]
# plot_multiple_relative_log_frequencies(image_filenames)

## 截取0-1Π

import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap


def calculate_relative_log_frequency(image):
    # 进行傅里叶变换
    fourier_transform = np.fft.fft2(image)
    # 计算傅里叶变换的幅度
    amplitude = np.abs(fourier_transform)
    # 计算相对对数震频
    relative_log_frequency = np.log(amplitude + 1) - np.log(amplitude[0, 0] + 1)  # 相对于0点的对数震频
    # 获取图像的宽度
    image_width = image.shape[1]
    # 计算频率轴上的值
    frequency_values = np.fft.fftfreq(image_width)
    # # 重新排列频率轴和相对对数震频，使其从0.0到1.0排列
    # sorted_indices = np.argsort(frequency_values)
    # frequency_values = frequency_values[sorted_indices] * np.pi  # 缩放为0.0到1.0
    # relative_log_frequency = relative_log_frequency[:, sorted_indices]
    # 保留0.0到1.0范围的部分
    valid_indices = (frequency_values >= 0.0) & (frequency_values <= 1.0/ np.pi)
    frequency_values = frequency_values[valid_indices]
    relative_log_frequency = relative_log_frequency[:, valid_indices]

    # 减少取值，减少震荡
    # 下面是添加的部分，每隔3个取一个值
    frequency_values = frequency_values[::4]
    relative_log_frequency = relative_log_frequency[:, ::4]

    # 重新排列频率轴
    # 重新排列频率轴到0.0到1.0范围
    frequency_values = (frequency_values - min(frequency_values)) / (max(frequency_values) - min(frequency_values))
    return relative_log_frequency[0], frequency_values

def plot_multiple_relative_log_frequencies(image_filenames, alpha=0.8):
    plt.figure(figsize=(8, 6))
    cmap = get_cmap('Blues')

    new_labels = ["step1","step100","step200",
                  "step300","step400","step500",
                  "step600","step700","step800",
                  "step900","step1000"]

    for i, filename in enumerate(image_filenames):
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        relative_log_frequency, frequency_values = calculate_relative_log_frequency(image)

        k = i / len(image_filenames)
        color = cmap(k+0.2)


        # 使用新标签
        label = new_labels[i]

        # 调整alpha参数以控制曲线的透明度
        plt.plot(frequency_values, relative_log_frequency, color=color, label=label, linewidth=2.5, alpha=alpha)


    plt.xlabel('Frequency', fontsize=16)
    plt.ylabel('Relative Log amplitude', fontsize=16)
    plt.xlim(0.0, 1.0)
    plt.grid(False)
    plt.legend()

    # 修改横坐标标签
    x_ticks = np.linspace(0, 1, 6)
    x_tick_labels = [f'{x:.1f}π' for x in x_ticks]
    plt.xticks(x_ticks, x_tick_labels)

    plt.show()


# 使用示例
# image_filenames = ["0-eps1.0.png", "0-eps0.8.png",
#                    "0-eps0.6.png",
#                    "0-eps0.4.png", "0-eps0.2.png",
#                    "0-eps0.0.png"]

image_filenames = ["0-eps1.0.png", "0-eps0.9.png", "0-eps0.8.png",
                   "0-eps0.7.png", "0-eps0.6.png", "0-eps0.5.png",
                   "0-eps0.4.png", "0-eps0.3.png", "0-eps0.2.png",
                   "0-eps0.1.png", "0-eps0.0.png"]

plot_multiple_relative_log_frequencies(image_filenames)

### 优化曲线


