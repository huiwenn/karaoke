# karaoke
🎵

## Run the lyrics generator
Currently the fine-tuned model lives in BMO. (TODO: make it a service???) Run the following command in the `\lyrics` directory.

`python inference.py new_titles.txt`
`python postprocess.py`

The result can then betrimmed by the ~ artists ~. 

## Image generation

we use [attnGAN](https://arxiv.org/pdf/1711.10485.pdf) and did something similar to what goodkids did [here](https://neurips2019creativity.github.io/doc/Text%20Conditional%20Lyric%20Video%20Generation.pdf). 

The downloaded model also lives in BMO. Commands:

(in karaoke root directory)

`python lyrics/generate_images.py`

or for a specific song:
`python lyrics/generate_images.py --song "hack the fuck out of it"`


## Midi generation

due to the limited time & compute resource, we are using [musegan](https://github.com/salu133445/musegan) to generate little pop song bits. (maybe imigrate to magenta's transformer in the future.)


## Conda enviornment
For versioning consistency, this repo is designed to be run in a conda env.
After cloning, create the env by running:

`conda env create -f env-ubuntu.yml`

With the right yml file for the operating system. and then

`conda activate karaoke`

If you installed something, remember to update the yml file by running:

`conda env export > env-os.yml`

replace "os" with the os you are working in. 
