import subprocess


def crop_gif(input_path, output_path, crop_width, crop_height, crop_x, crop_y):
	command = [
		'ffmpeg',
		'-i', input_path,
		'-filter_complex', f'crop={crop_width}:{crop_height}:{crop_x}:{crop_y},split[s0][s1];[s0]palettegen=max_colors=256:reserve_transparent=on:transparency_color=ffffff[p];[s1][p]paletteuse',
		'-y',
		output_path
	]
	try:
		result = subprocess.run(command, check=True, capture_output=True, text=True)
		print(f"Successfully cropped {input_path} to {output_path}")
		return True
	except subprocess.CalledProcessError as e:
		print(f"FFmpeg command failed: {e}")
		print(f"FFmpeg errors: {e.stderr}")
		return False


input_file = 'raw/battle-bg.gif'
output_file = 'output/cropped_battle-bg.gif'
crop_width = 960
crop_height = 460
crop_x = 0
crop_y = 40

success = crop_gif(input_file, output_file, crop_width, crop_height, crop_x, crop_y)

if success:
	print("GIF cropping completed successfully.")
else:
	print("GIF cropping failed.")
