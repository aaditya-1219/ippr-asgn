import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# DISPLAY RESIZED GRAYSCALE IMAGE 
img = cv.imread("./walchand.jpeg")
resizedImg = cv.resize(img, (512,512))
grayImg = cv.cvtColor(resizedImg, cv.COLOR_BGR2GRAY)
cv.imshow('image',grayImg)
cv.waitKey(0)

# SPLIT THE CHANNELS
# img = cv.imread("./walchand.jpeg")
# img = cv.resize(img, (512,512))
# b = img[:,:,0]
# g = img[:,:,1]
# r = img[:,:,2] 
# zeros = np.zeros_like(b)

# Display the individual channels
# cv.imshow('Blue image',b)
# cv.imshow('Green image',g)
# cv.imshow('Red image',r)
# cv.waitKey(0)

# Display using matplotlib
# fig, axes = plt.subplots(1, 3, figsize=(12, 4)) # figsize specifies the size of the subplot in inches
# axes[0].imshow(cv.merge([b, zeros, zeros]))
# axes[0].set_title('Blue Channel')
# axes[0].axis('off')
# axes[1].imshow(cv.merge([zeros, g, zeros]))
# axes[1].set_title('Green Channel')
# axes[1].axis('off')
# axes[2].imshow(cv.merge([zeros, zeros, r]))
# axes[2].set_title('Red Channel')
# axes[2].axis('off')
# plt.show()

# ENHANCE A PARTICULAR CHANNEL
# img = cv.imread("walchand.jpeg")
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# b,g,r = cv.split(img) 
# enhanced_g = np.clip(g*1.5,0,255).astype(np.uint8)
# enhanced_img = cv.merge([b,enhanced_g,r])
# fig,axes = plt.subplots(1,2, figsize=(8,4))
# axes[0].imshow(img)
# axes[0].set_title("Original image")
# axes[0].axis('off')
# axes[1].imshow(enhanced_img)
# axes[1].set_title("Enhanced image")
# axes[1].axis('off')
# plt.show()
