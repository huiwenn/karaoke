import os, tqdm, argparse, random
import pretty_midi

bits = os.listdir("./music/data/bits")
files = os.listdir("./lyrics/samples")

bit_len = 9.6

all_lines = set([])

for f in files:
	if f[-3:] != "txt":
		continue
	with open("./lyrics/samples/{}".format(f), 'r') as lyr:
		lines = [l.strip() for l in lyr.readlines()]
		all_lines = all_lines.union(set([l for l in lines if len(l) > 0]))

indexs = random.sample(range(1000), len(all_lines))
matches = {}

for i, l in enumerate(list(all_lines)):
	matches[l] = "./music/data/bits/{}.mid".format('{:04d}'.format(indexs[i]))

for f in files:
	if f[-3:] != "txt":
		continue

	midis = []

	with open("./lyrics/samples/{}".format(f), 'r') as lyr:
		line = lyr.readline()
		while line:
			if len(line.strip()) != 0:
				midis.append(matches[line.strip()])
			line = lyr.readline()

	song_midi = pretty_midi.PrettyMIDI(midis[0])
	insts = song_midi.instruments

	for i, mid in enumerate(midis[1:]):
		midi = pretty_midi.PrettyMIDI(mid)
		
		for j, inst in enumerate(midi.instruments):

			new_notes = inst.notes
			for n in new_notes:
				n.start += (i+1) * bit_len
				n.end += (i+1) * bit_len
			
			insts[j].notes += new_notes

	file = pretty_midi.PrettyMIDI(initial_tempo=120, resolution=22050)
	file.instruments.extend(insts)
	endtime = file.get_end_time()
	print(endtime)
	eos = pretty_midi.TimeSignature(1, 1, endtime)
	file.time_signature_changes = [eos]

	out_fp = '{}.mid'.format(f[:-4])
	out_fp = os.path.join("./music/data/songs", out_fp)
	file.write(out_fp)





'''

os.makedirs("./lyrics/tmp", exist_ok=True)

parser = argparse.ArgumentParser(description='generate images')
parser.add_argument('--song', type=str, help='an integer for the accumulator')
args = parser.parse_args()

if args.song:
	files = [args.song+".txt"]
else:
	files = os.listdir("./lyrics/samples")

	#os.makedirs("./vis/img/{}".format(song_name), exist_ok=True)
	#counter = 0
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
'''