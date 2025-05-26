class Employee:
    name = "Paul" # Public member
    _age = 30 # Protected member
    __salary = 5000 # Private member
        # _Employee__salary

class Test(Employee):
    def showData(self):
        print("Age: ", self._age)


paul = Test()
print(paul.name)
paul.showData()
#print(paul.__salary)
employee = Employee()
#print(employee.__salary)
print(employee._Employee__salary)

