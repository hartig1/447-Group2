# File Name: Zip.py
# File Version: 1.0
# Developers: Adam Snyder and Wyatt Schweitzer
# Description: Holds the data necessary for the operation of the Zip object
# Inputs: Data stored on USB and user input
# Outputs: information for a given United States Zip Code
# Is primarily in edited by the processing component of ROBBR
# Import description here
# No known bugs as of this version

###################################################################
###################################################################


class Zip:
    def __init__(self, crime, jew_dist):
        self.crime = crime
        self.jew_dist = jew_dist

    def getCrime(self):
        return self.crime

    def getJewDist(self):
        return self.jew_dist

    def setScore(self, score):
        self.score = score
