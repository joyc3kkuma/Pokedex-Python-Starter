import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
print(data[0])


# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def I_choose_you(language_choice):
    for pokemon in data:
        if language_choice in pokemon["name"]:
            print(pokemon["name"][language_choice])

# Add a language choice feature and print the pokemons name based on the user input

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
    
# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
