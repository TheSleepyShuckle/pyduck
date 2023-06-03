# Script to return pokemon species types, per pyduck #13
# Will add genericize this in a future ticket...
# In a future ticket, I can add more functions to this, perhaps eventually converting
#   to a class

# Imports
import requests

def pokeapi_species_types(species_name):
    raw_response = pokeapi_species_call(species_name)
    processed_response = pokeapi_convert_raw_output(raw_response)
    types = pokeapi_return_species_types(processed_response)
    return types

def pokeapi_move_types(move_name):
    raw_response = pokeapi_move_call(move_name)
    processed_response = pokeapi_convert_raw_output(raw_response)
    types = pokeapi_return_move_type(processed_response)
    return types

# pokeapi_species_call:  takes as input a Pokemon species's name, return pokeapi's
#   raw output
def pokeapi_species_call(species_name):
    lower_species_name = species_name.lower()
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{lower_species_name}")
    return response


def pokeapi_move_call(move_name):
    lower_move_name = move_name.lower()
    lower_dash_move_name = lower_move_name.replace(" ","-")
    response = requests.get(f"https://pokeapi.co/api/v2/move/{lower_dash_move_name}")
    return response


# pokeapi_convert_raw_output:  takes pokeapi's raw output and converts into a json
#   file
def pokeapi_convert_raw_output(json_string):
    return json_string.json()

# pokeapi_return_types:  take processed pokeapi species data and return a list of 
#   that species's types
def pokeapi_return_species_types(species_dict):
    types = [type_data["type"]["name"] for type_data in species_dict["types"]]
    return types

def pokeapi_return_move_type(move_dict):
    # I don't quite understand how the page structure works, but ChatGPT said do this and it works
    move_type = move_dict['type']['name']
    move_category = move_dict['damage_class']['name']
    #include logic for status vs special/physical move
    if move_category == 'physical':
        return move_type
    elif move_category == 'special':
        return move_type
    else:
        return 'na'