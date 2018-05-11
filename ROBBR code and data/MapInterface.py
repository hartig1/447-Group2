from appJar import gui
import time
import csv
app = gui("ROBBR")
def MapInterface(q):
    count = 0
    app.addGoogleMap("Map")
    app.setGoogleMapZoom("Map",6)
    file = open("houses.csv","r")
    reader = csv.reader(file,delimiter=",")
    houses = ''
    if q.state == "Maryland":
        q.getCOM()
        app.setGoogleMapZoom("Map",9)
        app.searchGoogleMap("Map",location = str(q.COMLat)+ "," + str(q.COMLong))
        x = app.getGoogleMapLocation("Map")
        if(x != None):
            app.setGoogleMapMarker("Map", location=x, size=None, colour='blue', label='J', replace=False)
    for row in reader:
        #print(row[1])
        if count < 5:
            time.sleep(.5)
            # markerLabel = 'A'
            # if count == 0:
            #     markerLabel = 'A'
            # elif count == 1:
            #     markerLabel = 'B'
            # elif count == 2:
            #     markerLabel = 'C'
            # elif count == 3:
            #     label = 'D'
            # elif markerLabel == 4:
            #     label = 'E'
            # elif count == 5:
            #     markerLabel = 'F'
            # elif count == 6:
            #     markerLabel = 'G'
            #houses += markerLabel + ": " + row[0] + " " + row[1] + "\n"
            houses += row[0] + " " + row[1] + "\n"
            app.searchGoogleMap("Map", location=row[1])
            x = app.getGoogleMapLocation("Map")
            if x != None:
                #app.setGoogleMapMarker("Map",location=x, size=None, colour="red", label=markerLabel, replace=False)
                app.setGoogleMapMarker("Map",location=x, replace=False)
            else:
                print("House not found")
        else:
            break
        count+=1
    #app.startSubWindow("list", modal=True)
    app.addMessage("Houses",houses)
    #app.stopSubWindow()
    #app.showSubWIndow("list")
    app.go()
if __name__ == "__main__":
    MapInterface()
