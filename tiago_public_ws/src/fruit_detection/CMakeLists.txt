cmake_minimum_required(VERSION 2.8.3)
cmake_policy(SET CMP0048 NEW)
project(fruit_detection)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  actionlib
  cv_bridge
  image_transport
  sensor_msgs
  control_msgs
  geometry_msgs
)

find_package(OpenCV REQUIRED)

catkin_package(
  CATKIN_DEPENDS
    roscpp
    actionlib
    cv_bridge
    image_transport
    sensor_msgs
    control_msgs
    geometry_msgs
)

include_directories(
  ${catkin_INCLUDE_DIRS}
  ${OpenCV_INCLUDE_DIRS}
)

### INSTALL ###

catkin_install_python(PROGRAMS src/fruit_detection.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
