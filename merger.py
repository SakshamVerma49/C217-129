import csv

dataSet1 = []
dataSet2 = []

with open("Final.csv", "r") as f:
    csvReader = csv.reader(f)

    for row in csvReader:
        dataSet1.append(row)

with open("data_sorted.csv", "r") as f:
    csvReader = csv.reader(f)

    for row in csvReader:
        dataSet2.append(row)

#The first row of each data file gets stored in "headers1" and "headers2" respectively
headers1 = dataSet1[0]
headers2 = dataSet2[0]

#Setting the value of headers1 and headers2 in a single variable called "headers"
headers = headers1 + headers2

planetData1 = dataSet1[1:]
planetData2 = dataSet2[1:]

planet_data = []

for index, data_row in enumerate(planetData1):
    planet_data.append(planetData1[index] + (planetData2[index]))

with open("merged.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)