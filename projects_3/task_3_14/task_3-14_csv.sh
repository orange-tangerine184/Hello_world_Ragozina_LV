#!/bin/bash

echo "Название товара: "
awk -F "," 'NF > 0 {print $2}' data.csv

echo -e "\nТовары, дороже 20: "
awk -F "," 'NF > 0 {if ($3 >20) print $2, $3}' data.csv

echo -e "\nОбщая стоимость: "
awk -F "," 'NF > 0 {sum += $3} END {print sum}' data.csv
