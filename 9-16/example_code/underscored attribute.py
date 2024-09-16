class Sample():

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__C = 3
obj1 = Sample()
print (obj1.a)
print (obj1._b)
print (obj1._Sample__C)
