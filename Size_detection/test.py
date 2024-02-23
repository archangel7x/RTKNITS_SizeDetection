import csv

data = [[10,20,30],[40,50,60],[70,80,90]]
file = open("detection.csv","w")

writer =csv.writer(file)
for row in data:
    print(row)
    writer.writerow(row)
file.close()