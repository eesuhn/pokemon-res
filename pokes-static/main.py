import os
import requests
from PIL import Image


INPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'raw'))
OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'out'))

BASE_URL = "https://img.pokemondb.net/sprites/black-white/normal/{}.png"
SIZE = (96, 96)


def download(name: str) -> bool:
	url = BASE_URL.format(name)
	response = requests.get(url)
	if response.status_code == 200:
		with open(os.path.join(INPUT_PATH, f"{name}.png"), 'wb') as file:
			file.write(response.content)
		return True
	print(f"Failed to download {name}")
	return False


def resize(input_path: str, output_path: str) -> bool:
	with Image.open(input_path) as image:
		image = image.convert('RGBA')
		bbox = image.getbbox()

		if bbox is None:
			print(f"Image {input_path} is empty")
			return False

		image = image.crop(bbox)
		width, height = image.size
		scale = min(SIZE[0] / width, SIZE[1] / height)
		new_size = (int(width * scale), int(height * scale))

		image = image.resize(new_size, Image.NEAREST)
		new_image = Image.new('RGBA', SIZE, (0, 0, 0, 0))
		new_image.paste(image, ((SIZE[0] - new_size[0]) // 2, (SIZE[1] - new_size[1]) // 2))

		new_image.save(output_path, 'PNG')
		return True


def main(pokemons: list[str]) -> None:
	for pokemon in pokemons:
		raw_file = os.path.join(INPUT_PATH, f"{pokemon}.png")
		output_file = os.path.join(OUTPUT_PATH, f"{pokemon}.png")

		if (download(pokemon) and resize(raw_file, output_file)):
			print(f"Processed {pokemon}")


if __name__ == '__main__':
	default_pokemons = [
		'charmander',
		'bulbasaur',
		'squirtle',
	]
	main(default_pokemons)
