import argparse
import os
from pathlib import Path

# given a text file listing sequences (strings) of arbitrary length, split each sequence into every possible 9-character substring and output each sequences's results into a unique text file

parser = argparse.ArgumentParser(description='Splits sequences in a text file into 9-character substrings and outputs to files')
parser.add_argument('input_file', type=str, help='Input text file containing sequences')
parser.add_argument('output_dir', type=str, help='Location for output text files; will be created if not exists')

args = parser.parse_args()
SUBSTRING_LENGTH = 9

Path(args.output_dir).mkdir(parents=True, exist_ok=True)

with open(args.input_file, 'r') as f:
    for line in f:
        sequence = line.rstrip()
        i = 0
        output_filename = sequence
        with open(os.path.join(args.output_dir, output_filename+'.txt'), 'w') as o:
            while i+SUBSTRING_LENGTH <= len(sequence):
                o.write(sequence[i:i+SUBSTRING_LENGTH] + '\n')
                i+=1