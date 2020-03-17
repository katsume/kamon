#!/usr/bin/env python3

import os
import glob
import argparse

from PIL import Image

if __name__=='__main__':

    parser= argparse.ArgumentParser()
    parser.add_argument('--mode', type=str, default='RGB', help='See https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes')
    parser.add_argument('src', type=str)
    parser.add_argument('dst', type=str)
    args= parser.parse_args()

    if not os.path.exists(args.dst):
        os.mkdir(args.dst)

    files= glob.glob(os.path.join(args.src, '*'));
    for file in files:

        dir, name= os.path.split(file)
        base, ext = os.path.splitext(name)
        if not ext in ['.jpg', '.png', '.gif']:
            continue

        img = Image.open(file).convert(args.mode)
        img.save(os.path.join(args.dst, name));

        print(name);
