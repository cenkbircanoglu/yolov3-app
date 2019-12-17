FROM ubuntu:16.04

## Pyton installation ##
RUN apt-get update && apt-get install -y python3.5 python3-pip git

## OpenCV 3.4 Installation ##
RUN apt-get install -y build-essential cmake
RUN apt-get install -y qt5-default libvtk6-dev
RUN apt-get install -y zlib1g-dev libjpeg-dev libwebp-dev libpng-dev libtiff5-dev libjasper-dev libopenexr-dev libgdal-dev
RUN apt-get install -y libdc1394-22-dev libavcodec-dev libavformat-dev libswscale-dev libtheora-dev libvorbis-dev libxvidcore-dev libx264-dev yasm libopencore-amrnb-dev libopencore-amrwb-dev libv4l-dev libxine2-dev
RUN apt-get install -y python-dev python-tk python-numpy python3-dev python3-tk python3-numpy
RUN apt-get install -y unzip wget
RUN wget https://github.com/opencv/opencv/archive/3.4.0.zip
RUN unzip 3.4.0.zip
RUN rm 3.4.0.zip
WORKDIR /opencv-3.4.0
RUN mkdir build
WORKDIR /opencv-3.4.0/build
RUN cmake -DBUILD_EXAMPLES=OFF ..
RUN make -j4
RUN make install
RUN ldconfig

## Downloading and compiling darknet ##
WORKDIR /
RUN apt-get install -y git
RUN git clone https://github.com/pjreddie/darknet.git
WORKDIR /darknet
# Set OpenCV makefile flag
RUN sed -i '/OPENCV=0/c\OPENCV=1' Makefile
RUN make
ENV DARKNET_HOME /darknet
ENV LD_LIBRARY_PATH /darknet
RUN pip3 install --upgrade pip
RUN pip3 install pkgconfig cython numpy gunicorn flask flask_cors

## Download and compile yolo3-4-py ##
WORKDIR /
ADD . /yolo3-4-py
WORKDIR /yolo3-4-py
RUN pip3 install pkgconfig
RUN pip3 install cython
RUN python3 setup.py build_ext --inplace

## Run test ##
RUN sh download_models.sh
CMD ["gunicorn", "-w", "3", "-b", "0.0.0.0:5000", "app:app"]