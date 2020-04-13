#!/usr/bin/env python3

import os
import argparse
import time

from PIL import Image, ImageDraw

if __name__=='__main__':

    parser= argparse.ArgumentParser()
    parser.add_argument('src_file', type=str, default='')
    parser.add_argument('dst_path', type=str, default=os.getcwd())
    parser.add_argument('--test', action='store_true')
    parser.add_argument('--origin', nargs=2, type=float)
    parser.add_argument('--size', nargs=2, type=float)
    parser.add_argument('--padding', nargs=2, type=float)
    parser.add_argument('--shape', nargs=2, type=int)
    args= parser.parse_args()

    (dir, basename)= os.path.split(args.src_file)
    (root, ext)= os.path.splitext(basename)
    img= Image.open(args.src_file)

    ox= args.origin[0]
    oy= args.origin[1]

    w= args.size[0]
    h= args.size[1]

    px= args.padding[0]
    py= args.padding[1]

    row= args.shape[0]
    col= args.shape[1]

    if args.test:

        rect_img= Image.new('RGBA', img.size, (0, 0, 0, 0))
        ctx= ImageDraw.Draw(rect_img)

        for i in range(args.shape[1]):
            for j in range(args.shape[0]):
                x= ox+(w+px)*j
                y= oy+(h+py)*i
                ctx.rectangle([int(x), int(y), int(x+w), int(y+h)], fill=(255, 0, 0, 64))

        test_img= img.convert('RGBA')
        test_img.alpha_composite(rect_img)
        test_img.save(os.path.join(args.dst_path, f'{root}-test-{time.time()}{ext}'))

    else:

        if not os.path.exists(args.dst_path):
            os.mkdir(args.dst_path)

        for i in range(col):
            for j in range(row):
                x= ox+(w+px)*j
                y= oy+(h+py)*i
                crop_img= img.crop((int(x), int(y), int(x+w), int(y+h)))
                crop_img.save(os.path.join(args.dst_path, f'{root}-{(i*row+j)}{ext}'))
