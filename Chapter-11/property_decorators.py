class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class value of a is {cls.a}")

    @property
    def name(self):
        return self.ename

    @name.setter
    def name(self,value):
        self.ename  = value


e = Employee()
e.a = 45
e.name = "Subrata"
print(e.name)
e.show()