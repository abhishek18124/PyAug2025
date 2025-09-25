# here, we are creating a dict using literal

capital_map = {
    "india": "new delhi",
    "russia": "moscow",
    "japan": "tokyo",
    "france": "paris",
    "usa": "washington",
}

print(len(capital_map))

print(capital_map.keys())
print(capital_map.values())
print(capital_map.items())

# here, we are creating a dict using a list of tuples with the help dict()

key_value_pairs = [("india", "new delhi"), ("russia", "moscow"), ("japan", "tokyo")]

capital_map_2 = dict(key_value_pairs)

print(type(capital_map_2))
print(len(capital_map_2))

print(capital_map_2.keys())
print(capital_map_2.values())
print(capital_map_2.items())


d = {}

print(type(d))
print(len(d))

d = dict()

print(type(d))
print(len(d))
