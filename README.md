# Mini project hand gesture over UDP

## Description
RPI run gstreamer and send over UDP to host (using mac). Mediapipe is used to detect hand gesture (thumbs up, open palm).

## OpenCV Build Instructions
By default, gstreamer is not enabled in OpenCV, so need to build from source.

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