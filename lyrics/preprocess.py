import os

files = os.listdir("./lyrics/samples")

for f in files:
	if file[-3:] != "txt":
		continue

	song_name = file[:-4]

	# first: make small batches
	os.mkdir("./lyrics/{}".format(song_name))
	ct = 0

	with open("./lyrics/samples/{}".format(f), 'r'):
		lines = f.readlines()
	
	fnames = []

	for i in range(len(lines)/10):
		pth = "./lyrics/tmp/{}_{}".format((song_name, i))
		with open(pth, 'w') as writefile:
			writefile.write(''.join(lines[i*10:(i+1)*10]))

		with open('./vis/AttnGAN/data/coco/example_filenames.txt', 'w') as f:
			f.write('../../.{}}'.format(pth))

		os.chdir('vis/AttnGAN/code')
		os.system("python2 main.py --cfg cfg/eval_coco.yml --gpu 0")
		os.chdir("../../..")



