#!/bin/bash

echo "Студенты с оценкой выше 80: "
awk 'NF > 0 && $2 > 80 {print $1}' students.txt

echo -e "\nСтуденты с оценкой ниже 70: "
awk 'NF > 0 && $2 < 70 {print $1}' students.txt

echo -e "\nПервая строка файла: "
awk 'NR==1' students.txt
