import os
import requests
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed


INPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'raw'))
OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'out'))

BASE_URL_FRONT = "https://img.pokemondb.net/sprites/black-white/anim/normal/{}.gif"
BASE_URL_BACK = "https://img.pokemondb.net/sprites/black-white/anim/back-normal/{}.gif"


def download(url: str, filename: str) -> bool:
	response = requests.get(url)
	if response.status_code == 200:
		with open(filename, 'wb') as file:
			file.write(response.content)
		return True
	print(f"Failed to download {url}")
	return False


def resize(input_path: str, output_path: str) -> bool:
	command = [
		'ffmpeg',
		'-i', input_path,
		'-filter_complex',
		'fps=20,scale=iw*2.5:ih*2.5:flags=neighbor,split[s0][s1];[s0]palettegen=max_colors=256:reserve_transparent=on:transparency_color=ffffff[p];[s1][p]paletteuse',
		'-y', output_path
	]
	try:
		subprocess.run(command, check=True, capture_output=True, text=True)
		return True
	except subprocess.CalledProcessError as e:
		print(f"Failed to resize {output_path}")
		print(f"FFmpeg error: {e}\n{e.stderr}")
		return False


def process(pokemon: str) -> None:
	for view in ['front', 'back']:
		if view == 'front':
			url = BASE_URL_FRONT.format(pokemon.lower())
		else:
			url = BASE_URL_BACK.format(pokemon.lower())

		raw_file = os.path.join(INPUT_PATH, f"{pokemon.lower()}-{view}.gif")
		output_name = f"{pokemon.capitalize()}-{view}"
		output_file = os.path.join(OUTPUT_PATH, f"{output_name}.gif")

		if (download(url, raw_file) and resize(raw_file, output_file)):
			print(f"Processed {output_name}")


def main(pokemons: list[str]) -> None:
	with ThreadPoolExecutor(max_workers=2) as executor:
		future_to_pokemon = {executor.submit(process, pokemon): pokemon for pokemon in pokemons}
		for future in as_completed(future_to_pokemon, timeout=60):
			pokemon = future_to_pokemon[future]
			try:
				future.result()
			except Exception as e:
				print(f"Failed to process {pokemon}: {str(e)}")


if __name__ == '__main__':
	default_pokemons = [
		'charmander',
		'bulbasaur',
		'squirtle',
	]
	main(default_pokemons)
