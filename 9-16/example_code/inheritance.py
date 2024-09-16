class user:
    name =""
    def __init__(self, name):
        self.name=name
    def PrintUser(self):
        print("Name = " + self.name)



class Programmer(user):
    language =""
    def __init__(self, name, language):
        #複寫父類別的init，繼承其方法（PrintUser）
        self.name=name
        self.language=language

    def PrintProgrammer(self):
         print("Name = " + self.name + "\n" + "Language = " + self.language )


John = user("John")
John.PrintUser()
Diana = Programmer("diana", "Python")
Diana.PrintUser
Diana.PrintProgrammer()