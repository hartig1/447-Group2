#from ROBBRInterface import *
from StateGUI import *
from Query import *
from stateNameConverter import *
def main():
    file = open("combined.csv", "w")
    file.write("")
    file.close()
    file = open("allState.csv", "w")
    file.write("")
    file.close()
    file = open("incomeSorted.csv", "w")
    file.write("")
    file.close()
    file = open("crimeSorted.csv", "w")
    file.write("")
    file.close()
    file = open("houses.csv", "w")
    file.write("")
    file.close()
    state = stateGUI()
    print("Please wait gathering zips")
    q = Query(state)
    #print(q.min_income)
    stateNameConverter()
    from QuintileGUI import *
    quintiles = QuintileGUI(q.min_income,q.max_income,q.min_crime,q.max_crime,25,100)
    print(quintiles)
    #return income then crime then dist
    from WeightGUI import *
    q.setSelectedCrime(quintiles[2],quintiles[3])
    q.setSelectedIncome(quintiles[0],quintiles[1])
    q.setSelectedDist(quintiles[4], quintiles[5])
    q.popZipDict()
    q.filter()
    q.findHouses()
    #pause()
    weightI, weightC, weightD = WeightGUI()
    from MapInterface import *
    MapInterface(q)
    #print(state)
if __name__ == '__main__':
    main()
