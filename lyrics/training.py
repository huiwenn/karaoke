# text generation traing

import os as os
import pandas as pd
import gpt_2_simple as gpt2
import tensorflow as tf

# read dataset. 
# https://www.kaggle.com/mousehead/songlyrics loaded into 
def data():
    dfs = []
    link = ('https://raw.githubusercontent.com/ThomasVrancken/'
            'lyrics_generation/master/songdata_{}.csv')
    for i in range(4):
      dfs.append(pd.read_csv(link.format(i)))

    df = pd.concat(dfs).reset_index(drop=True)


    if not os.path.exists('data'):
        os.makedirs('data')
      
    pd.DataFrame({"lyrics": df['text']})\
        .to_csv(os.path.join('data', 'lyrics.csv'), index=False)

def model(model):
    gpt2.download_gpt2(model_name=model)   

def train(model):
    learning_rate = 0.0001
    optimizer = 'adam' 
    batch_size = 1
    model_name = model 
    sess = gpt2.start_tf_sess()

    gpt2.finetune(sess,
                  'data/lyrics.csv',
                  model_name=model_name,
                  sample_every=50,
                  save_every=50,
                  print_every=10,
                  learning_rate=learning_rate,
                  batch_size=batch_size,
                  restore_from='latest',
                  steps=500)   # max number of training steps

def generate():
    lst_results=gpt2.generate(
        sess,
        prefix="<|startoftext|>",
        nsamples=10,
        temperature=0.8, # change me
        top_p=0.9, # Change me
        return_as_list=True,
        truncate="<|endoftext|>",
        include_prefix=True
        )

    for res in lst_results:
        print(res)
        print('\n -------//------ \n')

def main(m='124M'):
    #data()
    model(m)
    train(m)
    generate()


if __name__ == '__main__':
    m = '124M' # should be among ["124M","355M","774M"]
    main(m)

