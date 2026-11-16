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

def languages():
    for language in data:
        print("english, chinese, or japanese?: ")
language_choice = input("english, chinese, or japanese?: ")
if language_choice == "english":
    languages = "english"
elif language_choice == "chinese":
    languages = "chinese"
elif language_choice == "japanese":
    languages = "japanese"
I_choose_you(languages)