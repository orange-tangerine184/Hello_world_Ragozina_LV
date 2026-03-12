#!/bin/bash

printf "%-25s %-7s %-7s %-7s %-7s\n" "Файл" "A" "T" "G" "C"

for file in *.fasta; do
    if [ ! -s "$file" ]; then
        continue
    fi

    sequence=$(grep -v "^>" "$file" | tr -d '\n' | tr -d ' ')

    count_A=$(echo "$sequence" | grep -o "A" | wc -l)
    count_T=$(echo "$sequence" | grep -o "T" | wc -l)
    count_G=$(echo "$sequence" | grep -o "G" | wc -l)
    count_C=$(echo "$sequence" | grep -o "C" | wc -l)

    printf "%-20s %-7s %-7s %-7s %-7s\n" "$file" "$count_A" "$count_T" "$count_G" "$count_C"
done
