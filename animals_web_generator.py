import json

def load_data(file_path):
    """ Loads a JSON file """
    with open (file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")

for animal in animals_data:
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    location = animal["locations"][0]
    if "type" in animal["characteristics"]:
        type = animal["characteristics"]["type"]
        print(f"Name: {name}\nDiet: {diet}\nLocation: {location}\nType: {type}\n")
    else:
        print(f"Name: {name}\nDiet: {diet}\nLocation: {location}\n")