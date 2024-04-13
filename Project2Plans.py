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

# This function takes in a line and seperates it 
# into the two different datasources which is stored in memory
def feedToMemory(line):
    #CSV comma, space
    # Take this line and split it into an array
    index = 0
    lineArray = line.split(",")
    arrayCount = testValueEnd + 1
    studentId = ""
    #currently index is starting at 0
    while(index < testValueStart):
        if(index == 0):
            studentId = lineArray[index] 
        else if (index == 1):
            listOfStudents[studentId][0] = lineArray[index]        
        else if (index == 2):
            listOfStudents[studentId][1] = lineArray[index]
        else
            listOfStudent[studentId][2] = listOfStudent[studentId][0] + "_" + listOfStudents[studentId][1] 
        index = index + 1

    # index will be at 3 when it breaks from the first one
    # so calculation  - index(3)
    while(index < testValueEnd + 1):
        if(index > indenityend AND index < testValueEnd + 5):
            listOfTests[studentId][]
        index = index + 1

studentRecordCsvFile = open("section1-students.csv", "r")

while True:
    # Read the lines of the file
    text = studentRecordCsvFile.readline()
    if not text:
        break
    feedToMemory(text)
studentRecordCsvFile.close()
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
#p1 = Person( "abc123", "Linda", "Smith" )

#print(p1.firstName)


# Read information from a csv file 


# Process strings from the input
# Create a multi-dimensional list of lists (an array)
# Print information to the console
# Print plots to the console
# Create a text file as output 
# Use variables and sequence types
# Use If Statements and loops
# Use functions
## 



