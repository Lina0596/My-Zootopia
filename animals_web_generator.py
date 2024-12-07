import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data("animals_data.json")


def get_data(animals_data):
    """ Generates content from JSON file """
    output = ""
    for animal in animals_data:
        output += '<li class="cards__item">\n'
        if "name" in animal:
            name = animal["name"]
            output += f"Name: {name}<br/>\n"
        if "diet" in animal["characteristics"]:
            diet = animal["characteristics"]["diet"]
            output += f"Diet: {diet}<br/>\n"
        if "locations" in animal:
            location = animal["locations"][0]
            output += f"Location: {location}<br/>\n"
        if "type" in animal["characteristics"]:
            type = animal["characteristics"]["type"]
            output += f"Type: {type}<br/>\n"
        output += '</li>\n'
    return output

data_str = get_data(animals_data)


def content_html(html_file_path, data_str, new_html_file_path):
    """ Places content in html file and generates a new html file """
    with open(html_file_path, "r") as html_file:
        html_data = html_file.read()
        new_html_data = html_data.replace("__REPLACE_ANIMALS_INFO__", data_str)
    with open(new_html_file_path, "w") as html_file:
        html_file.write(new_html_data)

content_html("animals_template.html", data_str, "animals.html")




