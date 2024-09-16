class user:
    def __init__(self, name):
        self.name=name
        print("parent constructor")
 
    def PrintUser(self):
        print("Parent: Name = " + self.name)


class Programmer(user):
    # 複寫父類別__init__
    def __init__(self, name, language):
        # self.name=name
        # 用super使用父類別的方法
        super(Programmer, self).__init__(name)
        self.language = language
        print("son constructor")

    def PrintProgrammer(self):
        super(Programmer, self).PrintUser()
        print("Child: Language = " + self.language)
         # print("Name = " + self.name + "\n" + "Language = " + self.language )
    

John = user("John")
John.PrintUser()
print("-"*55)
Diana = Programmer("diana", "Python")
Diana.PrintProgrammer()
print("-"*55)

# 沒有複寫，也可直接沿用父類別的方法
Diana.PrintUser()