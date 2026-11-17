import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

def I_choose_you(language_choice):
    for pokemon in data:
        if language_choice in pokemon["name"]:
            print(pokemon["name"][language_choice])

def ball():
    for ball in data:
        print("Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost, Steel, Fire, Water, Grass, Electric, Psychic, Ice, Dragon, Dark, Fairy")
pokemon_types = input("Normal, Fighting, Flying, Poison, Ground, Rock, Bug, Ghost, Steel, Fire, Water, Grass, Electric, Psychic, Ice, Dragon, Dark, Fairy")
if pokemon_types == "Normal":
    ball = "Normal"
elif pokemon_types == "Fighting":
    ball = "Fighting"
elif pokemon_types == "Flying":
    ball = "Flying"
elif pokemon_types == "Poison":
    ball = "Posion"
elif pokemon_types == "Ground":
    ball = "Ground"
elif pokemon_types == "Rock":
    ball = "Rock"
elif pokemon_types == "Bug":
    ball = "Bug"
elif pokemon_types == "Ghost":
    ball = "Ghost"
elif pokemon_types == "Steel":
    ball = "Steel"
elif pokemon_types == "Fire":
    ball = "Fire"
elif pokemon_types == "Water":
    ball = "Water"
elif pokemon_types == "Grass":
    ball = "Grass"
I_choose_you(ball)