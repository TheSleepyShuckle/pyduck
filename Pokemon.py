import requests
from poke_types.pokeapi_type_pull_functions import pokeapi_species_types

class Pokemon:

    def __init__(self, species="pikachu") -> None:
        self.species = species
        self.types = pokeapi_species_types(species)


        pass
    