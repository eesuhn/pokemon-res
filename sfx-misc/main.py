import os
import ffmpeg


INPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'raw'))
OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'out'))


def adjust_volume(target_file: str, volume: int, file_extension: str) -> str:
	input_file = os.path.join(INPUT_PATH, target_file + file_extension)
	output_file = os.path.join(OUTPUT_PATH, target_file + '.mp3')

	stream = (
		ffmpeg
		.input(input_file)
		.filter('volume', volume=f'{volume}dB')
		.output(output_file, audio_bitrate='128k', acodec='libmp3lame')
		.overwrite_output()
	)
	ffmpeg.run(stream)
	return output_file


def main(sfx_with_volume: list[tuple[str, int, str]]):
	for item in sfx_with_volume:
		if len(item) == 3:
			target_file, volume, file_extension = item
		elif len(item) == 2:
			target_file, volume = item
			file_extension = '.mp3'
		else:
			print(f"Invalid item: {item}")

		adjust_volume(target_file, volume, file_extension)
		print(f"Compressed {target_file}")


if __name__ == '__main__':
	sfx_with_volume = [
		('button-a', -1),
		('ending-theme', -5),
		('battle-theme', -8, '.wav'),
		('stat-fell', -4),
		('stat-rose', -4),
	]
	main(sfx_with_volume)
