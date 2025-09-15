class Customer:
    def __init__(self, name: str, age: int, gender: str, balance: float) -> None:
        # print(f"We are in the __init__() of the Cusomter Class")
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance

    is_human = True


c1 = Customer("abhishek", 28, "male", 100.5)
print(f"name={c1.name}, age={c1.age}, gender={c1.gender}, balance={c1.balance}")
# print("name=", c1.name, "age=", c1.age, "gender=", c1.gender, "balance=", c1.balance)
print(c1)
print(Customer.is_human, c1.is_human)

c2 = Customer("shashank", 30, "male", 200.5)
print(f"name={c2.name}, age={c2.age}, gender={c2.gender}, balance={c2.balance}")
print(c2)
print(Customer.is_human, c2.is_human)
