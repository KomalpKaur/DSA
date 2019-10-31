import mysql.connector

class DBHelper:
    def fetchAllStudentInDB(self,list1):
        # 1. create SQL statement
        sql = "select * from student"

        # 2.create connection with database
        con = mysql.connector.connect(user="root", password="", host="127.0.0.1", database="Lab2")

        # 3. Obtain Cursor to execute sql statements
        cursor = con.cursor()
        cursor.execute(sql)

        rows = cursor.fetchall()
        # print(rows)            #print all rows , row is a list of Tuples , 1Tuple represents row, print rows as list of tuples

        self.list1=list1

        for row in rows:
            rm = row[2]  # print all rows in next lines
            self.list1.append(rm)
        print("Before Sorting list of rollnumbers is ",self.list1)

    def mergeSort(self,list1):
        print("Splitting ", list1)
        if (len(list1) > 1):
            mid = len(list1) // 2
            lefthalf = list1[:mid]
            righthalf = list1[mid:]
    
            self.mergeSort(lefthalf)
            self.mergeSort(righthalf)
            i = j = k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    list1[k] = lefthalf[i]
                    i = i + 1
                else:
                    list1[k] = righthalf[j]
                    j = j + 1
                k = k + 1
    
            while i < len(lefthalf):
                list1[k] = lefthalf[i]
                i = i + 1
                k = k + 1
    
            while j < len(righthalf):
                list1[k] = righthalf[j]
                j = j + 1
                k = k + 1
        print("Merging ", list1)

print(" Komalpreet Kaur - 1706460")
class Student:

    def __init__(self, name, urn, phone, address):
        self.name = name
        self.urn = urn
        self.phone = phone
        self.address = address

    def showStudentDetails(self):
        print(">> Name: {}   urn: {}  Phone: {}  Address: {}".format(self.name, self.urn, self.phone, self.address))

db = DBHelper()
list1=[]
db.fetchAllStudentInDB(list1)

db.mergeSort(list1)
print()
print("After applying mergesort...")
print("Sorted list of roll numbers:",list1)
