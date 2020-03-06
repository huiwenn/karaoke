import os


unwanted_char = [ '[', ']', '\"']

files = os.listdir("./samples")

for f in files:
	if f[-3:] != "txt":
		continue
	print(f)

	with open("./samples/"+f, 'r') as txt:
		alllines = []
		chunk = txt.readline()
		while chunk:
			processed = chunk.strip()
			for char in unwanted_char:
				processed = processed.replace(char, "")
			processed = [line for line in processed.split("\\n") if (len(line) > 0 and line!= "  ") ]
			print(processed)
			alllines += processed 
			alllines += ['\n']
			chunk = txt.readline()

		with open("./samples/processed/"+f, 'w') as p:
			p.write("\n".join(alllines))
