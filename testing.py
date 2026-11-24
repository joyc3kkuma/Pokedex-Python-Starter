import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

pokemon_types = []

for ball in data:
        pokedex.append()
pokemon_types = input("Pokemon! I choose:  ")
