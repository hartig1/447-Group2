from appJar import gui

def next():
    if(app.getOptionBox("State") == None):
        app.showLabel("Must select a state")
    else:
        state = app.getOptionBox("State")
        file = open("metaData.txt","w")
        file.write(state)
        file.close()
        app.stop()
def changeState():
    state = app.getOptionBox("State")
app=gui("ROBBR")
def stateGUI():
    states = ['- Select State -','Alabama','Arizona','Arkansas','California','Colorado','Connecticut','Delaware',
        'District of Columbia','Florida','Georgia','Idaho','Illinois','Indiana','Iowa',
        'Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota',
        'Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico'
        ,'New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island'
        ,'South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington',
        'West Virginia','Wisconsin','Wyoming']
    #app=gui("ROBBR")
    app.addLabelOptionBox("State", states)
    app.setOptionBoxChangeFunction("State", changeState)
    app.addLabel("Must select a state")
    app.hideLabel("Must select a state")
    state = app.addButtons(["NEXT"],next)
#app.hideOptionBox("State")
    app.go()
    file = open("metaData.txt", "r")
    state = file.read()
    return state
if __name__ == "__main__":
    stateGUI()
