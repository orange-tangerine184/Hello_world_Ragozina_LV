#!/bin/bash

read -p "Введите ваш рост (в метрах): " HEIGHT
read -p "Введите ваш вес (в кг): " WEIGHT

BMI=$(echo "scale=2; $WEIGHT / ($HEIGHT ^ 2)" | bc)

echo "Ваш индекс массы тела равен $BMI"
