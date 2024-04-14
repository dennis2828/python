# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page",
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(isinstance(band, dict))
print(len(band))

# Access  items

print(band["vocals"])
print(band.get("guitar"))

# list all keys

print(band.keys())

# list all values
print(band.values())

# list of key value pairs

print(band.items())

print("guitar" in band)
print("triangle" in band)

#Change values

band["vocals"] = "Coverdale"
band.update({"bass":"JPJ"})
print(band)

print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) # tuple
print(band)

# Delete and clear

band["drums"] = "Bonham"

del band["drums"]

print(band)