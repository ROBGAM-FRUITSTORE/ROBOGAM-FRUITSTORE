execute_process(COMMAND "/home/mgs09/tiago_public_ws/build/pal_python/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/mgs09/tiago_public_ws/build/pal_python/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
