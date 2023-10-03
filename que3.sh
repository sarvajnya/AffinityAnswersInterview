#!/bin/bash

# Input URL
input_url="https://www.amfiindia.com/spages/NAVAll.txt"

# Output TSV file
output_file="output_data.tsv"

# Logic
curl -s "$input_url" | awk -F';' '{print $4 "\t" $5}' > "$output_file"

echo "Successfull"
