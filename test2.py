import os
import csv
def test():
    file1 = open("zip centers.csv")
    reader1 = csv.reader(file1, delimiter=',')
    for row1 in reader1:
        file2 = open("combined.csv")
        reader2 = csv.reader(file2, delimiter=',')
        for row2 in reader2:
            #print(row1[0])
            #print(row2[0])
            if(row1[0] == row2[0]):
                out_file = open("allState.csv", 'a')
                writer = csv.writer(out_file)
                writer.writerow([row1[0], row2[1], row1[1], row1[2]])
                out_file.close()
        file2.close()   
if __name__ == "__main__":
    main()
