def displayMenu():  # -------------------------- Done

    print("================================================================")
    print("|| 1. Display Grade Info for all students                     ||")
    print("|| 2. Display Grade Info for a particular student             ||")
    print("|| 3. Display tests average for all students                  ||")
    print("|| 4. Modify a particular test grade for a particular student ||")
    print("|| 5. Add test grades for a particular test for all students  ||")
    print("|| 6. Add a new Student                                       ||")
    print("|| 7. Delete a student                                        ||")
    print("|| 8. Save and Exit                                           ||")
    print("================================================================")
    
def extractFile(inputData): # -------------------------- Done
    grades = {}     # This is a dictionary to store all students' grades.
      # Here, we want to read a file input. We put it inside a variable. 

    # First of all, we want to check and filter all useless things, such as #. We want to put a new variable called string and putting all useful things we want.
    for line in inputData: # It will check every single line and check first of all '#'. 
        string = ""
        for character in line:
            if character != "#": # We want to be more general, so we use methods isdigit and isspace and isalpha.
                string += character
                    
        fields = string.split()   # We made a list called fields.
        if fields[0].isdigit():   # To check if first index is digit or not.
            studentsID = fields[0] # if it True, that means it would be a studentID. 
            studentsGrades = []  # Also, we define a variable list called studentsGrades.
            studentsNameList = []
            for indexCheck in range(1,len(fields)):  # if it is True, we want to check only numbers of index from 3 into -1, because number 0 and indicates to studentID and numbers 1 and 2 indicate to studentName.
                if not fields[indexCheck].isalpha():
                    if str(int(float(fields[indexCheck]))).isdigit():
                        studentsGrades.append(round(float(fields[indexCheck]),1))
                else:
                    studentsNameList.append(fields[indexCheck])
                        
            studentsName = ""
            for i in range(len(studentsNameList)):
                studentsName += studentsNameList[i] + " "
            studentsName = studentsName.strip()
            grades[studentsID] = [studentsName] # Putting a student's name inside a dictionary.  
            for test in studentsGrades:  
                grades[studentsID].append(test) # After that, every thing inside studentsGrades list will be inside a dictionary in the same key.
        else:
            pass                   
    
    # All information from the file, is inside dictionary now.
    # After that, we want to close a file.
    inputData.close()
    
    # Finally, return a variable grades. And this function is for collecting data and put it inside dictionay.
    return grades
        
def displayGrades(grades): # number 1: Display Grade Info for all students.
    # ----------------------------------------------------------------------------
    
    if len(grades) == 0: # We want to check if nothing inside dictionary or not.
        print("There is no information here.")
        
    else:
        
        quizes = 0 # Variable for counting quizes.
        for studentID,data in grades.items():
            if len(data[1:]) > quizes: # We want to find a largest number of tests
                quizes = len(data[1:])
    
        counter = quizes 
        inpString = "StudentID    StudentName \t    " # ========> Here, to count all grades 
        for n in range(1,counter+1): # Here to check and print from test 1 into last number of test.
            inpString += " test%d    "%n
            
        print(inpString)
            
        for studentID, data in grades.items(): # We use this method to be able to control keys and values.
            studentName = data[0] 
            studentGrades = data[1:]
            allGrades = [] # ========> list for all student's grades
            allGradesStr = "" # Here we want to add all test grades from list into string.
            for tests in studentGrades:
                allGrades.append(tests)     # so we can complete using list and adding to string.
                
            for tests in allGrades: # All tests 
                allGradesStr += str(tests) + "      "     # Here we can be able to put the maximum number of quizes, and it will display on the end like "test4" if the number of quizes equal 4 and so on.
       
            print('  %-10s  %-20s   %-10s ' % (studentID, studentName, allGradesStr))  # Print each student line by line using for loop.
            
def dispalyGradesInParticuler(grades,studentID): # number 2: Display Grade Info for a particular student.      # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # ----------------------------------------------------------------------------

    print(studentID , end="   ") # Here, to print a student ID.
    data = grades[studentID]    # After a little spaces, it will print all quizes for the student.
    for i in data:
        print(i , end= "   ")
    print()
        
def displayTestAverage(grades): # number 3: Display quiz averages for all students. 
    # ----------------------------------------------------------------------------

    if len(grades) == 0:   # We want to check if nothing inside dictionary or not.
        print("There is no information here.")
                
    else: 
        print('StudentID\tStudent Name\t\tAverage') # Here to seperate between columns.
        for studentID, data in grades.items(): # Using for loop to print each student line by line.
            studentName = data[0] # Student name 
            studentGrades = data[1:]
            total = 0
            allGrades = ""
            for tests in studentGrades:
                total += tests
            
            average = total/len(studentGrades)   
            print('  %s          %-20s    %.2f' % (studentID, studentName, average)) 
    
def modifyParticulerTest(grades,studentID,quizNumber,newQuizGrade): # number 4: Modify a particular test grade for a particular student.
    # ----------------------------------------------------------------------------
    # It prompts for and reads a studentID, the test number, and the new test grade. 
    # Read carefuly:
    '''
    If the test number is invalid (outside range or not a number), or the new test grade is invalid (negative or greater than 100 or not a number)  
    an appropriate error message is displayed; otherwise it searches for this studentID. 
    If the studentID is not found an appropriate error message is displayed, otherwise; the student grade is updated in the list.
    '''
    if len(grades) == 0: # We want to check if nothing inside dictionary or not.
        print("There is no information here.")
        
    else: # Check if student exist.
        if studentID in grades:      
            data = grades[studentID]
            studentName = data[0] 
            beforeGrading = ""
            afterGrading = ""
            for i in data[1:]:
                beforeGrading += str(i) + '\t' # Using to seperate between grades.
                
            if quizNumber in range(1, len(data)+1):
                if 0 <= newQuizGrade <= 100:
                    data[quizNumber] = newQuizGrade
                        
                else:
                    print('Invalid grade')
            else:
                print('Invalid test number')
        else:
            print(f'Student with ID {studentID} not found.')
            
        for i in data[1:]:
            afterGrading += str(i) + '\t'
        print("Before grade modification: %s    %s    %s"%(studentID,studentName,beforeGrading.strip()))
        print("After grade modification:  %s    %s    %s"%(studentID,studentName,afterGrading.strip())) 

def addTestGrades(grades): # number 5: Add test grades for the next test for all students. 
    # ----------------------------------------------------------------------------

    if len(grades) == 0:  # We want to check if nothing inside dictionary or not.
        print("There is no information here.")
        
    else: 
        for studentID,data in grades.items(): # Here to see all students with all information (key and values)
            studentGrades = data[1:] # Seperate between studentGrades and studentName
            

        numberOfTest = len(list(studentGrades)) + 1 # Here, we want to know currently number of tests.
        valid = False
        valid2 = False        
        print("Please enter test grades for Test#%d"%numberOfTest) # Here a new number of quiz
        while not valid:
            for studentID,data in grades.items(): 
                enterGrade = input("Please enter grade for student : %s \n"%studentID)
                try:  # try values  
                    if 0 <= float(enterGrade) <= 100:
                        enterGrade = round(float(enterGrade),1)
                        grades[studentID] = data + [enterGrade]
                        valid = True
                        
                        
                    else:
                        valid2 = False
                        while not valid2:
                            enterGrade = input("Invalid Input: Please enter grade for student : %s \n"%studentID)
                            if 0 <= float(enterGrade) <= 100:
                                enterGrade = round(float(enterGrade),1)
                                grades[studentID] = data + [enterGrade]
                                valid = True  
                                valid2 = True
                                
                            else:
                                valid2 = False
                    
                except ValueError: # Except values that might be error and crash the program
                    valid2 = False
                    while not valid2:
                        enterGrade = input("Invalid Input: Please enter grade for student : %s \n"%studentID)
                        try:                 
                            if 0 <= float(enterGrade) <= 100:
                                enterGrade = round(float(enterGrade),1)
                                grades[studentID] = data + [enterGrade]
                                valid2 = True
                                
                            else:
                                valid3 = False
                                while not valid3:
                                    enterGrade = input("Invalid Input: Please enter grade for student : %s \n"%studentID)
                                    if 0 <= float(enterGrade) <= 100:
                                        enterGrade = round(float(enterGrade),1)
                                        grades[studentID] = data + [enterGrade]
                                        valid2 = True  
                                        valid3 = True

                        except ValueError:
                            valid2 = False
                                
                valid = True # After all, we want to close while loop.
            
def addNewStudent(grades): # number 6: Add New Student. # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # ----------------------------------------------------------------------------

    # For any invalid input, the program will ask the user to enter the input again or Press Enter key to go to the main menu.
    for studentID, data in grades.items():
        studentGrades = data[1:]
        
    if len(grades) == 0:  # We want to check if nothing inside dictionary or not.
        
        newStudentInfo = [] # All information of new Student
        studentsNameList = []
        # Checking from the names
        newStudentFirstName = input("Please, student's first name: ").strip()
        if not newStudentFirstName.isalpha():
            valid1 = False
            while not valid1:
                newStudentFirstName = input("Invalid Input: Please, student's first name CLEARLY: ").strip()
                if newStudentFirstName.isalpha():
                    studentsNameList.append(newStudentFirstName)
                    valid1 = True
        else:
            studentsNameList.append(newStudentFirstName)
            
        newStudentSecondName = input("Please, student's second name: ").strip()
        if not newStudentSecondName.isalpha():
            valid1 = False
            while not valid1:
                newStudentSecondName = input("Invalid Input: Please, student's second name CLEARLY: ").strip()
                if newStudentSecondName.isalpha():
                    studentsNameList.append(newStudentSecondName)
                    valid1 = True
        
        else:
            studentsNameList.append(newStudentSecondName)
        
        studentsName = ""
        for i in range(len(studentsNameList)):
            studentsName += studentsNameList[i] + " "
        
        studentsName = studentsName.strip()
        newStudentInfo.append(studentsName)
        

        enterNewStudentGrades = input("Enter a grade test1: ").strip()
        try:
            if 0 <= float(enterNewStudentGrades) <= 100:
                enterNewStudentGrades = round(float(enterNewStudentGrades),1)
                newStudentInfo.append(enterNewStudentGrades)

        except ValueError:
            valid = False
            while not valid:
                enterNewStudentGrades = input("Invalid Input: Enter a grade test1 or Press Enter key to continue: ").strip() 
                if enterNewStudentGrades == "":
                    valid = True

                else:
                    try:
                        if 0 <= float(enterNewStudentGrades) <= 100:
                            enterNewStudentGrades = round(float(enterNewStudentGrades),1)
                            newStudentInfo.append(enterNewStudentGrades)
                            valid = True
                        else:
                            valid = False
                            
                    except ValueError:
                        valid = False

                    
    else:   
        newStudentInfo = [] # All information of new Student
        studentsNameList = []
        # Checking from the names
        newStudentFirstName = input("Please, student's first name: ").strip()
        if not newStudentFirstName.isalpha():
            valid1 = False
            while not valid1: # Here we use valid for while loop.
                newStudentFirstName = input("Invalid Input: Please, student's first name CLEARLY: ").strip()
                if newStudentFirstName.isalpha():
                    studentsNameList.append(newStudentFirstName)
                    valid1 = True

        else:
            studentsNameList.append(newStudentFirstName)
            
        newStudentSecondName = input("Please, student's second name: ").strip()
        if not newStudentSecondName.isalpha():
            valid1 = False
            while not valid1:
                newStudentSecondName = input("Invalid Input: Please, student's second name CLEARLY: ").strip()
                if newStudentSecondName.isalpha():
                    studentsNameList.append(newStudentSecondName)
                    valid1 = True
        
        else:
            studentsNameList.append(newStudentSecondName)
            
        
        studentsName = ""
        for i in range(len(studentsNameList)):
            studentsName += studentsNameList[i] + " "
        
        studentsName = studentsName.strip()
        newStudentInfo.append(studentsName)
        
        for i in range(1,len(studentGrades)+1):
            enterNewStudentGrades = input("Enter a grade test%d: "%i).strip()
            try:
                if 0 <= float(enterNewStudentGrades) <= 100:
                    enterNewStudentGrades = round(float(enterNewStudentGrades),1)
                    newStudentInfo.append(enterNewStudentGrades)
                else:
                    raise ValueError
                    
            except ValueError:
                valid = False
                while not valid:
                    enterNewStudentGrades = input("Invalid Input: Enter a grade test%d or Press Enter key to continue: "%i).strip()

                    try:
                        if 0 <= float(enterNewStudentGrades) <= 100:
                            enterNewStudentGrades = round(float(enterNewStudentGrades),1)
                            newStudentInfo.append(enterNewStudentGrades)
                            valid = True
                            
                        else:
                            valid = False

                    except ValueError:
                        valid = False
            
    return newStudentInfo

def deleteStudent(grades,studentID): # number 7   # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

    if len(grades) == 0:  # We want to check if nothing inside dictionary or not.
        print("There is no information here.")
        return False
    
    else:
        grades.pop(studentID)
        
    # ----------------------------------------------------------------------------
    # To implement option 7, search the Students list or dictionary for the studentID of the student to be deleted. If found, delete it from the list/dictionary. 
    # Note: If the studentID does not exist, display an error message and ask the user for correct input or press Enter key to go to main menu. !!!!!

def saveExit(inputFile,grades): # number 8
    # ----------------------------------------------------------------------------
    # Save all data to the file that was used for reading at the beginning of the program, then terminates the program.
    inputData = open(inputFile,"w") 
    quizes = 0
    for studentID,data in grades.items():
        if len(data[1:]) > quizes: # We want to find a largest number of tests
            quizes = len(data)
    
    for studentID, data in grades.items():
            studentName = data[0]
            studentGrades = data[1:]
            allGrades = [] # ========> list for all student's grades
            allGradesStr = "" # Here we want to add all test grades from list into string.
            for tests in studentGrades:
                allGrades.append(tests)     # so we can complete using list and adding to string.
                
            for tests in allGrades:
                allGradesStr += str(tests) + " "
            
            inputData.write("%s# %s# %s\n" % (studentID, studentName, allGradesStr))


# This is our main function. 
def main(): 
    displayMenu()
    
    # Here, we want to check every file that contains studentsID and grades. If so, the prorgam for you.
    
    valid = False
    while not valid:
        try:
            fileName = input('Enter the file name: ')
            if not fileName.endswith(".txt"):
                raise IOError("File name must end with .txt")
            fileData = open(fileName, "r")
        except IOError as e:
            print("--------------------------Error--------------------------")
            print(e)
            print("Please enter a file again:")
            print("- A file should end with (.txt). Otherwise, you will not be able to open a txt File.")
            print("\nSo Press Enter to return again.")
            key = ""
            while True:
                userkey = input("Press Enter key to continue . . .")
                if userkey == key:
                    break
                
        else:
            valid = True
            grades = extractFile(fileData)
            
    # Here we want to define files into variables and it's all for reading  
    STUDENTS_GRADE_MAIN_FILE = fileData
    # Use a variable (valid) whether the user put a number eight or not.
    validChoice = True
    
    # Here, we define this variable to use it if the user presses Enterkey, the program will return into the menu.
    key = ""
    
    while validChoice: # YOU SHOULD BE CAREFUL FROM PRINTING INFINTE LOOP. !!!!!!!!!!!!!
        try:
            userChoice = input("Please select your choice: ").strip()
            # In this case, you should return the function depending on his 'number'. displayGrades(), for example, has a number of 1 and so on.


            if userChoice == "1": # Here, for the option 1
                displayGrades(grades) # Using the funtion of dispaly
                # Here to check if the user enters key, it will automatically go to the menu. Otherwise, it will ask again to press Enter.
                while True:
                    userkey = input("Press Enter key to continue . . .")
                    if userkey == key:
                        displayMenu()
                        break

            elif userChoice == "2":
            
                if len(grades) == 0:  # We want to check if nothing inside dictionary or not.
                    print("There is no information here.")

                else: 
                    studentID = input("Enter studentID: ") 
                    studentID = studentID.strip()
                    if studentID in grades:
                        dispalyGradesInParticuler(grades,studentID)
                        while True:
                            userkey = input("Press Enter key to continue . . .")
                            if userkey == key:
                                displayMenu()
                                break

                    else: 
                        valid = False
                        validKey = False
                        while not valid:
                            studentID = input("Error: Invalid Id Enter studentID or Press Enter key to go to main menu: ")
                            if studentID == "":
                                valid = True
                                validKey = False
                            studentID = studentID.strip() # Without spaces. Otherwise, it will ask him to write a StudentID clearly.
                            if studentID in grades:
                                dispalyGradesInParticuler(grades,studentID)
                                valid = True
                                validKey = True

                        # Here to check if the user enters key, it will automatically go to the menu. Otherwise, it will ask again to press Enter.
                        if validKey == True:
                            while True:
                                userkey = input("Press Enter key to continue . . .")
                                if userkey == key:
                                    displayMenu()
                                    break

            elif userChoice == "3":
                displayTestAverage(grades) 
                # Here to check if the user enters key, it will automatically go to the menu. Otherwise, it will ask again to press Enter.           
                while True:
                    userkey = input("Press Enter key to continue . . .")
                    if userkey == key:
                        displayMenu()
                        break

            elif userChoice == "4":
                # Here in this option, There is a lot of coding using Try and Except.
                
                # mainValid here, to check for the while loop and other if statements below. If the mainValid variable is equal to False, it will continue to check again and again
                # Otherwise, the while loop here, will be break.
                mainValid = False
                
                # Here to check if the user enters key, it will automatically go to the menu. Otherwise, it will ask again to press Enter.
                validKey = False
                             
                while not mainValid:
                    try:

                        studentID = input("Enter studentID: ").strip()
                        if studentID in grades:
                            valid1 = False
                            while not valid1:
                                try:
                                    quizNumber = input("Please enter quiz number to modify: ").strip()
                                    quizNumber = int(float(quizNumber))
                                    if quizNumber in range(1, len(grades[studentID])):
                                        valid1 = True
                                        # Here, to check again for the quizes using while loop. 
                                        valid2 = False
                                        while not valid2:

                                            try:
                                                newQuizGrade = input("Please enter new quiz %d grade: "%quizNumber).strip()
                                                newQuizGrade = round(float(newQuizGrade),1)
                                                if 0 <= newQuizGrade <= 100:
                                                    modifyParticulerTest(grades,studentID,quizNumber,newQuizGrade)
                                                    # If the user complete all requirements, all variables should be equal to True
                                                    valid2 = True
                                                    mainValid = True
                                                    validKey = True

                                                else:
                                                    # If there is an invalid input, the program should raise ValueError.
                                                    raise ValueError
                                            # So, we use here, ValueError Excpetion.
                                            
                                            
                                            # Also to repeat and checking from the user input using while loop.
                                            except ValueError:
                                                valid2 = False
                                                while not valid2:
                                                    try:
                                                        newQuizGrade = input("Invalid input, please enter new quiz %d grade modify or Press Enter key to continue: "%quizNumber).strip()
                                                        if newQuizGrade == "":
                                                            valid2 = True
                                                            mainValid = True

                                                        else:

                                                            newQuizGrade = input("Please enter new quiz %d grade: "%quizNumber).strip()
                                                            newQuizGrade = round(float(newQuizGrade),1)
                                                            if 0 <= newQuizGrade <= 100:
                                                                modifyParticulerTest(grades,studentID,quizNumber,newQuizGrade)
                                                                # If the user complete all requirements, all variables should be equal to True
                                                                valid2 = True
                                                                mainValid = True
                                                                validKey = True

                                                    except ValueError:
                                                        valid2 = False

                                    else:
                                        # If there is an invalid input, the program should raise ValueError.
                                        raise ValueError
                    
                                # So, we use here, ValueError Excpetion.
                                            
                                            
                                # Also to repeat and checking from the user input using while loop.
                                except ValueError:
                                    # As we said, we want to check all requirements that the user let all variables to be True. 
                                    # For example if the user has already pressed Enter key, the validKey variable will be False and will return into the menu.
                                    valid1 = False
                                    validKey = False
                                    while not valid1:
                                        quizNumber = input("Error: Invalid quiz number : Enter quiz number to modify or Press Enter key to continue: ").strip()
                                        if quizNumber == "":
                                            valid1 = True
                                            mainValid = True

                                        else:  
                                            try:
                                                quizNumber = int(float(quizNumber))
                                                if quizNumber in range(1, len(grades[studentID])):
                                                    valid1 = True
                                                    validKey = True
                                                    valid2 = False
                                                    while not valid2:

                                                        try:
                                                            newQuizGrade = input("Please enter new quiz %d grade: "%quizNumber).strip()
                                                            newQuizGrade = round(float(newQuizGrade),1)
                                                            if 0 <= newQuizGrade <= 100:
                                                                modifyParticulerTest(grades,studentID,quizNumber,newQuizGrade)
                                                                # If the user complete all requirements, all variables should be equal to True
                                                                valid2 = True
                                                                mainValid = True
                                                                validKey = True

                                                            else:
                                                                # If there is an invalid input, the program should raise ValueError.
                                                                raise ValueError
                                                        
                                                        # So, we use here, ValueError Excpetion.
                                            
                                            
                                                        # Also to repeat and checking from the user input using while loop.
                                                        except ValueError:
                                                            valid2 = False
                                                            while not valid2:
                                                                try:
                                                                    newQuizGrade = input("Invalid input, please enter new quiz %d grade modify or Press Enter key to continue: "%quizNumber).strip()
                                                                    if newQuizGrade == "":
                                                                        valid2 = True
                                                                        mainValid = True

                                                                    else:
                                                                        newQuizGrade = round(float(newQuizGrade),1)
                                                                        if 0 <= newQuizGrade <= 100:
                                                                            modifyParticulerTest(grades,studentID,quizNumber,newQuizGrade)

                                                                            valid2 = True
                                                                            mainValid = True
                                                                            validKey = True
                                                                            
                                                                        else:
                                                                            raise ValueError
                                                                            
                                                                except ValueError:
                                                                    valid2 = False
                                                                    
                
                                                else:
                                                    raise ValueError

                                            except ValueError:
                                                valid1 = False

                        else:
                            raise KeyError

                    # If the user didn't write a student ID or some mistakes, it will raise keyEror. 
                    
                    # Note: That all coding in the above is same as below.!!!!!!!!!!!!!!!!!!
                    except KeyError:
                        mainValid = False
                        validKey = False
                        studentID = input("Error: Invalid studentID. Enter studentID or Press Enter key to continue: ")
                        if studentID == "":
                            mainValid = True
                            validKey = False
                        else:  
                            try:
                                studentID = studentID.strip()
                                if studentID in grades:
                                    valid1 = False
                                    while not valid1:
                                        try:
                                            quizNumber = input("Please enter quiz number to modify: ").strip()
                                            quizNumber = int(float(quizNumber))
                                            if quizNumber in range(1, len(grades[studentID])):
                                                valid1 = True

                                                valid2 = False
                                                while not valid2:

                                                    try:
                                                        newQuizGrade = input("Please enter new quiz %d grade: "%quizNumber).strip()
                                                        newQuizGrade = round(float(newQuizGrade),1)
                                                        if 0 <= newQuizGrade <= 100:
                                                            modifyParticulerTest(grades,studentID,quizNumber,newQuizGrade)

                                                            valid2 = True
                                                            mainValid = True
                                                            validKey = True

                                                        else:
                                                            raise ValueError

                                                    except ValueError:
                                                        valid2 = False
                                                        while not valid2:
                                                            try:
                                                                newQuizGrade = input("Invalid input, please enter new quiz %d grade modify or Press Enter key to continue: "%quizNumber).strip()
                                                                if newQuizGrade == "":
                                                                    valid2 = True
                                                                    mainValid = True

                                                                else:

                                                                    newQuizGrade = input("Please enter new quiz %d grade: "%quizNumber).strip()
                                                                    newQuizGrade = round(float(newQuizGrade),1)
                                                                    if 0 <= newQuizGrade <= 100:
                                                                        modifyParticulerTest(grades,studentID,quizNumber,newQuizGrade)

                                                                        valid2 = True
                                                                        mainValid = True
                                                                        validKey = True

                                                            except ValueError:
                                                                valid2 = False

                                            else:
                                                raise ValueError

                                        except ValueError:

                                            valid1 = False
                                            validKey = False
                                            while not valid1:
                                                quizNumber = input("Error: Invalid quiz number : Enter quiz number to modify or Press Enter key to continue: ").strip()
                                                if quizNumber == "":
                                                    valid1 = True
                                                    mainValid = True

                                                else:  
                                                    try:
                                                        quizNumber = int(float(quizNumber))
                                                        if quizNumber in range(1, len(grades[studentID])):
                                                            valid1 = True
                                                            validKey = True
                                                            valid2 = False
                                                            while not valid2:

                                                                try:
                                                                    newQuizGrade = input("Please enter new quiz %d grade: "%quizNumber).strip()
                                                                    newQuizGrade = round(float(newQuizGrade),1)
                                                                    if 0 <= newQuizGrade <= 100:
                                                                        modifyParticulerTest(grades,studentID,quizNumber,newQuizGrade)

                                                                        valid2 = True
                                                                        mainValid = True
                                                                        validKey = True

                                                                    else:
                                                                        raise ValueError

                                                                except ValueError:
                                                                    valid2 = False
                                                                    while not valid2:
                                                                        try:
                                                                            newQuizGrade = input("Invalid input, please enter new quiz %d grade modify or Press Enter key to continue: "%quizNumber).strip()
                                                                            if newQuizGrade == "":
                                                                                valid2 = True
                                                                                mainValid = True

                                                                            else:
                                                                                newQuizGrade = round(float(newQuizGrade),1)
                                                                                if 0 <= newQuizGrade <= 100:
                                                                                    modifyParticulerTest(grades,studentID,quizNumber,newQuizGrade)

                                                                                    valid2 = True
                                                                                    mainValid = True
                                                                                    validKey = True
                                                                                    
                                                                                else:
                                                                                    raise ValueError
                                                                                    
                                                                        except ValueError:
                                                                            valid2 = False
                                                                            
                        
                                                        else:
                                                            raise ValueError

                                                    except ValueError:
                                                        valid1 = False


                                else:
                                    raise KeyError

                            except KeyError:
                                print("Error: Invalid studentID.")          

                if validKey == True: # If the user didn't press enter before, it will ask him to press enter key.
                    valid = False
                    while not valid:
                        userkey = input("Press Enter key to continue . . .")
                        if userkey == key: 
                            valid = True # If the user presses key, the program will ask him to to press Enter again and again.
                            displayMenu() 
                            
            elif userChoice == "5":                        
                addTestGrades(grades)
                # Here to check if the user enters key, it will automatically go to the menu. Otherwise, it will ask again to press Enter.
                while True:
                    userkey = input("Press Enter key to continue . . .")
                    if userkey == key:
                        displayMenu()
                        break

            elif userChoice == "6":
                newStudent = input("Enter new studentID: ").strip()
                if newStudent not in grades and newStudent.isdigit():
                    
                    grades[newStudent] = addNewStudent(grades)
                    # Here to check if the user enters key, it will automatically go to the menu. Otherwise, it will ask again to press Enter.
                    while True:
                        userkey = input("Press Enter key to continue . . .")
                        if userkey == key:
                            displayMenu()
                            break

                else:
                    valid = False
                    while True:
                        newStudent = input("Error: Invalid Id Enter studentID or Press Enter key to go to main menu: ").strip()

                        if newStudent not in grades and newStudent.isdigit():
                            grades[newStudent] = addNewStudent(grades)
                            valid = True
                            break

                        elif newStudent == key:
                            displayMenu()
                            valid = False
                            break

                    if valid == True: # If the user didn't press enter before, it will ask him to press enter key.
                        while True:
                            userkey = input("Press Enter key to continue . . .")
                            if userkey == key:
                                displayMenu()
                                break

            elif userChoice == "7":
                studentID = input("Enter studentID to delete: ")
                studentID = studentID.strip() # Here, If the user writes studentID, it will delete all spaces.
                if studentID in grades:
                    deleteStudent(grades,studentID)
                    print("The studentID %s has been deleted."%studentID)
                    while True:
                        userkey = input("Press Enter key to continue . . .")
                        if userkey == key:
                            displayMenu()
                            break

                else:
                    valid = False
                    while not valid:
                        studentID = input("The studentID does not exists, please press enter to go the menu . . . ")
                        studentID = studentID.strip()
                        if studentID == key:
                            displayMenu()
                            break

                        elif studentID in grades:
                            deleteStudent(grades,studentID)
                            valid = True

                    # Here to check if the user enters key, it will automatically go to the menu. Otherwise, it will ask again to press Enter.
                    if valid == True: # If the user didn't press enter before, it will ask him to press enter key.
                        while True:
                            userkey = input("Press Enter key to continue . . .")
                            if userkey == key:
                                displayMenu()
                                break
            
            # finally, if the user press the choice number 8, the programe will save all information inside the file.
            elif userChoice == "8":
                validChoice = False 
                saveExit(fileName,grades) # So, here we will use this the function saveExit.
            else:
                raise ValueError
            
            
        except ValueError:   
            print("Wrong input, Please try again !!!")
            
    # Close the files.
    fileData.close()
 
main()