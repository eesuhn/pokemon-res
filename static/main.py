import os
import requests
from PIL import Image
from concurrent.futures import ThreadPoolExecutor, as_completed


BASE_URL_FRONT = "https://img.pokemondb.net/sprites/black-white/anim/normal/{}.gif"


def download_gif(url, filename) -> bool:
	response = requests.get(url)
	if response.status_code == 200:
		with open(filename, 'wb') as f:
			f.write(response.content)
		return True
	return False


def process_gif(input_path, output_path) -> bool:
	try:
		with Image.open(input_path) as img:
			# Get the first frame of the GIF
			img.seek(0)
			# Convert to RGBA if it's not already
			img = img.convert('RGBA')
			# Calculate new size (1.5x)
			new_size = (int(img.width * 1.5), int(img.height * 1.5))
			# Resize using nearest neighbor resampling
			resized_img = img.resize(new_size, Image.NEAREST)
			# Save as PNG, overwriting if it exists
			resized_img.save(output_path, 'PNG')
		print(f"Processed {input_path} to {output_path}")
		return True
	except Exception as e:
		print(f"Image processing failed: {e}")
		return False


def process_pokemon(pokemon_name) -> None:
	pokemon_name_lower = pokemon_name.lower()
	url = BASE_URL_FRONT.format(pokemon_name_lower)

	raw_filename = os.path.join('raw', f'{pokemon_name}.gif')
	processed_filename = os.path.join('output', f'{pokemon_name}.png')

	if download_gif(url, raw_filename):
		print(f"Downloaded {pokemon_name}")
		if process_gif(raw_filename, processed_filename):
			print(f"Processed and saved as {pokemon_name}.png")
		else:
			print(f"Failed to process {pokemon_name}")
	else:
		print(f"Failed to download {pokemon_name}")


def process_pokemon_with_timeout(pokemon_name):
	try:
		process_pokemon(pokemon_name)
	except Exception as e:
		print(f"Error processing {pokemon_name}: {str(e)}")


def main():
	# Input list of Pokemon names
	pokemon_names = [
		'bulbasaur',
		'squirtle',
		'charmander',
		'snorlax',
	]

	# Adjust max_workers to control the number of threads
	with ThreadPoolExecutor(max_workers=3) as executor:
		future_to_pokemon = {executor.submit(process_pokemon_with_timeout, name): name for name in pokemon_names}
		for future in as_completed(future_to_pokemon):
			pokemon = future_to_pokemon[future]
			try:
				future.result()
			except Exception as e:
				print(f"{pokemon} generated an exception: {str(e)}")


if __name__ == "__main__":
	main()
