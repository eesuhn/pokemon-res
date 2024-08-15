import os
import requests
import subprocess
from bs4 import BeautifulSoup


INPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'raw'))
OUTPUT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), 'out'))


BASE_URL = "https://downloads.khinsider.com/game-soundtracks/album/pokemon-sfx-gen-5-attack-moves-blk-wht-blk2-wht2/"
VOLUME = +1


def download_link(move: str) -> str:
	url = BASE_URL + move.replace(' ', '%20') + '.mp3'
	response = requests.get(url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'html.parser')
		download_link = soup.find('audio', id='audio')['src']
		return download_link
	else:
		print(f"Failed fetch {move} from {url}")
		return None


def download(move: str) -> None:
	link = download_link(move)
	if link:
		response = requests.get(link)
		if response.status_code == 200:
			filename = os.path.join(INPUT_PATH, move + '.mp3')
			with open(filename, 'wb') as file:
				file.write(response.content)
		else:
			print(f"Failed download {move} from {link}")
	else:
		print(f"No download link for {move}")


def compress(move: str) -> None:
	input_file = os.path.join(INPUT_PATH, move + '.mp3')
	output_file = os.path.join(OUTPUT_PATH, move.lower().replace(' ', '-') + '.mp3')
	subprocess.run([
		'ffmpeg',
		'-i', input_file,
		'-vn',
		'-af', f'volume={VOLUME}dB',
		"-acodec", "libmp3lame",
		"-b:a", "128k",
		'-y', output_file
	])
	print(f"Compressed {move}")


def main(moves: list[str]) -> None:
	for move in moves:
		download(move)
		compress(move)


if __name__ == '__main__':
	default_moves = [
		'Ember',
		'Vine Whip',
		'Water Gun',
	]
	main(default_moves)
