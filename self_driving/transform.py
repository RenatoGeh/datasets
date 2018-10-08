import sys

import cv2
import numpy as np
import matplotlib.pyplot as pt

W = 45
H = 80
C = 3

UP = 0
LEFT = 1
RIGHT = 2
DIR = {0: 'up', 1: 'left', 2: 'right'}

def flip_label(l):
  if l == LEFT:
    return RIGHT
  return LEFT

DEBUG = False

if len(sys.argv) < 4 or len(sys.argv) > 5:
  print("Converts to grayscale and flips left and right labeled images.")
  print("Usage:", sys.argv[0], "data labels out [b]")
  print("  data   - dataset containing only images")
  print("  labels - dataset containing only labels")
  print("  out    - output file")
  print("  b      - bits for resolution")
  sys.exit(1)

if DEBUG:
  print("Loading...")
D, L = np.load(sys.argv[1]), np.load(sys.argv[2])
if DEBUG:
  print("Loaded")

K = []
res = 255
if len(sys.argv) >= 5:
  b = int(sys.argv[4])
  res = 2 << b-1
if res >= 255:
  q = None
else:
  q = (res-1)/255

i = 0
for I in D:
  if DEBUG:
    print("Instance", i, "labelled as", DIR[L[i]])
  M = np.reshape(I, (W, H, C))
  if DEBUG:
    print("Reshaped to ", (W, H, C))
  g = cv2.cvtColor(M, cv2.COLOR_RGB2GRAY)
  if q is not None:
    g = g*q
  if DEBUG:
    print("Converted to grayscale")
    pt.imshow(g, cmap="gray")
    pt.show()
    print("Next...")
  if L[i] == LEFT or L[i] == RIGHT:
    if DEBUG:
      print("Flipping to", DIR[flip_label(L[i])])
      print(g.shape)
    hi = np.flip(g, axis=1)
    h = np.asarray(hi.flatten().astype('uint8'))
    if DEBUG:
      pt.imshow(hi, cmap="gray")
      pt.show()
    K.append(np.append(h, flip_label(L[i])))
  g = np.asarray(g.flatten().astype('uint8'))
  K.append(np.append(g, L[i]))
  i += 1
K = np.asarray(K).astype('uint8')

if DEBUG:
  print("Saving...")
np.save(sys.argv[3], K)
if DEBUG:
  print("Saved")
