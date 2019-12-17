#!/usr/bin/env bash

nvidia-docker run -d --rm -it --name yolo34py-gpu -p 80:5000 cenkbircanoglu/yolo34py-gpu
