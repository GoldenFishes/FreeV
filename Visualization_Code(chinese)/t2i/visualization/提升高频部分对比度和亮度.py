import cv2

# 读取原始图像
original_image = cv2.imread("3_fthigh_18_concat.jpg")

# 对比度增强参数
alpha = 1.5 # 调整这个值以改变对比度

# 亮度增强参数
beta = 0  # 调整这个值以改变亮度

# 对图像进行对比度增强和亮度增强
enhanced_image = cv2.convertScaleAbs(original_image, alpha=alpha, beta=beta)

# 保存增强后的图像
cv2.imwrite('3_fthigh_18_concat_enhanced.jpg', enhanced_image)