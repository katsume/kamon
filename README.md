# kamon

## Requirements

- Docker

## Tree

```
.
├── Dropbox
│    └── _
│         └── kamon
│              ├── dst
│              │    └── book
│              │         └── pggan-tkarras
│              └── src
│                   └── book
│                        └── 2-png
│                             └── 260ppi-tfrecords
└── Projects
     └── kamon
          └── progressive_growing_of_gans
```

## Run

```
$ ./Projects/kamon/run.sh python3 ./Projects/kamon/progressive_growing_of_gans/train.py
```
