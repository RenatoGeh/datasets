#!/bin/bash

t=("test" "train" "valid")

b=""
c=""
if [ "$#" -eq 1 ]; then
  b="$1"
  c="_$b"
fi

for u in ${t[@]}; do
  #b=$(basename $f)
  python3 transform.py "raw/${u}_data.npy" "raw/${u}_labels.npy" "transformed/${u}${c}.npy" $b
done
