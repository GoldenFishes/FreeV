import numpy as np
import matplotlib.pyplot as plt

def Compute(paths, n=1536, ComputeN=True, Area=10.0):
    '''
    读取的txt为由torch.Size([1, 1104, 1536])拉伸成一条直线的数组
    数组[(<---1536--->)(<---1536--->)(<---1536--->)......(<---1536--->)]共1104个1536
    每隔n个数采一次样
    取值0-Area*Π之间
    '''
    area = Area

    plt.figure(figsize=(10, 6))

    for path in paths:
        with open(path, 'r') as file:
            lines = file.readlines()
            float_array = [float(line.strip()) for line in lines]

        if ComputeN:
            # 对数组进行采样
            sampled_array = float_array[::n]

            # 进行快速傅里叶变换
            fft_result = np.fft.fft(sampled_array)

            # 计算振幅谱
            magnitude = np.abs(fft_result)
            log_magnitude = 20 * np.log10(magnitude)

            if 'backbone' in path:
                reference_log_magnitude = log_magnitude[0]  # 存储第一个0点频率上的Backbone曲线的对数值

        else:
            # 计算块的数量
            num_blocks = len(float_array) // 1536
            # 将数组分割成块
            block_array = np.array(float_array).reshape(num_blocks, 1536)
            # 叠加块并计算平均值
            averaged_array = np.mean(block_array, axis=0)

            # 进行快速傅里叶变换
            fft_result = np.fft.fft(averaged_array)

            # 计算振幅谱
            magnitude = np.abs(fft_result)
            log_magnitude = 20 * np.log10(magnitude)

            if 'backbone' in path:
                reference_log_magnitude = log_magnitude[0]  # 存储第一个0点频率上的Backbone曲线的对数值

        # 计算相对对数值，以第一个0点频率上的Backbone曲线为标准
        relative_log_magnitude = log_magnitude - reference_log_magnitude

        # 获取频率轴
        N = len(sampled_array)
        frequency = np.fft.fftfreq(N, 1.0 / n)

        # 为曲线添加名称
        if 'backbone' in path:
            label = 'Backbone'
            color = 'green'
            linestyle = '--'
        elif 'skip' in path:
            label = 'Skip'
            color = 'orange'
            linestyle = '-.'
        elif 'fusion' in path:
            label = 'Fusion'
            color = 'Blue'
            linestyle = '-'
        else:
            label = 'Unknown'
            color = 'black'

        # 筛选频率轴在0.0到10.0Π区间的值
        mask = (frequency >= 0.0) & (frequency <= area*np.pi)
        filtered_frequency = frequency[mask]
        filtered_relative_log_magnitude = relative_log_magnitude[mask]

        plt.plot(filtered_frequency, filtered_relative_log_magnitude, label=label, color=color, linestyle=linestyle)

    # 绘制振幅谱
    plt.xlabel('Frequency', fontsize=16)
    plt.ylabel('Relative Log Amplitude', fontsize=16)
    plt.grid(True)

    # 设置横轴刻度为0.0到10.0Π
    plt.xticks(np.arange(0, (area + 0.2) * np.pi, np.pi), [str(i) + 'π' for i in range(int(area + 1))])

    # 移除左侧和右侧的空白
    plt.xlim(0, area * np.pi)

    plt.grid(False)

    # 显示图例
    plt.legend()

    plt.show()

file_paths = ['backbone_v.txt','skip_v.txt','fusion_v.txt']


Compute(file_paths, n=1104, Area=10.0)