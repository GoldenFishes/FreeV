import imageio

# 设置要合成的图片文件名列表
image_files = ["0-eps1.0.png", "0-eps0.9.png", "0-eps0.8.png",
               "0-eps0.7.png", "0-eps0.6.png", "0-eps0.5.png",
               "0-eps0.4.png", "0-eps0.3.png", "0-eps0.2.png",
               "0-eps0.1.png", "0-eps0.0.png"]  # 替换为你自己的图片文件名

# 设置输出动态图的文件名
output_file = "0-eps1-0.gif"

# 读取图片并将它们添加到一个帧列表中
frames = []
for image_file in image_files:
    img = imageio.imread(image_file)
    frames.append(img)

# 保存帧列表为一个动态图
imageio.mimsave(output_file, frames, duration=0.5)  # 设置帧之间的延迟时间（秒）

print(f"动态图已保存为 {output_file}")