import sys
from PIL import Image


SRC = "raw/dialog.png"  # 960 * 210
WIDTH = 380
HEIGHT = 210
HEIGHT_REDUCED = 180


def main():
	result = combine_cropped(crop_front(), crop_middle(), crop_back())
	result = result.resize((WIDTH, HEIGHT_REDUCED), resample=Image.NEAREST)
	result.save("output/battle-dialog-right.png")


def crop_front():
	x = 0
	y = 0
	width = 100
	height = HEIGHT
	crop_pos = (x, y, x + width, y + height)
	opened = Image.open(SRC)
	cropped = opened.crop(crop_pos)
	return cropped


def crop_back():
	x = 860
	y = 0
	width = 100
	height = HEIGHT
	crop_pos = (x, y, x + width, y + height)
	opened = Image.open(SRC)
	cropped = opened.crop(crop_pos)
	# Reduce the width to 80
	resized = cropped.resize((80, HEIGHT), resample=Image.NEAREST)
	return resized


def crop_middle():
	x = 100
	y = 0
	width = WIDTH - 200 + 20
	height = HEIGHT
	crop_pos = (x, y, x + width, y + height)
	opened = Image.open(SRC)
	cropped = opened.crop(crop_pos)
	return cropped


def combine_cropped(front, middle, back):
	combined = Image.new("RGB", (WIDTH, HEIGHT))
	combined.paste(front, (0, 0))
	combined.paste(middle, (100, 0))
	combined.paste(back, ((WIDTH - 80), 0))
	return combined


if __name__ == "__main__":
	main()
