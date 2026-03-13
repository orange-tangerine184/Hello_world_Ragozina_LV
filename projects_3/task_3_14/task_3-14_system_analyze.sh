#!/bin/bash

df -h | awk 'NR>1 {
    system_fill = $5
    gsub(/%/, "", system_fill)
    warning = ""
     if (system_fill+0 > 90)
        warning="Предупреждение! Тут больше 90% заполнено"

    print $1, $5, warning
}'
