# A new row can be added to an existing CSV file using the csv library with append mode 'a'.

import csv

new_row = [106, "Tom", 24, "Chemistry", ""]
with open("YOUR CSV FILE", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(new_row)