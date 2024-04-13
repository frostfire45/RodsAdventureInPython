# Reference places
## https://www.w3schools.com/python/

#Constants
identityNumberCount = 3
identityStart = 0
indenityend = 2
testValueNumberCount = 3
testValueStart = 3
testValueEnd = 5

# Initiated Cached Datasources
listOfStudents = { }
listOfTests = { }

###############################################################
#  feedtToMemory
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

studentRecordCsvFile = open("section1-students.csv", "r")

while True:
    # Read the lines of the file
    text = studentRecordCsvFile.readline()
    filteredText = text.replace("\n", "")
    
    if not text:
        break
    feedToMemory(filteredText)
studentRecordCsvFile.close()

print(listOfStudents)

#ListOfStudents(ID,Name,test[List])
#listOfStudents = { }
#listOfStudents["abc123"] = ["Linda","Smith","linda_smith"]
#listOfStudents["abc124"] = ["Linda","VanTucket","linda_VanTucket"]

#ListOfTest(ID,test[])
#listOfTests = { }
#listOfTests["abc123"] = [92,93,20]
#listOfTests["abc124"] = [20,35,25]

#print(listOfTests["abc123"][1])
#print(listOfStudents["abc123"][2])
#print(listOfTests["abc124"][1])
#print(listOfStudents["abc124"][2])

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



