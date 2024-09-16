class Car:
    Name="Carclass"           #定義class variable
    def __init__(self, CName):
        self.Name=CName            #定義object variable
        self.__updateSoftware()    #只能夠在定義CLASS中使用。不可外界(物件)呼叫 

    def __updateSoftware(self):
        print("updating software")

    def drive(self):
        print("driving" + self.Name)
    
Toyota= Car("Toyota")
Toyota.drive()
print(Car.Name)
print(Toyota.Name)

# Toyota.__updateSoftware()   只能夠在定義CLASS中使用。不可外界(物件)呼叫 
