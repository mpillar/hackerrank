#!/bin/bash
set -eu
cd $(dirname $0)

for make in $(find domains -name Makefile)
do
    cd $(dirname $make) 1>/dev/null 2>/dev/null
    echo "-------------------------------------------------------------------------------"
    echo "Running:" $(dirname $make)
    eval $(which make)
    cd - 1>/dev/null 2>/dev/null
done
