# here, we are creating a dict using literal

capital_map = {
    "india": "kolkata",
    "russia": "moscow",
    "japan": "tokyo",
    "france": "paris",
    "usa": "washington",
}

print(capital_map["india"])
print(capital_map["usa"])

if "italy" in capital_map:
    print(capital_map["italy"])
else:
    print("italy is not present in capital_map")


if "india" in capital_map:
    print(capital_map["india"])
else:
    print("india is not present in capital_map")

print(
    capital_map.get("italy", 0)
)  # here 0 is the default value which will be returned in case key is not present
print(capital_map.get("france", 0))

print(capital_map)

capital_map["italy"] = "rome"

print(capital_map)

print("italy" in capital_map)

capital_map["india"] = "new delhi"

print(capital_map)

del capital_map["france"]

print(capital_map)

# del capital_map["spain"] # KeyError since spain is not in capital map
