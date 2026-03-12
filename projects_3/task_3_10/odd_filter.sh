#!/bin/bash

for i in {1..20}; do
    [ $i -eq 15 ] && { echo "Stop, нашли 15"; break; }
    [ $((i % 2)) -eq 0 ] && continue
    echo "$i"
done
