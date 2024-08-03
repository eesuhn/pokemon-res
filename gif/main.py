import os
import requests
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


BASE_URL_FRONT = "https://img.pokemondb.net/sprites/black-white/anim/normal/{}.gif"
BASE_URL_BACK = "https://img.pokemondb.net/sprites/black-white/anim/back-normal/{}.gif"


def download_gif(url, filename) -> bool:
	response = requests.get(url)
	if response.status_code == 200:
		with open(filename, 'wb') as f:
			f.write(response.content)
		return True
	return False


def resize_gif(input_path, output_path) -> bool:
	command = [
		'ffmpeg',
		'-i', input_path,
		'-filter_complex', 'fps=20,scale=iw*2.5:ih*2.5:flags=neighbor,split[s0][s1];[s0]palettegen=max_colors=256:reserve_transparent=on:transparency_color=ffffff[p];[s1][p]paletteuse',
		'-y',
		output_path
	]
	try:
		subprocess.run(command, check=True, capture_output=True, text=True)
		print(f"Resized {input_path} to {output_path}")
		return True
	except subprocess.CalledProcessError as e:
		print(f"FFmpeg command failed: {e}")
		print(f"FFmpeg errors: {e.stderr}")
		return False


def process_pokemon(pokemon_name) -> None:
	pokemon_name_lower = pokemon_name.lower()

	for view in ['front', 'back']:
		if view == 'front':
			url = BASE_URL_FRONT.format(pokemon_name_lower)
		else:
			url = BASE_URL_BACK.format(pokemon_name_lower)

		output_name = f"{pokemon_name.capitalize()}-{view}"

		raw_filename = os.path.join('gif/raw', f'{pokemon_name_lower}-{view}.gif')
		resized_filename = os.path.join('gif/resized', f'{output_name}.gif')

		if os.path.exists(resized_filename):
			print(f"{output_name} already exists, skipping.")
			continue

		if download_gif(url, raw_filename):
			print(f"Downloaded {pokemon_name}-{view}")
			if resize_gif(raw_filename, resized_filename):
				print(f"Resized and saved as {output_name}")
			else:
				print(f"Failed to resize {pokemon_name}-{view}")
		else:
			print(f"Failed to download {pokemon_name}-{view}")


def process_pokemon_with_timeout(pokemon_name):
	try:
		start_time = time.time()
		process_pokemon(pokemon_name)
		end_time = time.time()
		print(f"Processed {pokemon_name} in {end_time - start_time:.2f} seconds")
	except Exception as e:
		print(f"Error processing {pokemon_name}: {str(e)}")


def main(pokemon_names):
	# Adjust max_workers to control the number of threads
	with ThreadPoolExecutor(max_workers=3) as executor:
		future_to_pokemon = {executor.submit(process_pokemon_with_timeout, name): name for name in pokemon_names}
		for future in as_completed(future_to_pokemon, timeout=10):  # Adjust timeout as needed
			pokemon = future_to_pokemon[future]
			try:
				future.result()
			except Exception as e:
				print(f"{pokemon} generated an exception: {str(e)}")


if __name__ == "__main__":
	default_pokemon_names = [
		'blaziken',
		'breloom'
	]
	main(default_pokemon_names)
