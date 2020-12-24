# CLASS


class Employee:
    no_of_leave = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The name of employee is {self.name} and  salary is {self.salary} and the role is {self.role}"

    @classmethod
    def change_leave(cls, newleave):
        cls.no_of_leave = newleave

    @classmethod
    def str_split(cls, string):
        str_1 = string.split("-")
        print(str_1)
        return cls(str_1[0], str_1[1], str_1[2])

    # Static Method
    @staticmethod
    def static_method():
        print("Good morning")


harrry = Employee("Harry", 455, "Manager")
print(harrry.printdetails())

rohan = Employee("Rohan", 555, "Worker")
print(rohan.printdetails())

print(harrry.no_of_leave)
print(rohan.no_of_leave)

# Class method to change the assign value
Employee.change_leave(34)

print(harrry.no_of_leave)
print(rohan.no_of_leave)

# class method to split the argument passed to the function

karan = Employee.str_split("karan-455-student")
print(karan.printdetails())

print(Employee.static_method())
