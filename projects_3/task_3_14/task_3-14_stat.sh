#!/bin/bash

echo "Сумма всех оценок: "
awk 'NF > 0 {sum += $2} END {print sum}' students.txt

echo -e "\nСредняя оценка: "
awk 'NF > 0 {sum += $2; n++}  END {printf "%.2f\n", sum/n}' students.txt

echo -e "\nМаксимальная оценка: "
awk 'NF > 0 {if (NR==1) max=$2; if ($2 > max) max=$2} END{print max}' students.txt
