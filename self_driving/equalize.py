import sys

import numpy as np
import cv2
import matplotlib.pyplot as plt

def draw_hist(img):
  plt.hist(img.flatten(), MAX+1, [0, MAX+1], color='r')
  plt.show()

if len(sys.argv) < 3 or len(sys.argv) > 4:
  print("Usage: " + sys.argv[0] + " data out max")
  print("  data   - dataset containing images (in grayscale) and labels")
  print("  out    - output file")
  print("  max    - max pixel value")
  sys.exit(1)

D = np.load(sys.argv[1])
fout = sys.argv[2]

DEBUG=False
if len(sys.argv) > 3:
  MAX = int(sys.argv[3])
else:
  MAX = 255
k=255/MAX
W, H, C = 45, 80, 3
T, E = [], []
for i, I in enumerate(D):
  img, l = I[:-1], I[-1]
  eImg = cv2.equalizeHist(img)
  clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
  cImg = clahe.apply(img)
  if DEBUG:
    print(eImg.shape, cImg.shape, img.shape)
    res = np.hstack((k*img.reshape(W, H), eImg.reshape(W, H), k*cImg.reshape(W, H)))
    draw_hist(img)
    draw_hist(eImg)
    draw_hist(cImg)
    plt.imshow(res, cmap='gray')
    plt.show()
  T.append(np.append(eImg/k, l))

T = np.asarray(T).astype('uint8')
np.save(fout, T)
