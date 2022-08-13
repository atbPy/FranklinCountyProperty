import csv

with open('downloads/Conveyances-2022-08-12.csv', newline='') as csvfile:
     conveyances = csv.reader(csvfile, delimiter=',', quotechar='|')
     for row in conveyances:
         print(len(row))
         print(row)