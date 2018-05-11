import os
import csv


path = os.getcwd()

with open("data1.csv", "rb") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    current_zip = ""
    for row in reader:
    	current_zip = row[0].zfill(5)
        print(current_zip)
        two_directory = path + "/" + current_zip[:2] + "/"
        if not os.path.exists(two_directory):
    		os.makedirs(two_directory)
    	three_directory = two_directory + current_zip[:3] + "/"
    	if not os.path.exists(three_directory):
    		os.makedirs(three_directory)
        out_file = open(three_directory + current_zip + "Housing.csv", 'a')
        writer = csv.writer(out_file)
        writer.writerow([row[1], row[2]])
       	out_file.close()
