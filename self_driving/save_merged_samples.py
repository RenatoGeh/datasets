import sys
import random

import numpy as np
import cv2

if len(sys.argv) < 4 or len(sys.argv) > 5:
  print("Usage: " + sys.argv[0] + " data n outdir max")
  print("  data   - dataset to sample")
  print("  n      - number of samples to extract")
  print("  outdir - directory to save samples in")
  print("  max    - max pixel value")
  sys.exit(1)

n = int(sys.argv[2])
D = np.load(sys.argv[1])
path = sys.argv[3]

max = 255
if len(sys.argv) == 5:
    max = int(sys.argv[4])-1
k = 255/max

DIRS = ["up", "left", "right"]

m = len(D)
R = []
for i in range(n):
  while True:
    j = random.randrange(m)
    if j not in R:
      break
  R.append(j)
  I = (D[j,:-1]*k).reshape(45, 80)
  l = D[j,-1]
  cv2.imwrite(path + "/" + DIRS[l] + "_" + str(j) + ".png", I)

