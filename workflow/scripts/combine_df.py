#!/usr/bin/env python

import pandas as pd
import argparse
import os

#initialize argparse argument
parser = argparse.ArgumentParser()

#Add input and output arguments
parser.add_argument('-i', '--input', help='A  list of output file names from VERSE', dest='input', required=True, nargs='+')
parser.add_argument('-o', '--output', help='Output file name and path', dest='output', required=True)

args = parser.parse_args()

#Concat the input
concat = pd.concat([pd.read_csv(df, sep='\t', header=0, names = ['gene', '{}'.format(os.path.basename(df.split('.')[0]))], index_col='gene') for df in args.input], axis=1)

#Output as a csv
concat.to_csv(args.output)