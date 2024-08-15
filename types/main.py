import os
from PIL import Image


INPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'raw'))
OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'out'))

DIMENSION = (784, 784)
POSITION = (56, 56)


def main(types: list[str]) -> None:
	for type in types:
		input_file = os.path.join(INPUT_PATH, type + '_type.png')
		output_file = os.path.join(OUTPUT_PATH, type + '-type.png')
		image = Image.open(input_file)
		image = image.crop((*POSITION, POSITION[0] + DIMENSION[0], POSITION[1] + DIMENSION[1]))
		image.save(output_file)
		print(f"Resized {type}")


if __name__ == '__main__':
	default_types = [
		'fire',
		'grass',
		'water',
	]
	main(default_types)
