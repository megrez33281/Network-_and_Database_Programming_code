class Student:
    Number = 0                      # Number, name 為static 變數
    name="class name"
    def __init__(self, Sname, Num):
        self.name=Sname             # self.Number為物件屬性     
        self.Number=Num

John=Student("John", 1)
Student.Number=Student.Number+1 
print(John.name," ", John.Number)  
print(Student.Number)  
print(Student.name)  
print("**************************")
Mary=Student("Mary", 2)
print(Mary.name," ", Mary.Number)
Student.Number=Student.Number+1

print(Student.Number)  
print(Student.name)
