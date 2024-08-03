import os
import sys


sys.path.append(os.path.join(os.path.dirname(__file__), 'gif'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'static'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'sfx'))


from gif.main import main as gif_main
from static.main import main as static_main
from sfx.main import main as sfx_main


def main():
	pokemon_names = [
		'gengar'
	]

	move_names = [
		"Dream Eater"
	]

	# Run the gif process
	print("Running GIF process...")
	gif_main(pokemon_names)

	# Run the static process
	print("Running static image process...")
	static_main(pokemon_names)

	# Run the sfx process
	print("Running SFX process...")
	sfx_main(move_names)


if __name__ == "__main__":
	main()
