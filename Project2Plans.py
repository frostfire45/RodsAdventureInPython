# Reference places
## https://www.w3schools.com/python/

# Read information from a csv file and put into memory
# Process strings from the input
# Create a multi-dimensional list of lists (an array)
# Print information to the console
# Print plots to the console
# Create a text file as output 
# Use variables and sequence types
# Use If Statements and loops
# Use functions

## 
#Constants
identityNumberCount = 3
identityStart = 0
indenityend = 2
testValueNumberCount = 3
testValueStart = 3
testValueEnd = 5
pathToFile = "section1-students.csv"
tier1MenuInput = ["Exam Scores", "Graphs", "Class Graph", "OUtput File", "Exit Program"]
tier2MenuInput = ["List All","Average","Low Score","High Score","Back"]
# Initiated Cached Datasources
listOfStudents = { }
listOfTests = { }


## Function Declaration
def loadFile(filePath):
    studentRecordCsvFile = open(filePath,"r")
    return studentRecordCsvFile
def closeFile(filePointer):
    filePointer.close()
def initiateInMemoryValues():
    fileInMemory = loadFile(pathToFile)
    while True:
        # Read the lines of the file
        text = fileInMemory.readline()
        filteredText = text.replace("\n", "")
        
        if not text:
            break
        feedToMemory(filteredText)
    closeFile(fileInMemory)

###############################################################
"""  feedtToMemory
#==============================================================
#  Input: a single string
#  Output: None
#  Functionality:
#   1) Create a starting index to maintain array integrity
#   2) Split inputed String into an array seperated by a comma
#   3) Create an emtpy Student ID Key and store it for 
#      studentInfo and TestInfo Datasources
#   4) Create a temporary Repository For each Datasource
#   5) Create a loop to feed in the first 3 values
#   5a) First index will be the key / studentId to be used in 
#       creating multiple dictionary keys 
################################################################  
# This function takes in a line and seperates it 
# into the two different datasources which is stored in memory
## END ## """
def feedToMemory(line):
    #Functionality 1
    index = 0
    #Functionality 2
    lineArray = line.split(",")
    #Functionality 3
    key = ""
    # Functionality 4
    tempStudentList = []
    tempStudentTestList = []

    #Functionality 5
    ### currently index is starting at 0
    while index < testValueStart + 1:
        # Functionality 5a
        if index == 0:
            key = lineArray[index]
            index = index + 1 
        elif index == 1:
            tempStudentList.append(lineArray[index])
            index = index + 1
            #listOfStudents[studentId][0] = lineArray[index]        
        elif index == 2:
            tempStudentList.append(lineArray[index])
            index = index + 1
            #listOfStudents[studentId][1] = lineArray[index]
        elif index == 3:
            tempStudentList.append(tempStudentList[0] + "_" + tempStudentList[1])          
            listOfStudents[key] = tempStudentList 
            break

    # index will be at 3 when it breaks from the first one
    # so calculation  testValueNumberCount (3) - index(3)
   
    while index < testValueEnd + 1:
        if index > indenityend and index < testValueEnd + 1:
            tempStudentTestList.append(lineArray[index])
        if index == testValueEnd:
            listOfTests[key] = tempStudentTestList
        index = index + 1

## Displays for Menus and Menu tasks
def topTierMenu():
    menuLine = ""
    isGoing = "YES"
    while isGoing == "YES":        
        for x in range(len(tier1MenuInput)):
            menuLine = menuLine + "{0}) {1}\t\t".format(x+1,tier1MenuInput[x])  

        dispFormatLines(len(menuLine),"=")
        print(menuLine)    
        topMenuInput = input("input: ")
        if topMenuInput == "1":
            menuLine = ""
            tier1Entry1()
        elif (topMenuInput == "2"):
            menuLine = ""
            tier1Entry2()
        elif topMenuInput == "3":
            menuLine = ""
            tier1Entry3()
        elif topMenuInput == "q" or topMenuInput == "Q":
            break
        else:
            tier1Error()
            menuLine = ""
def dispFormatLines(length,charType):
    line = ""
    for x in range(length): 
        line = line + charType
    print(line)
## Tier 1
def tier1Entry1():
    tier2TestOption()
def tier1Entry2():
    print("Hit 2")
def tier1Entry3():
    print("Hit 3"
          )
def tier1Error():
    print("You entered the wrong value")
## Tier 2 menu stuff
def tier2TestOption():
    menuLine = ""
    isGoing = "YES"
    while isGoing == "YES":        
        for x in range(len(tier1MenuInput)):
            menuLine = menuLine + "{0}) {1}\t".format(x+1,tier2MenuInput[x])  

        dispFormatLines(len(menuLine),"=")
        print(menuLine)    
        topMenuInput = input("input: ")
        if topMenuInput == "1":
            menuLine = ""
            selectAll()
        elif (topMenuInput == "2"):
            menuLine = ""
            average()
        elif topMenuInput == "3":
            menuLine = ""
            lowScore()
        elif topMenuInput == "4":
            menuLine = ""
            highScore()
        elif topMenuInput == "q" or topMenuInput == "Q":
            break
        else:
            tier1Error()
            menuLine = ""
def selectAll():
    for x in listOfStudents.keys():
        print(listOfStudents[x] + listOfTests[x])
def average():
    for x in listOfTests.keys():
        key  = str(x)
        studenVal = listOfStudents[key]
        tesetVal = listOfTests[key]
        sum = (int(tesetVal[0]) + int(tesetVal[1]) + int(tesetVal[2])) / 3
        print( str(studenVal[2]) + "  " + "Average: " + str(sum)) 
def lowScore():
    for x in listOfTests.keys():
        key  = str(x)
        studenVal = listOfStudents[key]
        testVal = listOfTests[key]
        top = 100
        for y in range(len(testVal)):
           val = int(testVal[y])
           if int(testVal[y]) < int(top):
               top = testVal[y]  
        print( str(studenVal[2]) + "  " + "Low Score: " + str(top))
def highScore():
    for x in listOfTests.keys():
        key  = str(x)
        studenVal = listOfStudents[key]
        testVal = listOfTests[key]
        top = 0
        for y in range(len(testVal)):
           val = int(testVal[y])
           if int(testVal[y]) > int(top):
               top = testVal[y]  
        print( str(studenVal[2]) + "  " + "High Score: " + str(top))              
## Main Entry
initiateInMemoryValues()
topTierMenu()