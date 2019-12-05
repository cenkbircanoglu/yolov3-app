#!/usr/bin/env bash
# Make output directory
mkdir output

docker build -t yolo34py-gpu -f Dockerfile-gpu .

nvidia-docker run --rm -it --name yolo34py-gpu -p 80:5000 yolo34py-gpu
