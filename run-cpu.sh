#!/usr/bin/env bash

# Run the docker image
docker run --rm -it --name yolo34-py -p 80:5000 -v /Users/cenk.bircanoglu/wsl/wsl_survey/data/compcars/data/image:/image yolo34-py