import csv

data = []

with open("data.csv", "r") as f:

    csvReader = csv.reader(f)

    for row in csvReader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

#Converting all the planet names to lower case
for data_point in planet_data:
    data_point[0] = data_point[0].lower()

#Sorting the planet names in alphabetical order
planet_data.sort(key = lambda planet_data: planet_data[0])

#You can even use "append" mode at the file type bellow like this > ("a+")
with open("data_sorted.csv", "w") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)