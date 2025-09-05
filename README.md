# Mini project hand gesture over UDP

## Description
RPI run gstreamer and send over UDP to host (using mac). Mediapipe is used to detect hand gesture (thumbs up, open palm).

## Prerequisite
### Install GStreamer
1. For both RPI and macOS (not covered)
### OpenCV Build Instructions
By default, gstreamer is not enabled in OpenCV, so need to build from source. Gstreamer must be already installed before building OpenCV.

Clone the required repositories:
```sh
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
```

Build OpenCV with CMake:
```sh
cd opencv
mkdir build && cd build

cmake -D CMAKE_BUILD_TYPE=Release \
  -D CMAKE_INSTALL_PREFIX=$VIRTUAL_ENV \
  -D PYTHON3_EXECUTABLE=$(which python3) \
  -D PYTHON3_INCLUDE_DIR=$(python3 -c "import sysconfig; print(sysconfig.get_path('include'))") \
  -D PYTHON3_LIBRARY=$(python3 -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))") \
  -D PYTHON3_PACKAGES_PATH=$(python3 -c "import site; print(site.getsitepackages()[0])") \
  -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
  -D WITH_GSTREAMER=ON \
  ..
```

## Demo
### Instructions
1. Run from Raspberry Pi 4
    ```sh
    gst-launch-1.0 libcameras ! videoconvert ! videoscale ! video/x-raw, width=640, height=480, framerate=30/1 ! x264enc! rtph264pay ! udpsink host=192.168.x.x port=5000 sync=false
    ```
    Note that the quality of video including size and framerate need to be used, otherwise it may not work.
2. Run ```app_udp_hand.py``` from host

### Video
```app_udp_hand.mov```

### Keyword
![Raspberry Pi](https://img.shields.io/badge/-RaspberryPi-C51A4A?logo=raspberrypi&logoColor=white)
![OpenCV](https://img.shields.io/badge/-OpenCV-27338e?logo=opencv&logoColor=white)
![GStreamer](https://img.shields.io/badge/-GStreamer-009639?logo=gstreamer&logoColor=white)
![UDP](https://img.shields.io/badge/-UDP-blue)
![MediaPipe](https://img.shields.io/badge/-MediaPipe-orange)
![RealTime](https://img.shields.io/badge/-RealTime-red)
![GestureRecognition](https://img.shields.io/badge/-GestureRecognition-yellow)
