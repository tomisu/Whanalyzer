import json
import re


pattern = re.compile("(\d+\/\d+\/\d+), (\d\d):(\d\d) - (.*?):(.*)")

data = []
line_count = 0

with open('./ocelotes.txt', 'r') as input_file:
    line = input_file.readline()
    total_line = line

    while line:
        if pattern.match(line):
            line_count += 1
            data.append([total_line])  # Appending a list with the whole line because I was stupid when I did the frontend.
            total_line = line
        else:
            total_line += line

        line = input_file.readline()

with open('./output.json', 'w') as output_file:
    json.dump(data, output_file)

print(f"Processed {line_count} messages")
