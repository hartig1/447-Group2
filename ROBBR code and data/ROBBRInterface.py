# File Name: ROBBRInterface.py
# File Version: 1.4
# Developers: Ryan Hartig
# Description: Controls the GUI that the user interacts with
# Pulls data from the USB
# Connects with ROBBR.py for data and control
# Inputs: Users choices for state, quintile, and weight
# Outputs: Map of Jewelry COM and Available houses
# Is primarily in edited by the processing component of ROBBR
# Import gui from appjar for the interface
# Import ROBBR, the control file
# No known bugs as of this version
from appJar import gui
#from ROBBR import *
def hideStart(win):
    app.hideButton("START")
    app.showOptionBox("State")
    app.showButton("NEXT")
    app.hideLabel("l1")
def stateSelected():
    if(app.getOptionBox("State") == None):
        app.showLabel("Must select a state")
    else:
        app.hideOptionBox("State")
        app.showLabel("Lower")
        g.state = app.getOptionBox("State")
        app.showScale("Average Household Income")
        app.showScale("Annual robberies per 100,000 people")
        app.showScale("Distance from center of mass")
        app.hideButton("NEXT")
        app.showLabel("Income")
        app.showLabel("Robberies")
        app.showLabel("Distance")
        app.showButton("BACK")
        app.showButton("DONE")
        app.hideLabel("Must select a state")
def confirmInputDone():
    app.showMap("Map")
    app.hideButton("Map")
    app.hideButton("DONE")
    app.hideLabel("Income")
    app.hideLabel("Robberies")
    app.hideLabel("Distance")
def returnState():
    app.showOptionBox("State")
    app.hideScale("Average Household Income")
    app.hideScale("Annual robberies per 100,000 people")
    app.hideScale("Distance from center of mass")
    app.showButton("NEXT")
    app.hideButton("BACK")
    app.hideButton("DONE")
    app.hideLabel("Lower")
    app.hideLabel("Income")
    app.hideLabel("Robberies")
    app.hideLabel("Distance")
def inputDone():
    app.hideScale("Average Household Income")
    app.hideScale("Annual robberies per 100,000 people")
    app.hideScale("Distance from center of mass")
    app.showButton("Map")
    app.hideButton("BACK")
    #app.showButton("EDIT")
    app.hideButton("DONE")
def returnInput():
    app.showScale("Average Household Income")
    app.showScale("Annual robberies per 100,000 people")
    app.showScale("Distance from center of mass")
    app.showButton("BACK")
    #app.hideButton("EDIT")
    app.showLabel("Income")
    app.showLabel("Robberies")
    app.showLabel("Distance")
    app.hideMap("Map")
def updateUserIncomeLower():
    userIncome = app.getScale("Average Household Income")
    g.userIncomeLower = userIncome - g.incomeMin
    if(g.userIncomeLower <= g.incomeInterval/2):
        g.userIncomeLower = 1
    elif(g.userIncomeLower >= g.incomeInterval/2 and g.userIncomeLower <= 3*g.incomeInterval/2):
        g.userIncomeLower = 2
    elif(g.userIncomeLower >= 3*g.incomeInterval/2 and g.userIncomeLower <= 5*g.incomeInterval/2):
        g.userIncomeLower = 3
    elif(g.userIncomeLower >= 5*g.incomeInterval/2 and g.userIncomeLower <= 7*g.incomeInterval/2):
        g.userIncomeLower = 4
    else:
        g.userIncomeLower = 5
    app.setLabel("Income","You have selected average household income lower board: " + str(userIncome) + " which is in quintile #" + str(g.userIncomeLower))

def updateUserRobberiesLower():
    userRobberies = app.getScale("Annual robberies per 100,000 people")
    g.userRobberyLower = userRobberies - g.robberyMin
    if(g.userRobberyLower <= g.robberyInterval/2):
        g.userRobberyLower = 1
    elif(g.userRobberyLower >= g.robberyInterval/2 and g.userRobberyLower <= 3*g.robberyInterval/2):
        g.userRobberyLower = 2
    elif(g.userRobberyLower >= 3*g.robberyInterval/2 and g.userRobberyLower <= 5*g.robberyInterval/2):
        g.userRobberyLower = 3
    elif(g.userRobberyLower >= 5*g.robberyInterval/2 and g.userRobberyLower <= 7*g.robberyInterval/2):
        g.userRobberyLower = 4
    else:
        g.userRobberyLower = 5
    app.setLabel("Robberies","You have selected annual robberies per 100,000 people lower board: " + str(userRobberies) + " which is in quintile #" + str(g.userRobberyLower))
def updateUserDistLower():
    userDist = app.getScale("Distance from center of mass")
    g.userDistLower = userDist - g.distMin
    if(g.userDistLower <= g.distInterval/2):
        g.userDistLower = 1
    elif(g.userDistLower >= g.distInterval/2 and g.userDistLower <= 3*g.distInterval/2):
        g.userDistLower = 2
    elif(g.userDistLower >= 3*g.distInterval/2 and g.userDistLower <= 5*g.distInterval/2):
        g.userDistLower = 3
    elif(g.userDistLower >= 5*g.distInterval/2 and g.userDistLower <= 7*g.distInterval/2):
        g.userDistLower = 4
    else:
        g.userDistLower = 5
    app.setLabel("Distance", "You have selected distance from center of mass(miles): " + str(userDist) + " which is in quintile #" + str(g.userDistLower))
def updateUserIncomeUpper():
    userIncome = app.getScale("Average Household Income")
    g.userIncomeUpper = userIncome - g.incomeMin
    if(g.userIncomeUpper <= g.incomeInterval/2):
        g.userIncomeUpper = 1
    elif(g.userIncomeUpper >= g.incomeInterval/2 and g.userIncomeUpper <= 3*g.incomeInterval/2):
        g.userIncomeUpper = 2
    elif(g.userIncomeUpper >= 3*g.incomeInterval/2 and g.userIncomeUpper <= 5*g.incomeInterval/2):
        g.userIncomeLower = 3
    elif(g.userIncomeUpper >= 5*g.incomeInterval/2 and g.userIncomeUpper <= 7*g.incomeInterval/2):
        g.userIncomeUpper = 4
    else:
        app.setLabel("Income","You have selected average household income lower board: " + str(userIncome) + " which is in quintile #" + str(g.userIncomeUpper))

    g.userIncomeUpper = 5
def updateUserRobberiesLower():
    userRobberies = app.getScale("Annual robberies per 100,000 people")
    g.userRobberyUpper = userRobberies - g.robberyMin
    if(g.userRobberyUpper <= g.robberyInterval/2):
        g.userRobberyUpper = 1
    elif(g.userRobberyUpper >= g.robberyInterval/2 and g.userRobberyUpper <= 3*g.robberyInterval/2):
        g.userRobberyUpper = 2
    elif(g.userRobberyUpper >= 3*g.robberyInterval/2 and g.userRobberyUpper <= 5*g.robberyInterval/2):
        g.userRobberyUpper = 3
    elif(g.userRobberyLower >= 5*g.robberyInterval/2 and g.userRobberyUpper <= 7*g.robberyInterval/2):
        g.userRobberyUpper = 4
    else:
        g.userRobberyLower = 5
    app.setLabel("Robberies","You have selected annual robberies per 100,000 people lower board: " + str(userRobberies) + " which is in quintile #" + str(g.userRobberyLower))
def updateUserDistLower():
    userDist = app.getScale("Distance from center of mass")
    g.userDistLower = userDist - g.distMin
    if(g.userDistLower <= g.distInterval/2):
        g.userDistLower = 1
    elif(g.userDistLower >= g.distInterval/2 and g.userDistLower <= 3*g.distInterval/2):
        g.userDistLower = 2
    elif(g.userDistLower >= 3*g.distInterval/2 and g.userDistLower <= 5*g.distInterval/2):
        g.userDistLower = 3
    elif(g.userDistLower >= 5*g.distInterval/2 and g.userDistLower <= 7*g.distInterval/2):
        g.userDistLower = 4
    else:
        g.userDistLower = 5
    app.setLabel("Distance", "You have selected distance from center of mass(miles): " + str(userDist) + " which is in quintile #" + str(g.userDistLower))
class GUI:
    def __init__(self):
        self.userIncomeLower =1
        self.userIncomeUpper =5
        self.userRobberyLower =1
        self.userRobberyUpper =1
        self.userDistLower =1
        self.userDistUpper=5
        self.incomeMax = 70000
        self.incomeMin = 40000
        self.robberyMax = 1000
        self.robberyMin = 200
        self.distMin = 0
        self.distMax = 30
        self.distInterval = (self.distMax-self.distMin)/4
        self.incomeInterval = (self.incomeMax-self.incomeMin)/4
        self.robberyInterval = (self.robberyMax-self.robberyMin)/4
        self.state = None
g = GUI()
def ROBBRGUI():
    ############################
    #start page
    #app.setFont(12)
    app.addLabel("l1", "Welcome to ROBBR")
    app.addButtons(["START"], hideStart)
    #end start page
    ############################
    ############################
    #State selection page -- lower bound
    app.addLabel("Lower", "Select the desired lower bound")
    app.hideLabel("Lower")
    states = ['- Select State -','Alabama','Arizona','Arkansas','California','Colorado','Connecticut','Delaware',
        'District of Columbia','Florida','Gorgia','Idaho','Illinois','Indiana','Iowa',
        'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota',
        'Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico'
        ,'New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island'
        ,'South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington',
        'West Virginia','Wisconsin','Wyoming']
    app.addLabelOptionBox("State", states)
    app.addLabel("Must select a state")
    app.hideLabel("Must select a state")
    app.hideOptionBox("State")
    #End state selection
    ###########################
    ###########################
    #Quitile selection page
    app.addLabel("Income", "You have selected average household income: " +str (g.incomeMin) + " which is in quintile #1")
    app.hideLabel("Income")

    app.addLabelScale("Average Household Income")
    app.setScaleChangeFunction("Average Household Income", updateUserIncomeLower)
    app.hideScale("Average Household Income")
    app.setScaleRange("Average Household Income", g.incomeMin, g.incomeMax)
    app.setScaleIncrement("Average Household Income", g.incomeInterval)
    app.showScaleIntervals("Average Household Income", g.incomeInterval)

    app.addLabel("Robberies","You have selected annual robberies per 100,000 people: " + str(g.robberyMin) + " which is in quintile #1")
    app.hideLabel("Robberies")

    app.addLabelScale("Annual robberies per 100,000 people")
    app.setScaleChangeFunction("Annual robberies per 100,000 people", updateUserRobberiesLower)
    app.hideScale("Annual robberies per 100,000 people")
    app.setScaleRange("Annual robberies per 100,000 people", g.robberyMin, g.robberyMax)
    app.setScaleIncrement("Annual robberies per 100,000 people", g.robberyInterval)
    app.showScaleIntervals("Annual robberies per 100,000 people", g.robberyInterval)
    #end quintile selection
    ###########################
    ###########################
    #Input verification page
    app.addLabel("Distance","You have selected distance from center of mass(miles): " + str(g.distMin) + " which is in quintile #1")
    app.hideLabel("Distance")

    app.addLabelScale("Distance from center of mass")
    app.setScaleChangeFunction("Distance from center of mass", updateUserDistLower)
    app.hideScale("Distance from center of mass")
    app.setScaleRange("Distance from center of mass", g.distMin, g.distMax)
    app.setScaleIncrement("Distance from center of mass", g.distInterval)
    app.showScaleIntervals("Distance from center of mass", g.distInterval)
    app.addButtons(["Map"], confirmInputDone)
    app.hideButton("Map")
    #app.addButtons(["EDIT"], returnInput)
    #app.hideButton("EDIT")
    #end imput verification
    ############################



    #############################
    #Map page
    app.addGoogleMap("Map")
    app.hideMap("Map")
    app.setGoogleMapSize("Map","600x600")
    app.setGoogleMapZoom("Map", 6)
    app.searchGoogleMap("Map",location="1742 Morse road, Forest Hill, MD")
    app.setGoogleMapMarker("Map", location='1742 Morse road, Forerst Hill, MD', size=None, colour='blue', label='J', replace=False)
    x = app.getGoogleMapLocation("Map")
    app.setGoogleMapMarker("Map",x)
    #end map page
    ##############################
    app.addButtons(["NEXT"], stateSelected)
    app.hideButton("NEXT")
    app.addButtons(["BACK"], returnState)
    app.hideButton("BACK")
    app.addButtons(["DONE"], inputDone)
    app.hideButton("DONE")
    app.go()
app=gui("ROBBR")
ROBBRGUI()
def sendData():
    if(g.state==None):
        return False
    else:
        return g.state
