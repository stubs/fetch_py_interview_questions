#!/bin/bash
cd fetch_py_problems_output
for filename in *.txt
do
    (cat "${filename}") > "ex${filename%.*}.py"
done
cd ..
