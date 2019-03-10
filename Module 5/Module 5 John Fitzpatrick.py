#-------------------------------------------------#
# Title: Working with Dictionaries
# Dev:   RRoot
# Date:  July 16, 2012
# ChangeLog: (Who, When, What)
#   RRoot, 11/02/2016, Created starting template
#   John Fitzpatrick, ???, Added code to complete assignment 5
#https://www.tutorialspoint.com/python/python_dictionary.htm
#-------------------------------------------------#

#-- Data --#
# declare variables and constants
# objFile = An object that represents a file
# strData = A row of text data from the file
# dicRow = A row of data separated into elements of a dictionary {Task,Priority}
# lstTable = A dictionary that acts as a 'table' of rows
# strMenu = A menu of user options
# strChoice = Capture the user option selection

#-- Input/Output --#
# User can see a Menu (Step 2)
# User can see data (Step 3)
# User can insert or delete data(Step 4 and 5)
# User can save to file (Step 6)

#-- Processing --#
# Step 1
# When the program starts, load the any data you have
# in a text file called ToDo.txt into a python Dictionary.

# Step 2
# Display a menu of choices to the user

# Step 3
# Display all todo items to user

# Step 4
# Add a new item to the list/Table

# Step 5
# Remove a new item to the list/Table

# Step 6
# Save tasks to the ToDo.txt file

# Step 7
# Exit program
#-------------------------------
#The command opens the text file and reads it to memory
with open("C:\Python\Todo.txt", "r+") as f:
   
    def read():
        with open("C:\Python\Todo.txt","r") as text:
            
         lstTable = [str(Task), str(Priority)]
         return dict(line.strip().split() for line in text)
#All rows of the file are in the python dictionary
row0 = ['0',"Task", "Priority"]
row1 = ['1',"Clean house", "low"]
row2 = ['2',"Pay Bills", "high"]
#The tables are displayed with the print function
table = [row1, row2]
print(table)


# Step 1 - Load data from a file
    # When the program starts, load each "row" of data 
    # in "ToDo.txt" into a python Dictionary.
    # Add the each dictionary "row" to a python list "table"
 

# Step 2 - Display a menu of choices to the user
while(True):
    print ("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 4] - "))
    print()#adding a new line

    # Step 3 -Show the current items in the table
    if (strChoice.strip() == '1'):
        print(table) == '1'
        continue
     #The data in the table is displayed   
    # Step 4 - Add a new item to the list/Table
    #The input is displayed for the user to enter data
    elif(strChoice.strip() == '2'):
        z = int(input("Enter new TaskID: "))
        x = input("Enter new Task: ")
        y = input("Enter new Priority: ")
        newRow = (z),(x),(y)
        strnewRow = [z, x, y]
        table.append(newRow)
        print(newRow)
        continue
    # Step 5 - Remove a new item to the list/Table
    #I couldn't get the delete function to work.
    elif(strChoice == '3'):
        print(table)
        table = input("Enter the data you want to delete: ")
        table.remove(table)
        print(table)
        continue
     # Step 6 - Save tasks to the ToDo.txt file
     #The loop opens the file and saves the data or not
    elif(strChoice == '4'):
     todo = y
     if(str(y.lower() == 'y')):
        objF =open("C:\Python\Todo.txt", 'w')
        objF.write(str(table))
        objF.close()
        print("Data\n\r",table,"\n\ris saved")
     else:
        print("Data is not saved")
        continue

    elif(strChoice == '5'):
         break #and Exit the program

