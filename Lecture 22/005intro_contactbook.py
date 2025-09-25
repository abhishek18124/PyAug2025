from collections import defaultdict

contact_map = defaultdict(list)

contact_map["nitin"].append("1234")
contact_map["nitin"].append("4567")

print(contact_map)

contact_map["hitesh"].append("0000")
contact_map["hitesh"].append("1111")

print(contact_map)

for key in contact_map:
    print(key)
print()

for val in contact_map.values():
    print(val)
print()

for key, value in contact_map.items():
    print(key, value)
