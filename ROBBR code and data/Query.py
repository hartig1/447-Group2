# File Name: Query.py
# File Version: 1.0
# Developers: Adam Snyder and Wyatt Schweitzer
# Descripton: Holds the data necessary for the operation of the Query object
# Inputs: Data stored on USB and user input
# Outputs: rankList
# Is primarily in edited by the processing component of ROBBR
# Imports:
# 	Zip.py holds necessary data for the Zip objects, which hold
# 	information for each zip code
# No known bugs as of this version

###################################################################
###################################################################

from Zip import *
import csv
import os

class Query:
    def __init__(self, state):
        self.state = state
        self.zip_dict = {}
        self.zip_to_state = {}
        self.filterZips = []
        self.zipToState()
        self.getCrimeBounds()
        self.getIncBounds()
        self.getDistBounds()

    def getIncBounds(self):
        with open("stateMinMaxIncs.csv", "rb") as incomeFile:
            reader = csv.reader(incomeFile, delimiter=",")
            for row in reader:
                if row[0] == self.state:
                    self.min_income = float(row[1])
                    self.max_income = float(row[2])

    def getCrimeBounds(self):
        with open("stateMinMaxCrime.csv", "rb") as incomeFile:
            reader = csv.reader(incomeFile, delimiter=",")
            for row in reader:
                if row[0] == self.state:
                    self.min_crime = float(row[1])
                    self.max_crime = float(row[2])
    def getDistBounds(self):
        self.min_dist = 25
        self.max_dist = 100

    def zipToState(self):
        file = open("zipState.csv", 'r')
        contents = file.readlines()
        for items in contents:
            line = items.split(",")
            self.zip_to_state[line[0]] = line[1].strip()
        file.close()
    # populates zip_dict, which is a dictionary of considered zip codes
    def popZipDict(self):
        for index in range(1 + self.income_min + self.income_max):
            try:
                with open("States/" + self.state + "Q" + str(index + self.income_min) + ".csv", "r") as file:
                    reader = csv.reader(file,delimiter=',')
                    for row in reader:
                        zipDict[row[0]] = Zip(row[1], row[2])
            except:
                file = open("zipStates.csv")
                reader = csv.reader(file,delimiter=',')
                for row in reader:
                    if(row[1] == self.state):
                        out_file = open("combined.csv", 'a')
                        writer = csv.writer(out_file)
                        writer.writerow([row[0],row[1]])
                        out_file.close()
    def filter(self):
        try:
            for zip_code in zipDict:
                if zipDict[zip_code].crime >= self.crime_lower and zipDict[zip_code].crime <= self.crime_upper and zipDict[zip_code].jew_dist >= self.dist_lower and zipDict[zip_code].jew_dist <= self.dist_upper:
                    self.filterZips.append(zip_code)
        except:
            file = open("AGI.csv", "r")
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                #print(row)
                if(row[0] == "state"):
                    continue
                if(int(row[2]) >= self.income_lower and int(row[2]) <= self.income_upper and row[0] == self.state):
                     #print("found")
                     out_file = open("incomeSorted.csv", 'a')
                     writer = csv.writer(out_file)
                     writer.writerow([row[1], row[2]])
                     out_file.close()
            file.close()
            file = open("incomeSorted.csv","r")
            reader = csv.reader(file,delimiter=",")
            for row in reader:
                file2 = open("filteredCrimeData.csv","rU")
                reader2 = csv.reader(file2,delimiter=",")
                for row2 in reader2:
                    try:
                        if(float(row2[1]) >= self.crime_lower and float(row2[1]) <= self.crime_upper and int(row2[0]) == int(row[0])):
                             #print("found")
                            out_file = open("crimeSorted.csv","a")
                            writer = csv.writer(out_file)
                            writer.writerow([row[0],row[1],row2[1]])
                            out_file.close()
                    except:
                        continue
    def findHouses(self):
        path = os.getcwd()
        file = open("crimeSorted.csv","r")
        reader = csv.reader(file,delimiter=",")
        for row in reader:
            #print(row)
            current_zip = row[0].zfill(5)
            #print(current_zip)
            two_directory = path + "/" + "House Folder" + "/" + current_zip[:2] + "/"
            three_directory = two_directory + current_zip[:3] + "/"
            #print(three_directory)
            if(os.path.exists(three_directory + current_zip + "Housing.csv")):
                file2 = open(three_directory + current_zip + "Housing.csv", "r")
                reader2 = csv.reader(file2,delimiter=",")
                for row2 in reader2:
                    out_file = open("houses.csv","a")
                    writer = csv.writer(out_file)
                    writer.writerow([row2[0],row2[1]])
                    out_file.close()
                    break
            else:
                print("No such path: " + three_directory + current_zip + "Housing.csv")
        # if not self.filterZips:
        #     for zip in self.filterZips:
        #         current_zip = zip
        #         #print(current_zip)
        #         two_directory = path + "/" + "House Folder" + "/" + current_zip[:2] + "/"
        #         three_directory = two_directory + current_zip[:3] + "/"
        #         #print(three_directory)
        #         if(os.path.exists(three_directory + current_zip + "Housing.csv")):
        #             file2 = open(three_directory + current_zip + "Housing.csv", "r")
        #             reader2 = csv.reader(file2,delimiter=",")
        #             for row2 in reader2:
        #                 out_file = open("houses.csv","a")
        #                 writer = csv.writer(out_file)
        #                 writer.writerow([row2[0],row2[1]])
        #                 out_file.close()
        #                 break
        #         else:
        #             print("No such path: " + three_directory + current_zip + "Housing.csv")
        # else:
        # path = os.getcwd()
        # file = open("crimeSorted.csv","r")
        # reader = csv.reader(file,delimiter=",")
        # for row in reader:
        #     #print(row)
        #     current_zip = row[0].zfill(5)
        #     #print(current_zip)
        #     two_directory = path + "/" + "House Folder" + "/" + current_zip[:2] + "/"
        #     three_directory = two_directory + current_zip[:3] + "/"
        #     #print(three_directory)
        #     if(os.path.exists(three_directory + current_zip + "Housing.csv")):
        #         file2 = open(three_directory + current_zip + "Housing.csv", "r")
        #         reader2 = csv.reader(file2,delimiter=",")
        #         for row2 in reader2:
        #             out_file = open("houses.csv","a")
        #             writer = csv.writer(out_file)
        #             writer.writerow([row2[0],row2[1]])
        #             out_file.close()
        #             break
        #     else:
        #         print("No such path: " + three_directory + current_zip + "Housing.csv")
        #     file.close()
    # def weighZips(self):
    def getCOM(self):
        file = open("jewCOM_MD.csv","r")
        reader = csv.reader(file)
        lat = 0
        long = 0
        count = 0
        for row in reader:
            count+=1
            lat += float(row[0])
            long += float(row[1])
        self.COMLat = lat/count
        self.COMLong = long/count
        print(self.COMLat)
        print(self.COMLong)
        # with open("JewCOM.csv", "rb") as jew_COM:
        #     com_Data = csv.reader(jew_COM, delimiter=",")
        #     print(com_Data)
        #     for row in com_Data:
        #         if row[0] == self.state:
        #             print(row[1] + ", " + row[2])
        #             return row[1], row[2]

    def setSelectedCrime(self, min, max):
        self.crime_min = min
        self.crime_max = max
        self.crimeQ1 = self.min_crime + 0*(self.max_crime-self.min_crime)/5
        self.crimeQ2 = self.min_crime + 1*(self.max_crime-self.min_crime)/5
        self.crimeQ3 = self.min_crime + 2*(self.max_crime-self.min_crime)/5
        self.crimeQ4 = self.min_crime + 3*(self.max_crime-self.min_crime)/5
        self.crimeQ5 = self.min_crime + 4*(self.max_crime-self.min_crime)/5
        if(self.crime_min == 1):
            self.crime_lower = self.crimeQ1
        elif(self.crime_min == 2):
            self.crime_lower = self.crimeQ2
        elif(self.crime_min == 3):
            self.crime_lower = self.crimeQ3
        elif(self.crime_min == 4):
            self.crime_lower = self.crimeQ4
        elif(self.crime_min == 5):
            self.crime_lower = self.crimeQ5
        else:
            print("Bad min")
            print(self.crime_min)
        if(self.crime_max == 1):
            self.crime_upper = self.crimeQ2
        elif(self.crime_max == 2):
            self.crime_upper = self.crimeQ3
        elif(self.crime_max == 3):
            self.crime_upper = self.crimeQ4
        elif(self.crime_max == 4):
            self.crime_upper = self.crimeQ5
        elif(self.crime_max == 5):
            self.crime_upper = self.max_crime
        else:
            print("Bad max")
            print(self.crime_max)
        #print(self.crime_lower)
        #print(self.crime_upper)
    def setSelectedDist(self, min, max):
        self.dist_min = min
        self.dist_max = max
        self.distQ1 = self.min_dist + 0*(self.max_dist-self.min_dist)/5
        self.distQ2 = self.min_dist + 1*(self.max_dist-self.min_dist)/5
        self.distQ3 = self.min_dist + 2*(self.max_dist-self.min_dist)/5
        self.distQ4 = self.min_dist + 3*(self.max_dist-self.min_dist)/5
        self.distQ5 = self.min_dist + 4*(self.max_dist-self.min_dist)/5
        if(self.dist_min == 1):
            self.dist_lower = self.distQ1
        elif(self.dist_min == 2):
            self.dist_lower = self.distQ2
        elif(self.dist_min == 3):
            self.dist_lower = self.distQ3
        elif(self.dist_min == 4):
            self.dist_lower = self.distQ4
        elif(self.dist_min == 5):
            self.dist_lower = self.distQ5
        else:
            print("Bad min")
            print(self.dist_min)
        if(self.dist_max == 1):
            self.dist_upper = self.distQ2
        elif(self.dist_max == 2):
            self.dist_upper = self.distQ3
        elif(self.dist_max == 3):
            self.dist_upper = self.distQ4
        elif(self.dist_max == 4):
            self.dist_upper = self.distQ5
        elif(self.dist_max == 5):
            self.dist_upper = self.max_dist
        else:
            print("Bad max")
            print(self.dist_max)
        #print(self.crime_lower)
        #print(self.crime_upper)
    def setSelectedIncome(self, min, max):
        self.income_min = min
        self.income_max = max
        self.incomeQ1 = self.min_income + 0*(self.max_income-self.min_income)/5
        self.incomeQ2 = self.min_income + 1*(self.max_income-self.min_income)/5
        self.incomeQ3 = self.min_income + 2*(self.max_income-self.min_income)/5
        self.incomeQ4 = self.min_income + 3*(self.max_income-self.min_income)/5
        self.incomeQ5 = self.min_income + 4*(self.max_income-self.min_income)/5
        if(min == 1):
            self.income_lower = self.incomeQ1
        elif(min == 2):
            self.income_lower = self.incomeQ2
        elif(min == 3):
            self.income_lower = self.incomeQ3
        elif(min == 4):
            self.income_lower = self.incomeQ4
        elif(min == 5):
            self.income_lower = self.incomeQ5
        else:
            print("Bad min")
            print(min)
        if(max == 1):
            self.income_upper = self.incomeQ2
        elif(max == 2):
            self.income_upper = self.incomeQ3
        elif(max == 3):
            self.income_upper = self.incomeQ4
        elif(max == 4):
            self.income_upper = self.incomeQ5
        elif(max == 5):
            self.income_upper = self.max_income
        else:
            print("Bad max")
            print(max)
        #print(self.income_lower)
        #print(self.income_upper)
    def getRankList(self):
        return self.rank_list

    def setMinIncome(self, min_income):
        self.min_income = min_income

    def setMaxIncome(self, max_income):
        self.max_income = max_income

    def setMinCrime(self, min_crime):
        self.min_crime = min_crime

    def setMaxCrime(self, max_crime):
        self.max_crime = max_crime

    def setMinJewDist(self, min_jew_dist):
        self.min_dist = min_jew_dist

    def setMaxJewDist(self, max_jew_dist):
        self.max_dist = max_jew_dist
