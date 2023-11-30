import json
import requests


response = requests.get('https://swapi.dev/api/starships/?search=Millennium Falcon')
data = response.json()
ship = data['results'][0]

pilots_info = []
for pilot_url in ship['pilots']:
    pilot_response = requests.get(pilot_url)
    pilot_data = pilot_response.json()
    homeworld_response = requests.get(pilot_data['homeworld'])
    homeworld_data = homeworld_response.json()
    pilots_info.append({
        'name': pilot_data['name'],
        'height': pilot_data['height'],
        'mass': pilot_data['mass'],
        'homeworld': homeworld_data['name'],
        'homeworld_url': pilot_data['homeworld'],

    })

ship_info = {
    'name': ship['name'],
    'max_atmosphering_speed': ship['max_atmosphering_speed'],
    'class': ship['starship_class'],
    'pilots': pilots_info
}

print(json.dumps(ship_info, indent=4))

with open('ship_info.json', 'w') as file:
    json.dump(ship_info, file ,indent=4)