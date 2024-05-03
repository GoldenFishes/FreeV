# from sklearn import metrics as mr
# import cv2
#
# img1 = cv2.imread('real/1.png')
# img2 = cv2.imread('ud/2.png')
# img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
# nmi = mr.normalized_mutual_info_score(img1.reshape(-1), img2.reshape(-1))
# print(nmi)
#
# # ----------------------------
import cv2
import numpy as np

# 读取两张图片
img1 = cv2.imread('6.png')
img2 = cv2.imread('6o.png')

# Ensure both images have the same size
img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Compute SSIM using cv2.matchTemplate
result = cv2.matchTemplate(img1, img2, cv2.TM_CCOEFF_NORMED)
ssim = np.max(result)

print("SSIM:", ssim)