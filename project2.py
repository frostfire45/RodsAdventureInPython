# Open the CSV file
with open("section1-students.csv", "r") as file:
    # Read the lines of the file
    lines = file.readlines()

# Initialize an empty grade book
grade_book = []

# Iterate through each line in the file
for line in lines:
    # Remove newline characters and split the line into tokens
    tokens = line.strip().split(',')
    
    # Convert exam scores to integer values
    for i in range(3, len(tokens)):  # Assuming exam scores start from the fourth token
        tokens[i] = int(tokens[i])
    
    # Append the list of tokens to the grade book
    grade_book.append(tokens)

# Printing the grade book for verification
#for student in grade_book:
#   print(student) #Testing token output

###################
#Sub_Menu Functions
###################
# Function to calculate average
#def list_exams(grade.book):

def list_exams(grade_book):
    for student in grade_book:
        print(student)

def cal_ave(grade_book):
    exam_scores = []
    for student in grade_book:
        exam_scores.extend(student[3:])  # Assuming exam scores start from index 3
    average_score = sum(exam_scores) / len(exam_scores)
    print(f"Average score: {average_score:.2f}")

# Function to calculate lowest score
def cal_low(grade_book):
    lowest_score = min([min(student[3:]) for student in grade_book])  # Assuming exam scores start from index 3
    print(f"Lowest score: {lowest_score}")

# Function to calculate highest score
def cal_high(grade_book):
    highest_score = max([max(student[3:]) for student in grade_book])  # Assuming exam scores start from index 3
    print(f"Highest score: {highest_score}")


################
#Main-Menu
################
def main_menu():
    print()
    print("Main Menu:")
    print("1:Exam Scores  2:Graphs  3:Class Graph  4:Exit Program")
    print()

def submenu():
    print()
    print("1:List All  2:Average  3:Low Score  4:High Score 5 :Exit")
    print()

def main():
    while True:
        main_menu()
        choice = input("Select and Option: ")
        
        if choice == "1":
            while True:
                submenu()
                sub_choice = input("Enter your choice: ")
                
                if sub_choice.lower() == "1":
                    print("You chose List All")
                    list_exams(grade_book)
                elif sub_choice.lower() == "2":
                    cal_ave(grade_book)
                elif sub_choice.lower() == "3":
                    cal_low(grade_book)
                elif sub_choice.lower() == "4":
                    cal_high(grade_book)
                elif sub_choice.lower() == "5":
                    break
                else:
                    print("Invalid choice. Please try again.")
        elif choice == "2":
            print("You chose Option 2")
        elif choice == "3":
            print("You chose Option 3")
        elif choice == "4":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()