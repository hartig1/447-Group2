from appJar import gui
def changeState():
    state = s.app.getOptionBox("State")
def updateIncomeLower():
    file = open("iL.txt","w")
    s.userIncome = app.getScale("Average Household Income Lower Bound")
    s.userIncomeL = s.userIncome - s.incomeMin
    if(s.userIncomeL <= s.incomeInterval/2):
        s.userIncomeL = 1
        file.write(str(1))
    elif(s.userIncomeL >= s.incomeInterval/2 and s.userIncomeL <= 3*s.incomeInterval/2):
        s.userIncomeL = 2
        file.write(str(2))
    elif(s.userIncomeL >= 3*s.incomeInterval/2 and s.userIncomeL <= 5*s.incomeInterval/2):
        s.userIncomeL = 3
        file.write(str(3))
    elif(s.userIncomeL >= 5*s.incomeInterval/2 and s.userIncomeL <= 7*s.incomeInterval/2):
        s.userIncomeL = 4
        file.write(str(4))
    else:
        s.userIncomeL= 5
        file.write(str(5))
    app.setLabel("Income","You have selected average household income: " + str(s.userIncome) + " which is in quintile #" + str(s.userIncomeL))
    file.close()
def updateDistLower():
    file = open("dL.txt","w")
    s.userDist = app.getScale("Distance from COM Lower Bound")
    s.userDistL = s.userDist - s.distMin
    if(s.userDistL <= s.distInterval/2):
        s.userDistL = 1
        file.write(str(1))
    elif(s.userDistL >= s.distInterval/2 and s.userDistL <= 3*s.distInterval/2):
        s.userDistL = 2
        file.write(str(2))
    elif(s.userDistL >= 3*s.distInterval/2 and s.userDistL <= 5*s.distInterval/2):
        s.userDistL = 3
        file.write(str(3))
    elif(s.userDistL >= 5*s.distInterval/2 and s.userDistL <= 7*s.distInterval/2):
        s.userDistL = 4
        file.write(str(4))
    else:
        s.userDistL = 5
        file.write(str(5))
    app.setLabel("Dist","Your selected distance from COM: " + str(s.userDist) + " which is in quintile #" + str(s.userDistL))
    file.close()
def updateRobberiesLower():
    s.userCrime = app.getScale("% chance of being robbed in a year lower bound")
    s.userCrimeL = s.userCrime - s.crimeMin
    file = open("cL.txt","w")
    if(s.userCrimeL <= s.crimeInterval/2):
        s.userCrimeL = 1
        file.write(str(1))
    elif(s.userCrimeL >= s.crimeInterval/2 and s.userCrimeL <= 3*s.crimeInterval/2):
        s.userCrimeL = 2
        file.write(str(2))
    elif(s.userCrimeL >= 3*s.crimeInterval/2 and s.userCrimeL <= 5*s.crimeInterval/2):
        s.userCrimeL = 3
        file.write(str(3))
    elif(s.userCrimeL >= 5*s.crimeInterval/2 and s.userCrimeL <= 7*s.crimeInterval/2):
        s.userCrimeL = 4
        file.write(str(4))
    else:
        s.userCrimeL = 5
        file.write(str(5))
    app.setLabel("Crime","You have selected: ." + str(s.userCrime).zfill(4) + "%  chance of being robbed in a year, which is in quintile #" + str(s.userCrimeL))
    file.close
def updateIncomeUpper():
    file = open("iU.txt","w")
    s.userIncome = app.getScale("Average Household Income Upper Bound")
    s.userIncomeU = s.userIncome - s.incomeMin
    if(s.userIncomeU <= s.incomeInterval/2):
        s.userIncomeU = 1
        file.write(str(1))
    elif(s.userIncomeU >= s.incomeInterval/2 and s.userIncomeU <= 3*s.incomeInterval/2):
        s.userIncomeU = 2
        file.write(str(2))
    elif(s.userIncomeU >= 3*s.incomeInterval/2 and s.userIncomeU <= 5*s.incomeInterval/2):
        s.userIncomeU = 3
        file.write(str(3))
    elif(s.userIncomeU >= 5*s.incomeInterval/2 and s.userIncomeU <= 7*s.incomeInterval/2):
        s.userIncomeU = 4
        file.write(str(4))
    else:
        s.userIncomeU = 5
        file.write(str(5))
    app.setLabel("Income","You have selected average household income: " + str(s.userIncome) + " which is in quintile #" + str(s.userIncomeU))
    file.close()
def updateDistUpper():
    file = open("dU.txt","w")
    s.userDist = app.getScale("Distance from COM Upper Bound")
    s.userDistU = s.userDist - s.distMin
    if(s.userDistU <= s.distInterval/2):
        s.userdistU = 1
        file.write(str(1))
    elif(s.userDistU >= s.distInterval/2 and s.userDistU <= 3*s.distInterval/2):
        s.userDistU = 2
        file.write(str(2))
    elif(s.userDistU >= 3*s.distInterval/2 and s.userDistU <= 5*s.distInterval/2):
        s.userDistU = 3
        file.write(str(3))
    elif(s.userDistU >= 5*s.distInterval/2 and s.userDistU <= 7*s.distInterval/2):
        s.userDistU = 4
        file.write(str(4))
    else:
        s.userDistU = 5
        file.write(str(5))
    app.setLabel("Dist","You have selected distance from COM: " + str(s.userDist) + " which is in quintile #" + str(s.userDistU))
    file.close()
def updateRobberiesUpper():
    file = open("cU.txt","w")
    s.userCrime = app.getScale("% chance of being robbed in a year upper bound")
    s.userCrimeU = s.userCrime - s.crimeMin
    if(s.userCrimeU <= s.crimeInterval/2):
        s.userCrimeU = 1
        file.write(str(1))
    elif(s.userCrimeU >= s.crimeInterval/2 and s.userCrimeU <= 3*s.crimeInterval/2):
        s.userCrimeU = 2
        file.write(str(2))
    elif(s.userCrimeU >= 3*s.crimeInterval/2 and s.userCrimeU <= 5*s.crimeInterval/2):
        s.userCrimeU = 3
        file.write(str(3))
    elif(s.userCrimeU >= 5*s.crimeInterval/2 and s.userCrimeU <= 7*s.crimeInterval/2):
        s.userCrimeU = 4
        file.write(str(4))
    else:
        s.userCrimeU = 5
        file.write(str(5))
    file.close()
    app.setLabel("Crime","You have selected: ." + str(s.userCrime).zfill(4) + "%  chance of being robbed in a year, which is in quintile #" + str(s.userCrimeU))
def enterUpper():
    file = open("metaData.txt","w")
    file.write(str(s.userIncomeL) + "," + str(s.userCrimeL))
    file.close()
    app.hideButton("NEXT")
    app.showButton("BACK")
    app.showButton("DONE")
    app.hideScale("Distance from COM Lower Bound")
    app.hideScale("Average Household Income Lower Bound")
    app.hideScale("% chance of being robbed in a year lower bound")
    app.showScale("Average Household Income Upper Bound")
    app.showScale("% chance of being robbed in a year upper bound")
    app.showScale("Distance from COM Upper Bound")
    app.hideLabel("Please choose your lower bound for the following")
    app.showLabel("Please choose your upper bound for the following")
    app.setScale("% chance of being robbed in a year upper bound", s.crimeMax)
    app.setScale("Average Household Income Upper Bound", s.incomeMax)
    app.setScale("Distance from COM Upper Bound", s.distMax)
def returnLower():
    app.hideButton("BACK")
    app.showButton("NEXT")
    app.hideButton("DONE")
    app.hideScale("Distance from COM Upper Bound")
    app.hideScale("Average Household Income Upper Bound")
    app.hideScale("% chance of being robbed in a year upper bound")
    app.showScale("Distance from COM Lower Bound")
    app.showScale("Average Household Income Lower Bound")
    app.showScale("% chance of being robbed in a year lower bound")
    app.setScale("Distance from COM Lower Bound", s.distMin)
    app.setScale("Average Household Income Lower Bound", s.incomeMin)
    app.setScale("% chance of being robbed in a year lower bound", s.crimeMin)
def finish():
    file = open("iL.txt", "r")
    iL = int(file.read())
    file.close()
    file = open("iU.txt", "r")
    iU = int(file.read())
    file.close()
    file = open("cL.txt", "r")
    cL = int(file.read())
    file.close()
    file = open("cU.txt", "r")
    cU = int(file.read())
    file.close()
    file = open("dL.txt", "r")
    dL = int(file.read())
    file.close()
    file = open("dU.txt", "r")
    dU = int(file.read())
    file.close()
    if(iL <= iU and cL <= cU and dL <= dU):
        app.stop()
    else:
        app.showLabel("Error")
app=gui("ROBBR")
class store:
    def __init__(self):
        self.userIncomeL = 1
        self.userCrimeL = 1
        self.userDistL = 1
        self.userIncomeU = 5
        self.userCrimeU = 5
        self.userDistU = 5
        self.incomeMin = None
        self.incomeMax = None
        self.crimeMin = None
        self.crimeMax = None
        self.distMin = None
        self.distMax = None
        self.userCrime = None
        self.userIncome = None
        self.userDist = None
s = store()
def QuintileGUI(iMI, iMA, cMI, cMA, dMI, dMA):
    file = open("iL.txt", "w")
    file.write("1")
    file.close()
    file = open("iU.txt", "w")
    file.write("5")
    file.close()
    file = open("cL.txt", "w")
    file.write("1")
    file.close()
    file = open("cU.txt", "w")
    file.write("5")
    file.close()
    file = open("dL.txt", "w")
    file.write("1")
    file.close()
    file = open("dU.txt", "w")
    file.write("5")
    file.close()
    s.incomeMin = iMI
    s.incomeMax = iMA
    s.crimeMin = cMI * 10000
    s.crimeMax = cMA * 10000
    s.distMin = dMI
    s.distMax = dMA
    s.incomeInterval = float((s.incomeMax-s.incomeMin)/4)
    s.crimeInterval = int((cMA-cMI)*10000/4)
    s.distInterval = float((s.distMax-s.distMin)/4)
    app.addLabel("Please choose your lower bound for the following")
    app.addLabel("Please choose your upper bound for the following")
    app.hideLabel("Please choose your upper bound for the following")

    app.addLabel("Income", "You have selected average household income: " +str (s.incomeMin) + " which is in quintile #1")

    app.addLabelScale("Average Household Income Lower Bound")
    app.setScaleChangeFunction("Average Household Income Lower Bound", updateIncomeLower)
    app.setScaleRange("Average Household Income Lower Bound", s.incomeMin, s.incomeMax)
    app.setScaleIncrement("Average Household Income Lower Bound", s.incomeInterval)
    #app.showScaleIntervals("Average Household Income Lower Bound", s.incomeInterval)
    s.userIncome = app.getScale("Average Household Income Lower Bound")

    app.addLabelScale("Average Household Income Upper Bound")
    app.setScaleChangeFunction("Average Household Income Upper Bound", updateIncomeUpper)
    app.setScaleRange("Average Household Income Upper Bound", s.incomeMin, s.incomeMax)
    #app.showScaleIntervals("Average Household Income Upper Bound", s.incomeInterval)
    s.userIncome = app.getScale("Average Household Income Upper Bound")
    app.hideScale("Average Household Income Upper Bound")

    app.addLabel("Crime","You have selected: ." + str(s.crimeMin).zfill(4) + "%  chance of being robbed in a year, which is in quintile #1")
    app.setScaleIncrement("Average Household Income Upper Bound", s.incomeInterval)

    app.addLabelScale("% chance of being robbed in a year lower bound")
    app.setScaleChangeFunction("% chance of being robbed in a year lower bound", updateRobberiesLower)
    app.setScaleRange("% chance of being robbed in a year lower bound", s.crimeMin, s.crimeMax)
    app.setScaleIncrement("% chance of being robbed in a year lower bound", s.crimeInterval)
    #app.showScaleIntervals("% chance of being robbed in a year lower bound", s.crimeInterval)
    s.userCrime = app.getScale("% chance of being robbed in a year lower bound")

    app.addLabelScale("% chance of being robbed in a year upper bound")
    app.setScaleChangeFunction("% chance of being robbed in a year upper bound", updateRobberiesUpper)
    app.setScaleRange("% chance of being robbed in a year upper bound", s.crimeMin, s.crimeMax)
    app.setScaleIncrement("% chance of being robbed in a year upper bound", s.crimeInterval)
    #app.showScaleIntervals("% chance of being robbed in a year upper bound", s.crimeInterval)
    s.userCrime = app.getScale("% chance of being robbed in a year upper bound")
    app.hideScale("% chance of being robbed in a year upper bound")

    app.addLabel("Dist","You have selected: " + str(s.distMin) + " which is in quiltile #1")

    app.addLabelScale("Distance from COM Upper Bound")
    app.setScaleChangeFunction("Distance from COM Upper Bound", updateDistUpper)
    app.setScaleRange("Distance from COM Upper Bound", s.distMin, s.distMax)
    app.setScaleIncrement("Distance from COM Upper Bound", s.distInterval)
    #app.showScaleIntervals("Distance from COM Upper Bound", s.distInterval)
    s.userIncome = app.getScale("Distance from COM Upper Bound")
    app.hideScale("Distance from COM Upper Bound")

    app.addLabelScale("Distance from COM Lower Bound")
    app.setScaleChangeFunction("Distance from COM Lower Bound", updateDistLower)
    app.setScaleRange("Distance from COM Lower Bound", s.distMin, s.distMax)
    app.setScaleIncrement("Distance from COM Lower Bound", s.distInterval)
    #app.showScaleIntervals("Distance from COM Lower Bound", s.distInterval)
    s.userCrime = app.getScale("Distance from COM Lower Bound")

    app.addLabel("Error", "Upper bound must be greater than or equal to lower bound")
    app.hideLabel("Error")

    app.addButtons(["NEXT"], enterUpper)
    app.addButtons(["BACK"], returnLower)
    app.hideButton("BACK")
    app.addButtons(["DONE"], finish)
    app.hideButton("DONE")

    app.go()
    file = open("iL.txt", "r")
    iL = int(file.read())
    file.close()
    file = open("iU.txt", "r")
    iU = int(file.read())
    file.close()
    file = open("cL.txt", "r")
    cL = int(file.read())
    file.close()
    file = open("cU.txt", "r")
    cU = int(file.read())
    file.close()
    file = open("dL.txt", "r")
    dL = int(file.read())
    file.close()
    file = open("dU.txt", "r")
    dU = int(file.read())
    file.close()
    return iL, iU, cL, cU, dL, dU
if __name__ == "__main__":
    QuintileGUI(0,100,0,100,0,100)
