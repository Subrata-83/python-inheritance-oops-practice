class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is {self.name} and the salary is {self.company}")


class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")

# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showlanguge(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")

a = Employee()
b = Programmer()

b.show
b.printLanguage()
b.showlanguage()
