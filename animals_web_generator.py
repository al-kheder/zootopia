import json


def load_data(file_path):
    try:
        with open(file_path, "r") as handle:
            data = json.load(handle)
        return data
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' contains invalid JSON.")
        return None


def get_skin_types(animal_data):
    skin_types = set()
    for animal in animal_data:
        if "characteristics" in animal and "skin type" in animal["characteristics"]:
            skin_types.add(animal["characteristics"]["skin type"])
    return list(skin_types)


def generate_animals_info(animal_data):
    animals_info = ""
    for animal in animal_data:
        animals_info += '<li class="cards__item">'
        animals_info += f"<div class='card__title'>{animal['name']}</div>"
        animals_info += "<p class='card__text'>"
        animals_info += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br/>"
        animals_info += f"<strong>Location:</strong> {animal['locations'][0]}<br/>"
        if "type" in animal["characteristics"]:
            animals_info += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>"
        animals_info += "</p></li>"
    return animals_info


def generate_html(template_path, output_path, animals_info):
    try:
        with open(template_path, "r") as handle:
            template = handle.read()
        new_content = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)
        with open(output_path, "w") as handle:
            handle.write(new_content)
        print(f"HTML file successfully generated: {output_path}")
    except FileNotFoundError:
        print(f"Error: The file '{template_path}' was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    animal_data = load_data("animals_data.json")
    if not animal_data:
        return
    skin_types = get_skin_types(animal_data)
    print("Available skin types:", skin_types)
    animals_info = generate_animals_info(animal_data)

    generate_html("animals_template.html", "animals.html", animals_info)


if __name__ == "__main__":
    main()