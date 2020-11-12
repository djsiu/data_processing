###
# dataProcessing.py
# CMPT 120
# ASSIGNMENT #6 - Data Processing
#
# description:
# This program will process students' survey data, process
# the data, return some statistics and allow you to
# compare as many pairs of students' survey answers as you want
#
# by Benny Cao, Denise Siu, and Kayla Yu
# some code provided by Diana Cukierman
# created on 11/25/2019



#function for initializing numbers and lists

def read_string_list_from_file(the_file):

    '''
    Author: Diana Cukierman
    If you revise, indicate so here and how:
    - we changed the code given by making the localList_ofstrings a global variable
    - we created lists with the names and the answers (and made those variables global)
    - we made several traces for the lists and strings
    
    READING OF TEXT FILE
    String ---> List of Strings

    the_file is a string representing several 'lines',
    each line is a string, possibly including spaces , and ending with \n

    THIS FUNCTION GENERATES AND RETURNS  A LIST OF STRINGS

    Assumptions:
    1) the_file is in the same directory (folder) as this program 
    2) lines have a "\n" at the end, that is, after each 'line' (student)
       in the file , there is a new line character ("\n"), including the last
       line  in the_file
    3) for this problem each line has alphabetic and numeric values
       separated with spaces, but this does not affect this function. 
    '''

    
    global localList_ofstrings #list of string with students' names and answers
    global nameList #list of the names of the students
    global ansList #list of the students' answers


    
# lists being created for every person (with name and answers)
    fileRef = open(the_file,"r")      # opening file to be read
    localList_ofstrings=[]             # new list being constructed 
    stringofNames = []
    for line in fileRef:
        string = line[0:len(line)-1]  # -1 to eliminate trailing '\n'
                                      # of each line 
        localList_ofstrings.append(string)      # adds string (line) to list


# creating a list of names
    nameList = []
    for element in localList_ofstrings:
        newElem = element.split()
        nameList.append(newElem[0]) #makes a new list for name

# creating a list of list of answers
    ansList = [] 
    for element in localList_ofstrings:
        newElem = element.split()
        ansList.append(newElem[1:])


######### INITIAL PROCESSING
    print("\nInitial processing... ")

# PRINT list of strings answers
    print ("\n TRACE, the list OF STRINGS is:\n")
    print(localList_ofstrings)

# PRINT one student per line and list of responses
    for i in range(len(nameList)):
        print(nameList[i],"\t--",ansList[i])


    fileRef.close()
    return localList_ofstrings


# creating the output file with the names and averages
def write_perstudent_to_file(the_file):

    '''
    Author: Diana Cukierman
    If you revise, indicate so here and how:
    - we created a new file called "OUTperstudent.csv"
    - in that file we but the names of all the students and thier average answers
    - we also added a printed trace of the names and averages

    list of Strings --> ()  (A file is saved it the current folder)

    You need to ensure that lout_Strings has the appropriate contents
    according to the assumptions (and needed to write a text file)

    Assumptions:
    1) the_file will be saved in the same directory (folder) as this program 
    2) lout_Strings is formatted so that it
       2.0) is a list of strings
       2.1) each string contains one student's  data  
       2.2) each  string for one student includes the name
       2.3) each  string includes a comma after the students' name,then the avg
       2.4) each string includes a new line ('\n') at the end
    '''
    
    fileRef = open(the_file,"r")
    outFile = open("OUT_perstudent.csv", "w")
    print("TRACE, list of strings ready to save to output file, one per line:")
    
    aline = fileRef.readline()
    while aline:
        items = aline.split()
        total=0
        for i in range(1,len(items)+1):
            total+=int(i)
        avg=total/(len(items)-1)
        
        dataline = items[0] + ',' + str(avg)
        print(dataline)
        outFile.write(dataline + '\n')
        
        aline = fileRef.readline()
        
    fileRef.close()
    outFile.close()
    
    return

# function determining the most number of 4 or 5 any student answered with
def maxAgree(answers):
    maxAgree = []
    for i in range(len(answers)):
        counter = 0
        for k in range(len(answers[i])):
            newList = answers[i]
            if str(newList[k]) == "4" or str(newList[k]) == "5":
                counter += 1
        maxAgree.append(counter)
    return max(maxAgree)

# function for the ans average per question
def averageQuestion():
    averagePerQuestion = []
    listO = [0]*21
    for i in range(len(ansList)):
        for k in range(len(ansList[i])):
            newList = ansList[i]
            listO[k] += int(newList[k])
    for i in range(len(listO)):
        listO[i] = listO[i]/len(nameList)
        listO[i] = round(listO[i],2)
    return listO

# a function to print the average answers of each question
def printAvg(average):
    for i in range(numQuestions):
        print(i+1, "-", average[i])

# function for the most agreed on questions
def mostAgreed(avg):
    maxQs=""
    maxNum=max(avg)
    for i in range(len(avg)):
        if avg[i] == maxNum:
            maxQs+=str(i+1)+", "
    maxQs=maxQs[:-2]
    return maxQs

# function compares two students' answers and determines how many they have in common
def process_ONE_pair(fstPerson,sndPerson):
    simCounter = 0
    numQs=len(ansList[0])
    student1=ansList[nameList.index(fstPerson)]
    student2=ansList[nameList.index(sndPerson)]
    # counting the number of similar responses they have
    for i in range(numQs):
        if student1[i] == student2[i]:
            simCounter += 1
    simPercentage=(simCounter/numQs)*100
    if simPercentage >= 90:
        print("\n",fstPerson,"and",sndPerson,"really do have a lot in common (>90%)!")
    elif simPercentage >= 50:
        print("\n",fstPerson,"and",sndPerson,"have about half opinions in common!")
    elif simCounter >= 2:
        print("\n",fstPerson,"and",sndPerson,"have just a few opinions in common (<50%)!")
    else:
        print("\n",fstPerson,"and",sndPerson,"have nothing in common!")
    return simCounter

# function to allow the user to input students they want to compare
def userInputCompare(names):
    count=0
    end=True
    while count<int(pairs) and end:
        firstStudent=input("Please provide the first name in the pair (or END to finish) ==> ")
        if firstStudent.upper() == "END":
            end=False
        else:
            secondStudent=input("Please provide the second name in the pair ==> ")
            if (firstStudent in names) and (secondStudent in names):
                print("TRACE, they have:",process_ONE_pair(firstStudent,secondStudent),"answers in common\n")
            else:
                print("\nSorry, at least one name is not in the data!\nTRY AGAIN\n")
            count+=1
        if count == int(pairs):
            print("Okay, you've reached the maximum of students you can compare:",pairs)
    
# function printing the introduction
def printIntro():
    print("WELCOME to the CMPT 120 Preferences and Similarities system!")
    print("============================================================")
    print("This system will process data from the file: IN_all_data.txt") 
    print("The file has answers of students opinions from 1 - strongly disagree  to 5- strongly agree")
    print("The system will produce:") 
    print("- an output file with avgs per student: OUT_perstudent.csv")
    print("- several statistics")
    print("You will also be able to check if pairs of students are similar")
    print()

# function printing the introduction for the similarities portion of the program
def printSimIntro():
    print("\n\nNOW... LET'S SEE SIMILARITIES BETWEEN PAIRS OF STUDENTS!!...") 
    print("============================================================")

    print("You can check up to", pairs,"pairs")
    

# calling the function from before
printIntro()

# allowing the user to choose the max number of students they can compare
isDigit=False
while not isDigit:
    pairs=input("Maximum number of pairs ==> ")
    if not pairs.isdigit():
        print("What you provided is not an integer  number, please re-type")
    else:
        isDigit=True
read_string_list_from_file("IN_all_data.txt")


# determining the number of people and the number of questions
print()
numPeople=len(nameList)
numQuestions=len(ansList[0])
print("the number of students is:",numPeople)
print("the number of questions is:", numQuestions)

print("\n\n")
print("Processing all students' responses  ...")
print("All students' responses have been processed ...\n")


### CALCULATED STATS
print("SOME STATS!!")
print("=============\n")
print("The input file had responses from:",numPeople,"students")
print("Each student responded to:",numQuestions,"questions")
print("The maximum agrees (response 4 or 5) in a student was:", maxAgree(ansList),"\n")

# PRINT the average for the questions
print("The averages per question were:")
print("(in the format: question num - average)\n")
printAvg(averageQuestion())
print("\nThe most agreed questions were:",mostAgreed(averageQuestion()))

# similarities between students
printSimIntro()
print("Here is a list of the students you can choose from:\n",nameList,"\n")
userInputCompare(nameList)

# calling the function to create a new file
print("\nOutput file being saved...")
write_perstudent_to_file("IN_all_data.txt")

print("\nAll done! Bye!")




