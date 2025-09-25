capital_map = {
    "india": "kolkata",
    "russia": "moscow",
    "japan": "tokyo",
    "france": "paris",
    "usa": "washington",
}

for key in capital_map:
    print(key)
print()

for key in capital_map.keys():
    print(key)
print()

for val in capital_map.values():
    print(val)
print()


for key, val in capital_map.items():
    print(key, val)
print()

for country_name, capital_name in capital_map.items():
    print(country_name, capital_name)
print()
