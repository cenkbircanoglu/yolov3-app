#!/usr/bin/env bash

nvidia-docker run -d --rm -it --name cenkbircanoglu/yolo34py-gpu:latest -p 80:5000 yolo34py-gpu
