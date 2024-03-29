import os, tqdm
import argparse

os.makedirs("./lyrics/tmp", exist_ok=True)

parser = argparse.ArgumentParser(description='generate images')
parser.add_argument('--song', type=str, help='an integer for the accumulator')
args = parser.parse_args()

if args.song:
	files = [args.song+".txt"]
else:
	files = os.listdir("./lyrics/samples")

for f in files:
	if f[-3:] != "txt":
		continue

	song_name = "_".join(f[:-4].split(" "))
	os.makedirs("./vis/img/{}".format(song_name), exist_ok=True)

	counter = 0

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
				os.system("mv vis/AttnGAN/models/coco_AttnGAN2/{}/{} vis/img/{}/{}.png"
					.format(dir_name, img, song_name, counter))
				counter += 1