# A CSV file can be created using Python's csv library by writing rows of data into a CSV file.

import csv

data = [
    ['Name', 'Age', 'City'],
    ['AAA', 20, 'NYC'],
    ['BBB', 21, 'IL'],
    ['CCC', 22, 'LA']
]
with open('my_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("CSV created")