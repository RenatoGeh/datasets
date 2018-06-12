#!/bin/bash

for i in `seq 0 39`; do
  for j in `seq 1 10`; do
    convert "$i/$j.pgm" -compress none "$i/${j}_ascii.pgm"
  done
done
