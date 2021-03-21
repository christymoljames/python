import csv
f=open("F:\python\Book2.csv",'r')
content=csv.reader(f)
for x in content:
    print(x)