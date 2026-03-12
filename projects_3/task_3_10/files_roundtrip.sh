#!/bin/bash

for i in {1..10}; do
    touch "test${i}.txt"
    echo "Появился файл ${i} ;)"
done

i=10
while [ $i -ge 1 ]; do
    rm "test${i}.txt"
    echo "Минус файл ${i} :("
    i=$((i - 1))
done
