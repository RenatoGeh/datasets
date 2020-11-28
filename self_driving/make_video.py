import sys
import math

import cv2
import numpy as np

if len(sys.argv) != 4:
  print("Usage: " + sys.argv[0] + " data n out")
  print("  data - dataset to generate video")
  print("  n    - number of frames")
  print("  out  - output filename")
  sys.exit(1)

WIDTH, HEIGHT = 45, 80
CHANNELS = 3

n = int(sys.argv[2])
if n < 0:
  n = math.inf

D = np.load(sys.argv[1])

V = cv2.VideoWriter(sys.argv[3], cv2.VideoWriter_fourcc(*"MJPG"), 1, (3*HEIGHT, 3*WIDTH))

SIZE = tuple([HEIGHT, WIDTH, CHANNELS])
NSIZE = tuple([3*HEIGHT, 3*WIDTH, CHANNELS])

for i, I in enumerate(D):
  if i >= n:
    break
  I = I.reshape((WIDTH, HEIGHT, CHANNELS))
  I = cv2.resize(I, (3*HEIGHT, 3*WIDTH), 0, 0, cv2.INTER_LINEAR)
  V.write(I.reshape(3*WIDTH, 3*HEIGHT, CHANNELS))

cv2.destroyAllWindows()
V.release()
