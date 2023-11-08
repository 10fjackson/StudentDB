import sqlite3
import csv
conn = sqlite3.connect('/Users/finleyjackson/Documents/CPSC/408/Assignment1/StudentDB')  # establishconnection
mycursor = conn.cursor()
# opening the CSV file
# mycursor.execute("CREATE TABLE Person (first_name TEXT, last_name TEXT, emailTEXT, phone_number int, job TEXT,
# company TEXT, date_of_birth TEXT, ssn TEXT,credit_card_number int);")
with open('/Users/finleyjackson/Documents/CPSC/408/Assignment1/students.csv', mode='r') as file:
    # reading the CSV file
    csvFile = csv.reader(file)

 # # displaying the contents of the CSV file
 # for row in csvFile:
 # print(row[0], row[1])
    count = 0
    for row in csvFile:
        if count == 0:
            count += 1
        else:
            mycursor.execute("INSERT INTO Student('FirstName',"
                      " 'LastName',"
                      " 'Address',"
                      " 'City',"
                      " 'State',"
                      " 'ZipCode',"
                      " 'MobilePhoneNumber',"
                      " 'Major',"
                      " 'GPA' ,"
                      "'isDeleted') "
                      "VALUES (?,?,?,?,?,?,?,?,?,?)",
                      (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], 0,))
            conn.commit()
# mycursor.execute("Select * from Student;")
# rows2 = mycursor.fetchall()
# for row2 in rows2:
#    print(row2)
# mycursor.close()