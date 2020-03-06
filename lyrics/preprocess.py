import os

files = os.listdir("./lyrics/samples")


with open('./vis/AttnGAN/data/coco/example_filenames.txt', 'w') as f:
	for file in files:
		if file[-3:] == "txt":
			f.write('../../../lyrics/samples/{}\n'.format(file[:-3]))


