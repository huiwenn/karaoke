# karaoke
🎵

## Run the lyrics generator
Currently the fine-tuned model lives in BMO. (TODO: make it a service???) Run the following command in the `\lyrics` directory.

`python inference.py 'priming sentence' `

## Image generation

idea: we will use [attnGAN](https://arxiv.org/pdf/1711.10485.pdf) and maybe do something similar to what goodkids did [here](https://neurips2019creativity.github.io/doc/Text%20Conditional%20Lyric%20Video%20Generation.pdf). How doable is it in real time?

## Midi generation

## Conda enviornment
For versioning consistency, this repo is designed to be run in a conda env.
After cloning, create the env by running:

`conda env create -f env-ubuntu.yml`

With the right yml file for the operating system. and then

`conda activate karaoke`

If you installed something, remember to update the yml file by running:

`conda env export > env-os.yml`

replace "os" with the os you are working in. 
