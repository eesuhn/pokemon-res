import requests
from bs4 import BeautifulSoup
import subprocess


VOLUME = +4


def get_download_link(move_name):
	base_url = "https://downloads.khinsider.com/game-soundtracks/album/pokemon-sfx-gen-5-attack-moves-blk-wht-blk2-wht2/"
	page_url = base_url + move_name.replace(' ', '%20') + ".mp3"

	response = requests.get(page_url)
	if response.status_code == 200:
		soup = BeautifulSoup(response.content, 'html.parser')
		download_link = soup.find('audio', id='audio')['src']
		return download_link
	else:
		print(f"Failed to fetch page for: {move_name}")
		return None


def download_mp3(move_name):
	download_link = get_download_link(move_name)
	if download_link:
		response = requests.get(download_link)
		if response.status_code == 200:
			filename = f"{move_name}.mp3"
			with open(f"raw/{filename}", "wb") as f:
				f.write(response.content)
			print(f"Downloaded: {filename}")
		else:
			print(f"Failed to download: {move_name}")
	else:
		print(f"Couldn't find download link for: {move_name}")


def convert_to_wav_and_rename(move_name):
	mp3_file = f"raw/{move_name}.mp3"
	wav_file = f"reduced/{move_name.lower().replace(' ', '-')}.wav"

	subprocess.run([
		"ffmpeg",
		"-i", mp3_file,
		"-af", "volume=" + str(VOLUME) + "dB",
		"-acodec", "pcm_s16le",
		"-ar", "44100",
		"-y",
		wav_file
	])
	print(f"OUTPUT: {wav_file}")


def main():
	moveList = [
		"Vine Whip",
		"Water Gun",
		"Ember"
	]

	for move in moveList:
		download_mp3(move)
		convert_to_wav_and_rename(move)


if __name__ == '__main__':
	main()
