import csv
def getCOM():
    file = open("jewCOM_MD.csv","r")
    reader = csv.reader(file)
    lat = 0
    long = 0
    count = 0
    for row in reader:
        count+=1
        lat += float(row[0])
        long += float(row[1])
    COMLat = lat/count
    COMLong = long/count
    print(COMLat)
    print(COMLong)
    file.close()
getCOM()
