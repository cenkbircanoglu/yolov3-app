#!/usr/bin/env bash

# Build the docker image
docker build -t yolo3-4-py .

# Run the docker image
docker run --rm -it --name yolo3-4-py -p 80:5000 yolo3-4-py