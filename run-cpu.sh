#!/usr/bin/env bash

# Run the docker image
docker run --rm -it --name cenkbircanoglu/yolo34-py:latest -p 80:5000 yolo34-py