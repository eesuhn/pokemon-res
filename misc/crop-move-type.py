from PIL import Image


SRC = "raw/physical_move.png"
POS = (90, 289)
WIDTH = 714
HEIGHT = 316


def main():
	cropped = crop()
	result = cropped
	result.save("output/physical-move.png")


def crop():
	opened = Image.open(SRC)
	cropped = opened.crop((POS[0], POS[1], POS[0] + WIDTH, POS[1] + HEIGHT))
	return cropped


if __name__ == "__main__":
	main()
