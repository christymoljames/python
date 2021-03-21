import csv
with open("F:\python\Book1.csv", newline="") as csvfile:
    data = csv.reader(csvfile, delimiter=" ", quotechar="|")
    for row in data:
        print(",".join(row))


