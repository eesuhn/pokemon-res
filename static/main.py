import os
import requests
from PIL import Image


BASE_URL_FRONT = "https://img.pokemondb.net/sprites/black-white/normal/{}.png"


def download_pokemon(name, output_folder):
	url = BASE_URL_FRONT.format(name)
	response = requests.get(url)
	if response.status_code == 200:
		file_path = os.path.join(output_folder, f"{name}.png")
		with open(file_path, 'wb') as file:
			file.write(response.content)
		print(f"Downloaded {name}.png")
		return file_path
	else:
		print(f"Failed to download {name}.png")
		return None


def resize_image(input_path, output_path, size=(96, 96)):
	with Image.open(input_path) as img:
		# Convert to RGBA if not already
		img = img.convert("RGBA")

		# Get the bounding box of non-transparent pixels
		bbox = img.getbbox()

		if bbox:
			# Crop the image to remove transparent padding
			img = img.crop(bbox)

			# Calculate the scaling factor
			width, height = img.size
			scale = min(size[0] / width, size[1] / height)

			# Calculate new dimensions
			new_width = int(width * scale)
			new_height = int(height * scale)

			# Resize the image using nearest neighbor to maintain pixel art quality
			img = img.resize((new_width, new_height), Image.NEAREST)

			# Create a new image with the desired size and paste the resized image
			new_img = Image.new("RGBA", size, (0, 0, 0, 0))
			paste_x = (size[0] - new_width) // 2
			paste_y = (size[1] - new_height) // 2
			new_img.paste(img, (paste_x, paste_y))

			# Save the result
			new_img.save(output_path, "PNG")
			print(f"Resized and saved {output_path}")
		else:
			print(f"Image {input_path} is empty or fully transparent")


def main(pokemon_names):
	output_folder = 'static/raw'
	resized_folder = 'static/output'

	for name in pokemon_names:
		file_path = download_pokemon(name, output_folder)
		if file_path:
			resized_path = os.path.join(resized_folder, f"{name}.png")
			resize_image(file_path, resized_path)


if __name__ == "__main__":
	default_pokemon_names = [
		'blaziken',
		'breloom'
	]
	main(default_pokemon_names)
