class user:
    name ="USERICLASS"  #static variable
    def __init__(self, name):
        # 建立物件
        self.name=name
    def PrintName(self):
        print("Name = " + self.name)

John = user("John")
John.PrintName()
print(user.name)
print(John.name)

