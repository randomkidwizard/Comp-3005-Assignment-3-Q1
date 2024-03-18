#import this library to be able to interact with postgres
import psycopg2

#connect to the postgres database
conn = psycopg2.connect(
    "dbname='A3' user='postgres' host='localhost' password='postgres'"
)
cur = conn.cursor()

#function that retrieves and displays all records from the students table.
def getAllStudents():
    cur.execute("SELECT * FROM students;") #SQL code selecting all records from students
    for record in cur.fetchall():
        print(record) #print them all 

#function that inserts a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);",  #SQL code insert a new record with the paramaters specified into students
                (first_name, last_name, email, enrollment_date))
    conn.commit()

#function that updates the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email):
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s;",  #SQL code that updates the email of a specific student identified by 'student_id' with new_email
                (new_email, student_id))
    conn.commit()

#function that deletes the record of the student with the specified student_id
def deleteStudent(student_id):
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,)) #SQL code that delete a specific record from 'students' table identified by 'student_id'
    conn.commit()

getAllStudents()
print("-------------------------------------------------------------------------")

'''
addStudent('Amin', 'Robleh', 'amin@example.com', '2023-09-03')
print("-------------------------------------------------------------------------")
getAllStudents()

updateStudentEmail(1, 'john.newemail@example.com')
getAllStudents()
print("-------------------------------------------------------------------------")

'''
deleteStudent(3)
print("-------------------------------------------------------------------------")
getAllStudents()

# Close the database connection
conn.close()
