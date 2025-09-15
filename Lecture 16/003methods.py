class Customer:
    def __init__(self, name: str, age: int, gender: str, balance: float) -> None:
        # print(f"We are in the __init__() of the Cusomter Class")
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance

    def describe(self):
        info = f"name = {self.name} age = {self.age} gender = {self.gender} balance = {self.balance}"
        print(info)

    def __str__(self):
        info = f"name = {self.name} age = {self.age} gender = {self.gender} balance = {self.balance}"
        return info


c1 = Customer("abhishek", 28, "male", 100.5)
# c1.describe()
print(c1)

c2 = Customer("shashank", 30, "male", 200.5)
# c2.describe()
print(c2)
