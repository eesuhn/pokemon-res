from PIL import Image


DIM = (784, 784)
POS = (56, 56)


def main():
	types = [
		# 'normal',
		# 'fire',
		# 'water',
		# 'electric',
		# 'grass',
		# 'ice',
		# 'fighting',
		# 'poison',
		'psychic',
		# 'bug',
		# 'rock'
	]

	for t in types:
		current = crop(f'./raw/{t}_type.png')
		current.save(f'./output/{t}-type.png')


def crop(imageName):
	img = Image.open(imageName)
	return img.crop((POS[0], POS[1], POS[0] + DIM[0], POS[1] + DIM[1]))


if __name__ == '__main__':
	main()
