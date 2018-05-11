import os
os.chdir("C:/python27/Lib/site-packages")
from appJar import gui
def launch(win):
    app.showSubWindow(win)

app=gui("ROBBR Start Screen")
app.setFont(12)
app.addLabel("l1", "Welcome to ROBBR")
# these go in the main window
app.addButtons(["START"], launch)
#app.hide()
app.startSubWindow("START","ROBBR State Selection")
states = ['- Select State -','Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware',
    'District of Columbia','Florida','Gorgia','Hawaii','Idaho','Illinois','Indiana','Iowa',
    'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota',
    'Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico'
    ,'New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island'
    ,'South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington',
    'West Virginia','Wisconsin','Wyoming']
app.addLabelOptionBox("State", states)
selected = app.getOptionBox("State")
app.addButtons(["NEXT"], launch)
app.addNamedButton("BACK", "State", app.hideSubWindow)
app.startSubWindow("NEXT","ROBBR Parameter Entry")
app.setStretch("both")
app.setSticky("w")
app.addLabel("l2", "ROBBR Parameter Entry")
app.addLabelScale("Average Household Income",row=None,column=1,rowspan=1,colspan=10)
app.setScaleWidth("Average Household Income", 10)
app.setScaleHeight("Average Household Income", 800)
app.setScaleRange("Average Household Income", 30000, 70000)
app.setScaleIncrement("Average Household Income", 10000)
app.showScaleValue("Average Household Income")
app.showScaleIntervals("Average Household Income", 10000)
app.stopSubWindow()

app.stopSubWindow()
# this is a pop-up
#selected = app.getOptionBox("State")
#while selected == None:
#    selected = app.getOptionBox("State")
app.go()
app.stop()
