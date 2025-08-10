# Simple test of JSON Query

JSON Query documentation can be found here: https://jsonquerylang.org/ 

Environment:
* Python 3.12
* JSON Query
* Pokemon API
* See requirements.txt for libs used

Example of default Pokemon API response: https://pokeapi.co/api/v2/pokemon/1

Example of data filtered via JSON Query:
```
{
    "id": 1,
    "name": "bulbasaur",
    "base_experience": 64,
    "height": 7,
    "weight": 69,
    "type": {
        "name": "grass",
        "url": "https://pokeapi.co/api/v2/type/12/"
    }
}
```
