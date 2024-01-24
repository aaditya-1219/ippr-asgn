import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

# INVERT ALL CHANNELS
img = cv.imread("walchand.jpeg")
rgb_img = cv.cvtColor(img,cv.COLOR_BGR2RGB)
b,g,r = cv.split(img)
B = np.array(b)
B = 255-B
G = np.array(g)
G = 255-G
R = np.array(r)
R = 255-R
fig,axes = plt.subplots(1,2, figsize=(8,4))
axes[0].imshow(rgb_img)
axes[0].set_title("Original image")
axes[0].axis('off')
axes[1].imshow(cv.merge([R,G,B]))
axes[1].set_title("Enhanced image")
axes[1].axis('off')
plt.show()