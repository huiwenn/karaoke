import os
import tqdm

files = os.listdir("./lyrics/samples")

for f in files:
	if f[-3:] != "txt":
		continue

	song_name = f[:-4]

	os.makedirs("./lyrics/{}".format(song_name), exist_ok=True)
	ct = 0

	with open("./lyrics/samples/{}".format(f), 'r') as lyr:
		lines = lyr.readlines()
	
	for i in range(int(len(lines)/10)):
		pth = "./lyrics/tmp/{}_{}".format(song_name, i)
		print(pth)
		with open(pth, 'w') as writefile:
			if 10*(i+1) >= len(lines):
				writefile.write(''.join(lines[i*10:]))
			else:
				writefile.write(''.join(lines[i*10:(i+1)*10]))

		with open('./vis/AttnGAN/data/coco/example_filenames.txt', 'w') as f:
			f.write('../../.{}}'.format(pth))

		os.chdir('vis/AttnGAN/code')
		os.system("python2 main.py --cfg cfg/eval_coco.yml --gpu 0")
		os.chdir("../../..")



