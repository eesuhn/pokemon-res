import ffmpeg

input_file = 'raw/a_button_trimmed.mp3'
output_file = 'output/button-a.mp3'

stream = (
	ffmpeg
	.input(input_file)
	.filter('volume', volume='-1dB')
	.output(output_file, audio_bitrate='128k', acodec='libmp3lame')
	.overwrite_output()
)

ffmpeg.run(stream)

print(f"Processed file saved as {output_file}")
