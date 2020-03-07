import os
import tqdm

os.makedirs("./lyrics/tmp", exist_ok=True)
files = os.listdir("./lyrics/samples")

for f in files:
	if f[-3:] != "txt":
		continue

	song_name = f[:-4]
	os.makedirs("./vis/img/{}".format(song_name), exist_ok=True)

	with open("./lyrics/samples/{}".format(f), 'r') as lyr:
		lines = lyr.readlines()
	
	for i in range(int(len(lines)/10)):
		dir_name = "{}_{}".format(song_name, i)
		pth = "./lyrics/tmp/{}.txt".format(dir_name)
		print(pth)
		with open(pth, 'w') as writefile:
			if 10*(i+1) >= len(lines):
				writefile.write(''.join(lines[i*10:]))
			else:
				writefile.write(''.join(lines[i*10:(i+1)*10]))

		with open('./vis/AttnGAN/data/coco/example_filenames.txt', 'w') as f:
			f.write('../../.{}'.format(pth[:-4]))

		os.chdir('vis/AttnGAN/code')
		os.system("python2 main.py --cfg cfg/eval_coco.yml --gpu 0")
		os.chdir("../../..")

		imgs = os.listdir("./vis/AttnGAN/models/coco_AttnGAN2/{}".format(dir_name))
		for img in imgs:
			if img[-5] == '2': #big image!
				os.system("mv vis/AttnGAN/models/coco_AttnGAN2/{}/{} vis/img/{}"
					.format(dir_name, img, song_name))