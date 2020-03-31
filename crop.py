#!/usr/bin/env python3

import os
import glob
import argparse
import time

from PIL import Image, ImageDraw

if __name__=='__main__':

    parser= argparse.ArgumentParser()
    parser.add_argument('src', type=str, default='')
    parser.add_argument('dst', type=str, default=os.getcwd())
    parser.add_argument('--size', nargs=2, type=int)
    args= parser.parse_args()

    if not os.path.exists(args.dst):
        os.mkdir(args.dst)

    files= glob.glob(os.path.join(args.src, '*'));
    for file in files:

        dir, name= os.path.split(file)
        base, ext = os.path.splitext(name)
        if not ext in ['.jpg', '.png', '.gif']:
            continue

        img = Image.open(file)
        crop_img= img.crop((0, 0, args.size[0], args.size[1]))
        crop_img.save(os.path.join(args.dst, name))

        print(name);
