def insert_at_bottom(s, val):
    # base case
    if len(s) == 0:
        s.append(val)
        return

    # recursive case

    x = s.pop()
    insert_at_bottom(s, val)
    s.append(x)


s = []

s.append(10)
s.append(20)
s.append(30)
s.append(40)
s.append(50)

print(s)  # [10, 20, 30, 40, 50]

insert_at_bottom(s, 0)

print(s)  # [0, 10, 20, 30, 40, 50]
