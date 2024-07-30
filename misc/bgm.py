import subprocess


def main():
	wav_file = "battle-theme.wav"

	subprocess.run([
		"ffmpeg",
		"-i", wav_file,
		"-af", "volume=-4dB",
		"-acodec", "pcm_s16le",
		"-ar", "44100",
		"-y",
		"reduced-" + wav_file
	])


if __name__ == "__main__":
	main()
