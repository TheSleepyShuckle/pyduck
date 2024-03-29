import requests
from pokeapi_type_pull_functions import pokeapi_species_types, pokeapi_move_types
# Only need to import the function that gets pulled

#Nominal case test

species0 = "venusaur"
species1 = "charizard"
species2 = "blastoise"

print(pokeapi_species_types(species0))
print(pokeapi_species_types(species1))
print(pokeapi_species_types(species2))

# Capital letter tests + minor misspelling tests...just want to see what
#  pokeapi does

species3 = "BUTTERFREE"
# species4 = "Beeedrill" # pokeapi can't handle
# species5 = "Raticatte" #pokeapi can't handle

print(pokeapi_species_types(species3))
# print(pokeapi_species_types(species4))
# print(pokeapi_species_types(species5))

move1 = "ember"
move2 = "Flying Press"
move3 = "Will-o-Wisp"
move4 = "Protect"

print(pokeapi_move_types(move1))
print(pokeapi_move_types(move2))
print(pokeapi_move_types(move3))
print(pokeapi_move_types(move4))
