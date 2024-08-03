import os
import sys


from gif.main import main as gif_main
from static.main import main as static_main
from sfx.main import main as sfx_main


sys.path.append(os.path.join(os.path.dirname(__file__), 'gif'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'static'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'sfx'))


def main():
	# [info]   Missing asset: pokes/Duskull-front.gif
	# [info]   Missing asset: pokes/Duskull-back.gif
	# [info]   Missing asset: pokes-static/duskull.png
	# [info]   Missing asset: pokes/Shuppet-front.gif
	# [info]   Missing asset: pokes/Shuppet-back.gif
	# [info]   Missing asset: pokes-static/shuppet.png
	# [info]   Missing asset: pokes/Froslass-front.gif
	# [info]   Missing asset: pokes/Froslass-back.gif
	# [info]   Missing asset: pokes-static/froslass.png
	# [info]   Missing asset: pokes/Dusknoir-front.gif
	# [info]   Missing asset: pokes/Dusknoir-back.gif
	# [info]   Missing asset: pokes-static/dusknoir.png
	# [info]   Missing asset: pokes/Shedinja-front.gif
	# [info]   Missing asset: pokes/Shedinja-back.gif
	# [info]   Missing asset: pokes-static/shedinja.png
	# [info]   Missing asset: pokes/Gengar-front.gif
	# [info]   Missing asset: pokes/Gengar-back.gif
	# [info]   Missing asset: pokes-static/gengar.png
	pokemon_names = [
		'duskull',
		'shuppet',
		'froslass',
		'dusknoir',
		'shedinja',
		'gengar'
	]

	# [info]   Missing SFX: curse.mp3
	# [info]   Missing SFX: thunder-punch.mp3
	# [info]   Missing SFX: fire-punch.mp3
	# [info]   Missing SFX: confuse-ray.mp3
	# [info]   Missing SFX: lick.mp3
	# [info]   Missing SFX: shadow-ball.mp3
	move_names = [
		"Curse",
		"Thunder Punch",
		"Fire Punch",
		"Confuse Ray",
		"Lick",
		"Shadow Ball"
	]

	print("<<GIF>>>.")
	gif_main(pokemon_names)

	print("<<<STATIC>>>")
	static_main(pokemon_names)

	print("<<<SFX>>>")
	sfx_main(move_names)


if __name__ == "__main__":
	main()
