#!/bin/bash

BASE=tensorflow/tensorflow:1.6.0-gpu-py3
WORK_DIR=/tmp

DIR=$(cd $(dirname $0) && pwd)
NAME=$(whoami)/${DIR##*/}

# TF_FORCE_GPU_ALLOW_GROWTH=true
# https://qiita.com/ysuzuki19/items/b727bbcb45f1cad37630
# https://www.tensorflow.org/guide/gpu#limiting_gpu_memory_growth

docker build -t $NAME -<<- EOF
	FROM $BASE
	ENV TF_FORCE_GPU_ALLOW_GROWTH=true
	RUN apt-get update && apt-get install -y \
		ffmpeg \
		imagemagick \
		&& apt-get clean \
		&& rm -rf /var/lib/apt/lists/*
	RUN pip install moviepy
	RUN cat /dev/null > /etc/ImageMagick-6/policy.xml
	WORKDIR $WORK_DIR
	EOF
docker run -it --gpus all --rm -u ${UID}:${GID} -v $PWD:$WORK_DIR -w $WORK_DIR $NAME "$@"
