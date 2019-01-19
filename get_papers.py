


import argparse
import os


def parse_args():
    description = "filter knowledge"
    parser = argparse.ArgumentParser(description=description)
      
    parser.add_argument('--file')
    parser.add_argument('--output')
    args = parser.parse_args()
 
    return args


if __name__ == "__main__":
    args = parse_args()
    if not os.path.exists(args.output):
        os.makedirs(args.output)
    output = args.output

    for line in open(args.file):
        paper_name = line.strip()
        os.system('sopaper {} -d {}'.format(paper_name, output))

