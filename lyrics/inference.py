# inference

import gpt_2_simple as gpt2
import argparse


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str,
                       help='input prefix string for generation')
    args = parser.parse_args()

    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess)

    with open(args.file,'r') as f:
        prime = f.readline()
        print(prime)
        text = gpt2.generate(sess, prefix=args.prefix, return_as_list=True)
        print(" ".join(text))
