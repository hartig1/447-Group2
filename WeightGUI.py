from appJar import *
app=gui("ROBBR")
def checkDone():
    i = app.getEntry("Income")
    if(i == None):
        i = 0
    c = app.getEntry("Crime")
    if(c == None):
        c = 0
    d = app.getEntry("Distance")
    if(d == None):
        d = 0
    if(i + c + d != 1):
        app.showLabel("Weights must add up to 1")
    else:
        i = app.getEntry("Income")
        if(i == None):
            i = 0
        c = app.getEntry("Crime")
        if(c == None):
            c = 0
        d = app.getEntry("Distance")
        if(d == None):
            d = 0
        file = open("weights.txt", "w")
        file.write(str(i) + "," + str(c) + "," + str(d))
        file.close()
        app.stop()
def WeightGUI():
    app.addLabel("Enter the weight for income here")
    app.addNumericEntry("Income")
    app.addLabel("Enter the weight for crime here")
    app.addNumericEntry("Crime")
    app.addLabel("Enter the weight for distance here")
    app.addNumericEntry("Distance")
    app.addLabel("Weights must add up to 1")
    app.hideLabel("Weights must add up to 1")
    app.addButtons(["DONE"], checkDone)
    app.go()
    file = open("weights.txt","r")
    weights = file.read().split(",")
    return weights
if __name__ == "__main__":
    WeightGUI()
