import numpy as np
import matplotlib.pyplot as plt
import cv2

import sys

if len(sys.argv) != 3:
  print("Usage: " + sys.argv[0] + " dataset max")
  print("  dataset - set of grayscale images in .npy format")
  print("  max     - max pixel value")
  sys.exit(1)

D = np.load(sys.argv[1])[:,:-1]
max = int(sys.argv[2])+1
hist, bins = np.histogram(D, max, [0, max])
print(len(hist), hist)
# hist /= 1000

plt.bar(np.arange(0, max), hist, 1)
plt.show()
