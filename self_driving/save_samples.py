import sys
import random

import numpy as np
import cv2

if len(sys.argv) != 4:
  print("Usage: " + sys.argv[0] + " data n outdir")
  print("  data   - dataset to sample")
  print("  n      - number of samples to extract")
  print("  outdir - directory to save samples in")
  sys.exit(1)

n = int(sys.argv[2])
D, L = np.load(sys.argv[1] + "_data.npy"), np.load(sys.argv[1] + "_labels.npy")
path = sys.argv[3]

DIRS = ["up", "left", "right"]

m = len(D)
R = []
for i in range(n):
  while True:
    j = random.randrange(m)
    if j not in R:
      break
  R.append(j)
  I = D[j].reshape(45, 80, 3)
  l = L[j]
  cv2.imwrite(path + "/" + DIRS[l] + "_" + str(j) + ".png", I)

