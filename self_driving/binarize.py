import sys

import numpy as np
import cv2
import matplotlib.pyplot as plt

if len(sys.argv) != 3:
  print("Usage: " + sys.argv[0] + " data out")
  print("  data   - dataset containing images (in grayscale) and labels")
  print("  out    - output file")
  sys.exit(1)

D = np.load(sys.argv[1])
fout = sys.argv[2]

W, H, C = 45, 80, 3
T = []
for i, I in enumerate(D):
  img, l = I[:-1], I[-1]
  # gImg = cv2.cvtColor(np.reshape(I, (W, H, C)), cv2.COLOR_RGB2GRAY)
  gImg = cv2.GaussianBlur(img, (1, 1), 1, 1, cv2.BORDER_REFLECT)
  # bImg = cv2.adaptiveThreshold(gImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 1)
  _, bImg = cv2.threshold(gImg, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  bImg = (bImg.flatten()/255).astype('uint8')
  # plt.imshow(bImg, cmap='gray')
  # plt.show()
  T.append(np.append(bImg, l))

T = np.asarray(T).astype('uint8')
np.save(fout, T)
