class Employee:
    name = "Paul" # Public member
    _age = 30 # Protected member
    __salary = 5000 # Private member


paul = Employee()
print(paul.name)