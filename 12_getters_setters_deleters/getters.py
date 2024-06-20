class Employee:

    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last
        # self.email = f"{self.first}.{self.last}@gmail.com"

    @property
    def fullname(self):
        return f"{self.first} {self.last}"

    @property
    def email(self):
        return f"{self.first}.{self.last}@gmail.com"


emp1 = Employee("Abhirup", "Ghosh")
emp1.first = "Abhi"
emp1.last = "G"
# PROBLEM IS RIYAL! THE FIRST AND LAST IS GETTING CHANGED ALSO THE fullname() function is working fine then wtf happneded to email?
print(emp1.first)
print(emp1.last)
print(emp1.email)
# print(emp1.fullname())
print(emp1.fullname)

## Now this can be solved by making the email function like fullname function but that means we have to give () to everywhere email is used previously as an attribute

# def email(self):
#         return f"{self.first}.{self.last}@gmail.com"

## the above is one solution but we dont want to change the email attribute to email()

# @ https://www.youtube.com/watch?v=jCzT9XFZ5bw

# ~ The @property decorater makes a function an attribute





