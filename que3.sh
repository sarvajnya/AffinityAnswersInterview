#!/bin/bash

# Input URL
input_url="https://www.amfiindia.com/spages/NAVAll.txt"

# Output TSV file
output_file="output_data.tsv"

# Logic
if curl -s "$input_url" | awk -F';' '{print $4 "\t" $5}' > "$output_file"; then
    echo "Successfull"
else
    echo "Unsuccessfull"
fi

