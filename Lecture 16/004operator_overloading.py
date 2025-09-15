class Customer:
    def __init__(self, name: str, age: int, gender: str, balance: float) -> None:
        # print(f"We are in the __init__() of the Cusomter Class")
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance

    def __eq__(self, other):
        return (
            self.name == other.name
            and self.age == other.age
            and self.gender == other.gender
            and self.balance == other.balance
        )


c1 = Customer("abhishek", 28, "male", 100.5)
c2 = Customer("abhishek", 28, "male", 100.5)

if c1 == c2:  # c1.__eq__(c2)
    print("Equal")
else:
    print("Not Equal")

print(c1 is c2)  # address are being compared
