#notes

#collection of key and value pairs

car= {
    "silver":  "jeep",
    "modle": "strangler",
    "color": "orange",
    "year": 2011
}
print(car["year"])
keys=list(car.keys())
for key in keys:
    print(f"{key} is {car[key]}")
print(len(car))
if "transmission" in car:
    print(car["transmission"])
else:
    car["transmission"] = "automatic"
car.pop("color")
print(*car)
print(car.items())







avatar= {
    "water": {
        "katara": "water bender",
        "sokka": "backbender"
    },
    "earth":{
        "Toph": "earth bender. The Goat"
    },
    "air":{
        "Aang": "air nomad, the avatar"
    },
    "fire":{
        "zuko": "fire bender",
        "iroh": "knower of wisdom and fire bender"
    },
    "villains":{
        "cabbage man": "my cabbages"
    }

}


print(avatar["fire"]["iroh"])
print()