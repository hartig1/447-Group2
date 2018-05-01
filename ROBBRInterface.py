from appJar import gui
import math
def hideStart(win):
    app.hideButton("START")
    app.showOptionBox("State")
    app.showButton("NEXT")
def stateSelected():
    if(app.getOptionBox("State") == None):
        app.showLabel("Must select a state")
    else:
        app.hideOptionBox("State")
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
def returnState():
    app.showOptionBox("State")
    app.hideScale("Average Household Income")
    app.hideScale("Annual robberies per 100,000 people")
    app.hideScale("Distance from center of mass")
    app.showButton("NEXT")
    app.hideButton("BACK")
    app.hideButton("DONE")
    app.hideLabel("Income")
    app.hideLabel("Robberies")
    app.hideLabel("Distance")
def inputDone():
    app.hideScale("Average Household Income")
    app.hideScale("Annual robberies per 100,000 people")
    app.hideScale("Distance from center of mass")
    app.hideButton("BACK")
    app.showButton("EDIT")
def returnInput():
    app.showScale("Average Household Income")
    app.showScale("Annual robberies per 100,000 people")
    app.showScale("Distance from center of mass")
    app.showButton("BACK")
    app.hideButton("EDIT")
    app.showLabel("Income")
    app.showLabel("Robberies")
    app.showLabel("Distance")
def updateUserIncome():
    userIncome = app.getScale("Average Household Income")
    quint = (userIncome-incomeMin)/(incomeInterval/2)
    #print(quint)
    if(quint == 0):
        quint = 1
    elif(quint == 1):
        quint = 2
    elif(quint == 2):
        quint = 2
    elif(quint == 3):
        quint = 3
    elif(quint == 4):
        quint = 3
    elif(quint == 5):
        quint = 4
    elif(quint == 6):
        quint = 4
    elif(quint == 7):
        quint = 5
    elif(quint == 8):
        quint = 5
    app.setLabel("Income","You have selected average household income: " + str(userIncome) + " which is in quintile #" + str(quint))

def updateUserRobberies():
    userRobberies = app.getScale("Annual robberies per 100,000 people")
    quint = (userRobberies-robberyMin)/(robberyInterval/2)
    #print(quint)
    if(quint == 0):
        quint = 1
    elif(quint == 1):
        quint = 2
    elif(quint == 2):
        quint = 2
    elif(quint == 3):
        quint = 3
    elif(quint == 4):
        quint = 3
    elif(quint == 5):
        quint = 4
    elif(quint == 6):
        quint = 4
    elif(quint == 7):
        quint = 5
    elif(quint == 8):
        quint = 5
    app.setLabel("Robberies","You have selected annual robberies per 100,000 people: " + str(userRobberies) + " which is in quintile #" + str(quint))
def updateUserDist():
    userDist = app.getScale("Distance from center of mass")
    quint = (userDist-distMin)/(distInterval/2)
    #print(quint)
    if(quint == 0):
        quint = 1
    elif(quint == 1):
        quint = 2
    elif(quint == 2):
        quint = 2
    elif(quint == 3):
        quint = 3
    elif(quint == 4):
        quint = 3
    elif(quint == 5):
        quint = 4
    elif(quint == 6):
        quint = 4
    elif(quint == 7):
        quint = 5
    elif(quint == 8):
        quint = 5
    app.setLabel("Distance", "You have selected distance from center of mass(miles): " + str(userDist) + " which is in quintile #" + str(quint))
incomeMax = 70000
incomeMin = 40000
robberyMax = 1000
robberyMin = 200
distMin = 0
distMax = 30
distInterval = (distMax-distMin)/4
incomeInterval = (incomeMax-incomeMin)/4
robberyInterval = (robberyMax-robberyMin)/4

app=gui("ROBBR")

app.setFont(12)
app.addLabel("l1", "Welcome to ROBBR")
app.addButtons(["START"], hideStart)

states = ['- Select State -','Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware',
    'District of Columbia','Florida','Gorgia','Hawaii','Idaho','Illinois','Indiana','Iowa',
    'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota',
    'Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico'
    ,'New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island'
    ,'South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington',
    'West Virginia','Wisconsin','Wyoming']
app.addLabelOptionBox("State", states)

app.addLabel("Income", "You have selected average household income: " +str (incomeMin) + " which is in quintile #1")
app.hideLabel("Income")


app.addLabelScale("Average Household Income")
app.setScaleChangeFunction("Average Household Income", updateUserIncome)
app.hideScale("Average Household Income")
app.setScaleRange("Average Household Income", incomeMin, incomeMax)
app.setScaleIncrement("Average Household Income", incomeInterval)
#app.showScaleValue("Average Household Income")
app.showScaleIntervals("Average Household Income", incomeInterval)

app.addLabel("Robberies","You have selected annual robberies per 100,000 people: " + str(robberyMin) + " which is in quintile #1")
app.hideLabel("Robberies")

app.addLabelScale("Annual robberies per 100,000 people")
app.setScaleChangeFunction("Annual robberies per 100,000 people", updateUserRobberies)
app.hideScale("Annual robberies per 100,000 people")
app.setScaleRange("Annual robberies per 100,000 people", robberyMin, robberyMax)
app.setScaleIncrement("Annual robberies per 100,000 people", robberyInterval)
#app.showScaleValue("Annual robberies per 100,000 people")
app.showScaleIntervals("Annual robberies per 100,000 people", robberyInterval)

app.addLabel("Distance","You have selected distance from center of mass(miles): " + str(distMin) + " which is in quintile #1")
app.hideLabel("Distance")

app.addLabelScale("Distance from center of mass")
app.setScaleChangeFunction("Distance from center of mass", updateUserDist)
app.hideScale("Distance from center of mass")
app.setScaleRange("Distance from center of mass", distMin, distMax)
app.setScaleIncrement("Distance from center of mass", distInterval)
#app.showScaleValue("Annual robberies per 100,000 people")
app.showScaleIntervals("Distance from center of mass", distInterval)

app.addLabel("Must select a state")
app.hideLabel("Must select a state")
app.hideOptionBox("State")
app.addButtons(["NEXT"], stateSelected)
app.hideButton("NEXT")
app.addButtons(["BACK"], returnState)
app.hideButton("BACK")
app.addButtons(["EDIT"], returnInput)
app.hideButton("EDIT")
app.addButtons(["DONE"], inputDone)
app.hideButton("DONE")
app.go()
