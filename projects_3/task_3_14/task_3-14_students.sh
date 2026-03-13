#!/bin/bash

echo "Имена студентов:"
awk 'NF > 0 {print $1}' students.txt

echo -e "\nОценки студентов: "
awk 'NF > 0 {print $2}' students.txt

echo -e "\nИмя и номер строки: "
awk 'NF{print ++n, $1}' students.txt
