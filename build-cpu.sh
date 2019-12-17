#!/usr/bin/env bash

# Build the docker image
docker build -t yolo34-py .

# Run the docker image
docker run --rm -it --name yolo34-py -p 80:5000 yolo34-py