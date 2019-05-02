import numpy as np
import matplotlib.pyplot as plt
import cv2

img=cv2.imread('DeathNote.jpg',0)

for i in range(0,225):
    for j in range(0,225):
         a=img[i][j] # Replace this line with your 90x100 numpy array.
a = np.expand_dims(a, axis = 2)
a = np.concatenate((a, a, a), axis = 2)
print(a.shape)
# (90, 100, 3)

for y in a:
  plt.imshow(y)
  plt.show()
