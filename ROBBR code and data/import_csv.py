from appJar import gui

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
        app.hideButton("NEXT")
        app.showLabel("Income")
        app.showLabel("Robberies")
        app.showButton("BACK")
        app.showButton("DONE")
        app.hideLabel("Must select a state")
def returnState():
    app.showOptionBox("State")
    app.hideScale("Average Household Income")
    app.hideScale("Annual robberies per 100,000 people")
    app.showButton("NEXT")
    app.hideButton("BACK")
    app.hideButton("DONE")
    app.hideLabel("Income")
    app.hideLabel("Robberies")
def inputDone():
    app.hideScale("Average Household Income")
    app.hideScale("Annual robberies per 100,000 people")
    app.hideButton("BACK")
    app.showButton("EDIT")
def returnInput():
    app.showScale("Average Household Income")
    app.showScale("Annual robberies per 100,000 people")
    app.showButton("BACK")
    app.hideButton("EDIT")
    app.showLabel("Income")
    app.showLabel("Robberies")
def updateUserIncome():
    userIncome = app.getScale("Average Household Income")
    app.setLabel("Income","You have selected average household income: " + str(userIncome) + " which is in quintile #" + str(int((userIncome-incomeMin)/incomeInterval)+1))

def updateUserRobberies():
    userRobberies = app.getScale("Annual robberies per 100,000 people")
    app.setLabel("Robberies","You have selected annual robberies per 100,000 people: " + str(userRobberies) + " which is in quintile #" + str(int((userRobberies-robberyMin)/robberyInterval)+1))

incomeMax = 70000
incomeMin = 40000
robberyMax = 1000
robberyMin = 200
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
