animals = [
    {
        "name": "Bird",
        "wings": True,
        "legs": 2,
        "habitat": "Air",
        "tail": True,
        "type": "Bird"
    },
    {
        "name": "Dog",
        "wings": False,
        "legs": 4,
        "habitat": "Land",
        "tail": True,
        "type": "Mammal"
    },
    {
        "name": "Fish",
        "wings": False,
        "legs": 0,
        "habitat": "Water",
        "tail": True,
        "type": "Fish"
    },
    {
        "name": "Snake",
        "wings": False,
        "legs": 0,
        "habitat": "Land",
        "tail": True,
        "type": "Reptile"
    },
    {
        "name": "Horse",
        "wings": False,
        "legs": 4,
        "habitat": "Land",
        "tail": True,
        "type": "Mammal"
    },
    {
        "name": "Whale",
        "wings": False,
        "legs": 0,
        "habitat": "Water",
        "tail": True,
        "type": "Mammal"
    }
]

name = input("Input animal name : ")

def has_wings(animal):
    if animal["wings"]:
        print(f'{animal["name"]} has wings.')
        
def no_wings(animal):
    if not animal["wings"]:
        print(f'{animal["name"]} does not have wings.')
        
def has_four_legs(animal):
    if animal["legs"] == 4:
        print(f'{animal["name"]} has four legs.')
        
def has_two_legs(animal):
    if animal["legs"] == 2:
        print(f'{animal["name"]} has two legs.')
        
def lives_in_water(animal):
    if animal["habitat"] == "Water":
        print(f'{animal["name"]} lives in water.')
        
def lives_on_land(animal):
    if animal["habitat"] == "Land":
        print(f'{animal["name"]} lives on land.')
        
def has_tail(animal):
    if animal["tail"]:
        print(f'{animal["name"]} has a tail.')
        
def no_tail(animal):
    if not animal["tail"]:
        print(f'{animal["name"]} does not have a tail.')
        
def is_mammal(animal):
    if animal["type"] == "Mammal":
        print(f'{animal["name"]} is a mammal.')
        
def is_reptile(animal):
    if animal["type"] == "Reptile":
        print(f'{animal["name"]} is a reptile.')

for animal in animals:
    if animal["name"] == name:
        has_wings(animal)
        no_wings(animal)
        has_four_legs(animal)
        has_two_legs(animal)
        lives_in_water(animal)
        lives_on_land(animal)
        has_tail(animal)
        no_tail(animal)
        is_mammal(animal)
        is_reptile(animal)