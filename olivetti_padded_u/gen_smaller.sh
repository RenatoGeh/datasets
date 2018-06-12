#!/bin/bash

resize=1

if [ "$#" -eq 1 ]; then
  resize=0
elif [ "$#" -ne 3 ]; then
  echo "Usage: $0 n w h"
  echo "  n - number of samples per class"
  echo "  w - width to resize"
  echo "  h - height to resize"
  exit 1
fi

path="../olivetti_small/"

echo "Creating directories..."
for i in `seq 0 39`; do
  mkdir -p "$path$i"
done

n=$1
w=$2
h=$3
for i in `seq 0 39`; do
  echo "Class $i:"
  for j in `seq 1 $n`; do
    if ! (( i % 2 )); then
      m=0
    else
      m=10
    fi
    let k=m+j
    let p=(i+2)/2
    f="$i/grid_${p}x${k}.pgm"
    echo "$f"
    if [ "$resize" -eq 1 ]; then
      convert "$f" -resize "$w"x"$h" "$path$f"
    else
      cp "$f" "$path$f"
    fi
  done
  echo "  done"
done
