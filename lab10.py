
#Task1
def txtToCSV(filename='', csvName=''):
    txtFile = open(filename, 'r')
    csvFile = open(csvName, 'w')
    csvFile.write('Names, Count\n')
    for row in txtFile:
        csvFile.write(row)


# txtToCSV('boysnames.txt','boysnames2.csv')

#Task2
def userInput():
    name = input("Enter CSV file name: ")
    readFile = open(name, 'r')
    for row in readFile:
        strRow = str(row)
        rep = [i.strip() for i in strRow.split(',')]
        # rep = strRow.replace(",", " ").replace("\n","")
        print(rep)


# userInput()
#Task3
def generateDictionary(filename=''):
    readFile = open(filename, 'r')
    newDict = {}
    for row in readFile:
        newRow = str(row)
        k = [i.strip() for i in newRow.split(',')]

        key = k[1]
        value = list(str(k[0]))
    # newDict[key] = value
        liNum = value[2:]
        binLi = [bin(int(el, 16)) for el in liNum]
        binLi2 = [binLi[n][2:] for n in range(len(binLi))]
        binLi3 = []
        binLi4 = []
        for x in binLi2:
            if len(x) == 1 or len(x) == 2 or len(x)==3:
                fillBin = x.zfill(4)
                binLi3.append(fillBin)
            else:
                binLi3.append(x)
        conCatLi = [i+j for i,j in zip(binLi3[::2],binLi3[1::2])]
        for x in conCatLi:
            doubleList = list(x)
            binLi4.append(doubleList)
            newDict[key] = binLi4

    # print(newDict)
    return newDict

# generateDictionary('font3.txt')

def clearScreen(lcd):
    lcd.clear()
    lcd.show()

def displayChar():
    # myFile = open('font3.txt', 'r')
    myDictionary = generateDictionary('font3.txt')
    inp = input('enter a character: ')
    print(myDictionary[inp])
    obj = myDictionary[inp]
    x=20
    y=40
    try:
        lcd.clear()
        xc = x
        for y1 in obj:
            for x2 in y1:
                if x2 == 1:
                    pixel = 1
                else:
                    pixel = 0
                lcd.set_pixel(xc,y,pixel)
                xc = xc + 1
            y=y+1
            lcd.set_pixel(xc,y,pixel)
            xc = x
        lcd.show()
    except:
        print("couldnt find character")
    print("press any key to quit")
    getchar()
    clearScreen(lcd)

displayChar()
