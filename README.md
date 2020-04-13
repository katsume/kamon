# kamon

## v2

### Requirements

- Docker
- [tkarras/progressive_growing_of_gans: Progressive Growing of GANs for Improved Quality, Stability, and Variation](https://github.com/tkarras/progressive_growing_of_gans)

### Tree

```
.
└── Projects
    ├── kamon
    └── progressive_growing_of_gans
```

### Run

```
$ ./Projects/kamon/run.sh python3 ./Projects/progressive_growing_of_gans/train.py
```

## v1

### Crop parmeters

```
./crop.py ../_src/kamon/1-retouched/kamon012190704.png ../_src/kamon/2-cropped/1 --origin 11 8 --size 100 100 --padding 16 36.75 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon022190703.png ../_src/kamon/2-cropped/2 --origin 12 10 --size 100 100 --padding 17.5 38.75 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon032190704.png ../_src/kamon/2-cropped/3 --origin 12 10 --size 100 100 --padding 18.7 39.8 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon042190704.png ../_src/kamon/2-cropped/4 --origin 13 10 --size 100 100 --padding 18.55 38.9 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon052190704.png ../_src/kamon/2-cropped/5 --origin 13 9 --size 100 100 --padding 18.55 38.9 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon062190704.png ../_src/kamon/2-cropped/6 --origin 11 10 --size 100 100 --padding 18 38.9 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon072190704.png ../_src/kamon/2-cropped/7 --origin 11 10 --size 100 100 --padding 19 38.9 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon082190704.png ../_src/kamon/2-cropped/8 --origin 11 10 --size 100 100 --padding 19 38.9 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon092190704.png ../_src/kamon/2-cropped/9 --origin 13 10 --size 100 100 --padding 19 38.9 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon102190704.png ../_src/kamon/2-cropped/10 --origin 14 10 --size 100 100 --padding 20.3 39 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon111100704.png ../_src/kamon/2-cropped/11 --origin 12 10 --size 100 100 --padding 19.2 38.6 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon122190704.png ../_src/kamon/2-cropped/12 --origin 12 11 --size 100 100 --padding 17.8 41 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon132190704.png ../_src/kamon/2-cropped/13 --origin 12 10 --size 100 100 --padding 18.9 38.8 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon142100704.png ../_src/kamon/2-cropped/14 --origin 12 10 --size 100 100 --padding 17.2 38.9 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon152190704.png ../_src/kamon/2-cropped/15 --origin 13 10 --size 100 100 --padding 18.9 38.8 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon162190704.png ../_src/kamon/2-cropped/16 --origin 11 10 --size 100 100 --padding 18.5 38.85 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon172190704.png ../_src/kamon/2-cropped/17 --origin 11 10 --size 100 100 --padding 18.1 39 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon182190704.png ../_src/kamon/2-cropped/18 --origin 11 10 --size 100 100 --padding 18.1 39 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon192190704.png ../_src/kamon/2-cropped/19 --origin 11 9 --size 100 100 --padding 18.1 38.9 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon202190704.png ../_src/kamon/2-cropped/20 --origin 11 10 --size 100 100 --padding 18.6 38.9 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon212190704.png ../_src/kamon/2-cropped/21 --origin 11 10 --size 100 100 --padding 17.9 38.8 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon222190704.png ../_src/kamon/2-cropped/22 --origin 11 10 --size 100 100 --padding 17.6 38.8 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon232190704.png ../_src/kamon/2-cropped/23 --origin 11 10 --size 100 100 --padding 17.9 38.8 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon242190704.png ../_src/kamon/2-cropped/24 --origin 9 10 --size 100 100 --padding 16.3 38.8 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon252190704.png ../_src/kamon/2-cropped/25 --origin 11 10 --size 100 100 --padding 18.5 38.8 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon262190704.png ../_src/kamon/2-cropped/26 --origin 11 11 --size 100 100 --padding 17.8 38.8 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon272190704.png ../_src/kamon/2-cropped/27 --origin 12 11 --size 100 100 --padding 19 38.9 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon282190704.png ../_src/kamon/2-cropped/28 --origin 12 10 --size 100 100 --padding 17.6 38.7 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon292190704.png ../_src/kamon/2-cropped/29 --origin 12 11 --size 100 100 --padding 17.6 38.7 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon302190704.png ../_src/kamon/2-cropped/30 --origin 12 10 --size 100 100 --padding 19.6 38.5 --shape 10 12
./crop.py ../_src/kamon/1-retouched/kamon312190704.png ../_src/kamon/2-cropped/31 --origin 10 10 --size 100 100 --padding 17.4 38.7 --shape 10 12
```
