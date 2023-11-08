import sqlite3
import requests


conn = sqlite3.connect('./StudentDB') #establish connection to db
mycursor = conn.cursor() #cursor allows python to execute SQL statements
def main():
    print("Choose the option you wish to complete:")
    print("1. Display all students and their attributes")
    print("2. Add new student")
    print("3. Update student")
    print("4. Delete student")
    print("5. Search/Display students by Major, GPA, City, State or Advisor")

    num = input()
    if num == '1' or num == '2' or num == '3' or num == '4' or num == '5':
        print("one moment while I handle your request")
        if num == '1':
            display_students()
        if num == '2':
            StudentID = getStudentCount() + 1
            firstName = getStudentFirstName()
            lastName = getStudentLastName()
            GPA = getStudentGPA()
            major = getStudentMajor()
            facultyAdvisor = getStudentFacultyAdvisor()
            address = getStudentAddress()
            city = getCity()
            state = getState()
            zipCode = getZipcode()
            mobilePhoneNumber = getPhoneNum()
            isDeleted = 0
            #Add new student
            add_student(StudentID, firstName, lastName, GPA, major, facultyAdvisor, address, city, state, zipCode, mobilePhoneNumber, isDeleted)
        if num == '3':
            print("What would you like to update:")
            print("1. The students major")
            print("2. The students Faculty Advisor")
            print("3. The students Mobile Phone Number")
            inp = input()
            if inp.isnumeric() == True:
                if inp == '1':
                    print("Enter the students ID number you wish to change")
                    StudentID = getStudentID()
                    print("Enter the new major you wish to switch the student into")
                    major = getStudentMajor()

                    update_student_major(StudentID, major)
                elif inp == '2':
                    print("Enter the students ID number you wish to change")
                    StudentID = getStudentID()
                    print("Enter the new Faculty Advisor you wish to change the student to")
                    advisor = getStudentFacultyAdvisor()

                    update_student_advisor(StudentID, advisor)
                elif inp == '3':
                    print("Enter the students ID number you wish to change")
                    StudentID = getStudentID()
                    print("Enter the new phone number you wish to replace the old one with in the students information")
                    number = getPhoneNum()

                    update_student_number(StudentID, number)


        if num == '4':
            print("Enter the ID number of the student you wish to delete")
            StudentID = getStudentID()
            delete_student(StudentID)
            print("The Student has been deleted")


        if num == '5': #Search/Display students by Major, GPA, City, State and Advisor.
            print("What would you like to search by:")
            print("1. Major")
            print("2. GPA")
            print("3. City")
            print("4. State")
            print("5. Advisor")
            sel = input()
            if sel == '1':
                searchByMajor()

            elif sel == '2':
                searchByGPA()
            elif sel == '3':
                searchByCity()
            elif sel == '4':
                searchByState()
            elif sel == '5':
                searchByAdvisor()
            else:
                print("Please enter a number 1-5")
                main()

        else:
            print("Request finished")
            main()





    else:
        print("!!!SORRY, please enter a number 1-5!!!")
        main()
    main()


def getStudentCount():
    mycursor.execute("SELECT * FROM Student")
    rows = mycursor.fetchall()
    length = len(rows)
    return length

def getStudentID():
    print("Enter the students id number")
    id = input()
    length = getStudentCount()
    numlength = int(length)
    if id.isnumeric() == True:
        numid = int(id)
        if numid <= numlength and numid > 0:
            return numid
        else:
            print("This student does not exist")
            getStudentID()
    else:
        print("Sorry, please enter a valid student id")
        getStudentID()
def getStudentLastName():
    print("Enter the students last name")
    lname = input()
    if lname.isalpha() == True:
        return lname
    else:
        print("Sorry, please enter a valid name")
        getStudentLastName()

def getStudentFirstName():
    print("Enter the students first name")
    fname = input()
    if fname.isalpha() == True:
        return fname
    else:
        print("Sorry, please enter a valid name")
        getStudentFirstName()

def getStudentGPA():
    print("Enter the students GPA on a 0 - 4.0 scale")
    gpa = input()
    try:
        float(gpa)
        bool = True
    except ValueError:
        bool = False
    if bool:
        gpa = float(gpa)
        print(gpa)
        if gpa >= 0.0 and gpa <= 4.0:
            print("this is a valid gpa")
            return gpa
        else:
            print("Please enter a GPA on the 4.0 scale")
            getStudentGPA()
    else:
        print("Sorry, please enter a valid numeric GPA")
        getStudentGPA()

def getStudentMajor():
    print("Enter major:")
    major = input()
    if all(x.isalpha() or x.isspace() for x in major):
        return major
    else:
        print("Sorry, please enter a valid major")
        getStudentMajor()


def getStudentFacultyAdvisor():
    print("Enter Faculty Advisor:")
    advisor = input()
    if advisor == "":
        return None
    elif all(x.isalpha() or x.isspace() for x in advisor):
        return advisor
    else:
        print("Sorry, please enter a valid advisor name or leave blank and simply click enter")
        getStudentFacultyAdvisor()


def getStudentAddress():
    print("Enter the students address")
    major = input()
    return major

def getCity():
    print("Enter the name of the city that they live in")
    city = input()
    if all(x.isalpha() or x.isspace() for x in city):
        return city
    else:
        print("Sorry, please enter a valid City name")
        getCity()

def getState():
    print("Enter the students State")
    state = input()
    if state in ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware",
                 "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky",
                 "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi",
                 "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico",
                 "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania",
                 "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont",
                 "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]:
        return state
    else:
        print("Sorry, please enter a valid State")
        getState()

def getZipcode():
    print("Enter the students ZipCode")
    zip = input()
    if zip.isnumeric() == True and len(zip) == 5:
        return zip
    else:
        print("Sorry, please enter a valid 5 digit zipcode")
        getZipcode()


def getPhoneNum():
    print("Enter phone number")
    num = input()
    if num.isnumeric() == True and len(num) == 10:
        return num
    else:
        print("Sorry, please enter a valid 10 digit phone number")
        getPhoneNum()
def display_students():
    mycursor.execute("SELECT * FROM Student WHERE isDeleted != 1")
    rows = mycursor.fetchall()
    print(len(rows))
    for row in rows:
        print(row)
    conn.commit()

def add_student(StudentID, firstName, lastName, GPA, major, facultyAdvisor, address, city, state, zipCode, mobilePhoneNumber, isDeleted):
    mycursor.execute("INSERT INTO Student VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (StudentID, firstName, lastName, GPA, major, facultyAdvisor, address, city, state, zipCode, mobilePhoneNumber, isDeleted))
    conn.commit()

def update_student_major(StudentID, major):
    mycursor.execute("UPDATE Student SET Major = ? WHERE StudentId = ?", (major, StudentID))
    conn.commit()


def update_student_advisor(StudentID, advisor):
    mycursor.execute("UPDATE Student SET Advisor = ? WHERE StudentId = ?", (advisor, StudentID))
    conn.commit()

def update_student_number(StudentID, advisor):
    mycursor.execute("UPDATE Student SET MobilePhoneNumber = ? WHERE StudentId = ?", (advisor, StudentID))
    conn.commit()

def delete_student(StudentID):
    mycursor.execute("UPDATE Student SET isDeleted = ? WHERE StudentId = ?", (1, StudentID))
    conn.commit()

def searchByMajor():
    maj = getStudentMajor()
    mycursor.execute("SELECT * FROM Student WHERE Major = ?", (maj,))
    rows = mycursor.fetchall()
    if len(rows) == 0:
        print("!!SORRY!! There were no students with the major of " + str(maj))
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    else:
        for row in rows:
            print(row)
        conn.commit()


def searchByGPA():
    GPA = getStudentGPA()
    mycursor.execute("SELECT * FROM Student WHERE GPA = ?", (GPA,))
    rows = mycursor.fetchall()
    if len(rows) == 0:
        print("!!SORRY!! There were no students with the GPA of " + str(GPA))
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    else:
        for row in rows:
            print(row)
        conn.commit()


def searchByCity():
    city = getCity()
    mycursor.execute("SELECT * FROM Student WHERE City = ?", (city,))
    rows = mycursor.fetchall()
    if len(rows) == 0:
        print("!!SORRY!! There were no students with the city of " + str(city))
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    else:
        for row in rows:
            print(row)
        conn.commit()

def searchByState():
    state = getState()
    mycursor.execute("SELECT * FROM Student WHERE State = ?", (state,))
    rows = mycursor.fetchall()
    if len(rows) == 0:
        print("!!SORRY!! There were no students with the state of " + str(state))
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    else:
        for row in rows:
            print(row)
        conn.commit()

def searchByAdvisor():
    adv = getStudentFacultyAdvisor()
    mycursor.execute("SELECT * FROM Student WHERE FacultyAdvisor = ?", (adv,))
    rows = mycursor.fetchall()
    if len(rows) == 0:
        print("!!SORRY!! There were no students with the advisor of " + str(adv))
        print("|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
    else:
        for row in rows:
            print(row)
        conn.commit()

main()
