import numpy as np
import matplotlib.pyplot as plt

import sys

if len(sys.argv) != 3:
  print("Usage: " + sys.argv[0] + " dataset max")
  print("  dataset - the dataset containing images and labels in .npy format")
  print("  max     - max pixel value")
  sys.exit(1)

T = np.load(sys.argv[1])
D, L = T[:,:-1], T[:,-1]

DIRS = ["up", "left", "right"]

for i, img in enumerate(D):
  print("Label: " + DIRS[L[i]])
  plt.imshow(img.reshape(45, 80), cmap="gray")
  plt.show()
