import json
import requests

from typing import Dict

from jsonquerylang import jsonquery


def ask_id() -> int:
    """ Show prompt to user to enter Pokemon ID """

    pokemon_id = input('Enter Pokemon ID [1-10277]: ')

    return int(pokemon_id)


def request_pokemon_data(id_: int) -> Dict:
    """ Send request to Pokemon API """

    response = {}

    try:
        response = requests.get(
            f'https://pokeapi.co/api/v2/pokemon/{id_}/',
            timeout=(30,30)
        ).json()
    except requests.exceptions.JSONDecodeError:
        print(F'No data for ID {id_}')
    except Exception as e:
        print(f'Unexpected exception: {e}')

    return response


def get_main_properties(pokemon_info: Dict) -> Dict:
    """ Get main Pokemon properties """
 
    # TODO: it's unclear how to get deeply nested data
    output = jsonquery(
        pokemon_info,
        """
            pick(.id, .name, .base_experience, .height, .weight, .types.0.type)
        """
    )

    return output


def run() -> None:
    pokemon_id = ask_id()
    
    pokemon_info = request_pokemon_data(pokemon_id)

    if pokemon_info:
        final_data = get_main_properties(pokemon_info)

        print(json.dumps(final_data, indent=4))


if __name__ == "__main__":
    run()
