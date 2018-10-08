import sys

import numpy as np

if len(sys.argv) != 5:
  print("Usage: " + sys.argv[0] + " data o_max n_max out")
  print("  data  - dataset containing images (in grayscale) and labels")
  print("  o_max - original images (contained in data) max pixel value")
  print("  n_max - new max pixel value")
  print("  out   - output file")
  sys.exit(1)

D = np.load(sys.argv[1])
p, q = int(sys.argv[2])-1, int(sys.argv[3])-1
fout = sys.argv[4]

W, H, C = 45, 80, 3
k = q/p
Q = []

for i, I in enumerate(D):
  img, l = I[:-1], I[-1]
  q = (img*k).astype('uint8')
  Q.append(np.append(q, l))
Q = np.asarray(Q).astype('uint8')

np.save(fout, Q)
