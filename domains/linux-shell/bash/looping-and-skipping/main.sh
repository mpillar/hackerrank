#!/bin/bash
set -eu

for i in {1..99}
do
    if [ $((i%2)) -ne 0 ]
    then
        echo $i
    fi
done
