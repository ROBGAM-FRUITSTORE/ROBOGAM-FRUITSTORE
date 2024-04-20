# Install script for directory: /home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/mgs09/tiago_public_ws/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
        file(MAKE_DIRECTORY "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}")
      endif()
      if (NOT EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin")
        file(WRITE "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/.catkin" "")
      endif()
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/mgs09/tiago_public_ws/install/_setup_util.py")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/mgs09/tiago_public_ws/install" TYPE PROGRAM FILES "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/_setup_util.py")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/mgs09/tiago_public_ws/install/env.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/mgs09/tiago_public_ws/install" TYPE PROGRAM FILES "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/env.sh")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/mgs09/tiago_public_ws/install/setup.bash;/home/mgs09/tiago_public_ws/install/local_setup.bash")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/mgs09/tiago_public_ws/install" TYPE FILE FILES
    "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/setup.bash"
    "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/local_setup.bash"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/mgs09/tiago_public_ws/install/setup.sh;/home/mgs09/tiago_public_ws/install/local_setup.sh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/mgs09/tiago_public_ws/install" TYPE FILE FILES
    "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/setup.sh"
    "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/local_setup.sh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/mgs09/tiago_public_ws/install/setup.zsh;/home/mgs09/tiago_public_ws/install/local_setup.zsh")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/mgs09/tiago_public_ws/install" TYPE FILE FILES
    "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/setup.zsh"
    "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/local_setup.zsh"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/home/mgs09/tiago_public_ws/install/.rosinstall")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/home/mgs09/tiago_public_ws/install" TYPE FILE FILES "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/.rosinstall")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pal_interaction_msgs/msg" TYPE FILE FILES
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/actiontag.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/ASRActivation.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/ASREvent.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/ASRLangModelMngmt.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/ASRLanguage.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/asrresult.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/ASRSrvRequest.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/ASRSrvResponse.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/ASRStatus.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/asrupdate.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/AudioDeviceDescription.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/AudioPlayerState.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/audiosignal.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/DirectionOfArrival.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/EnablingSoundLocalisation.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/I18nText.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/I18nArgument.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/Input.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/InputArgument.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/TTSstate.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/TtsText.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/TtsMark.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/VoiceActivity.msg"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/msg/WebGuiEvent.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pal_interaction_msgs/action" TYPE FILE FILES
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/action/ASRFile.action"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/action/AudioPlay.action"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/action/Sound.action"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/action/Tts.action"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pal_interaction_msgs/msg" TYPE FILE FILES
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/ASRFileAction.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/ASRFileActionGoal.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/ASRFileActionResult.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/ASRFileActionFeedback.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/ASRFileGoal.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/ASRFileResult.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/ASRFileFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pal_interaction_msgs/msg" TYPE FILE FILES
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/AudioPlayAction.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/AudioPlayActionGoal.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/AudioPlayActionResult.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/AudioPlayActionFeedback.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/AudioPlayGoal.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/AudioPlayResult.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/AudioPlayFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pal_interaction_msgs/msg" TYPE FILE FILES
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/SoundAction.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/SoundActionGoal.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/SoundActionResult.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/SoundActionFeedback.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/SoundGoal.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/SoundResult.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/SoundFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pal_interaction_msgs/msg" TYPE FILE FILES
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/TtsAction.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/TtsActionGoal.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/TtsActionResult.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/TtsActionFeedback.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/TtsGoal.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/TtsResult.msg"
    "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/pal_interaction_msgs/msg/TtsFeedback.msg"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pal_interaction_msgs/srv" TYPE FILE FILES
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/srv/ASRService.srv"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/srv/GetSpeechDuration.srv"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/srv/recognizerService.srv"
    "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/srv/SoundLocalisationService.srv"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pal_interaction_msgs/cmake" TYPE FILE FILES "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/pal_interaction_msgs-msg-paths.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/include/pal_interaction_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/roseus/ros/pal_interaction_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/common-lisp/ros/pal_interaction_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/share/gennodejs/ros/pal_interaction_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  execute_process(COMMAND "/usr/bin/python3" -m compileall "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/lib/python3/dist-packages/pal_interaction_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3/dist-packages" TYPE DIRECTORY FILES "/home/mgs09/tiago_public_ws/devel/.private/pal_interaction_msgs/lib/python3/dist-packages/pal_interaction_msgs")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/pal_interaction_msgs.pc")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pal_interaction_msgs/cmake" TYPE FILE FILES "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/pal_interaction_msgs-msg-extras.cmake")
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pal_interaction_msgs/cmake" TYPE FILE FILES
    "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/pal_interaction_msgsConfig.cmake"
    "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/catkin_generated/installspace/pal_interaction_msgsConfig-version.cmake"
    )
endif()

if("x${CMAKE_INSTALL_COMPONENT}x" STREQUAL "xUnspecifiedx" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/pal_interaction_msgs" TYPE FILE FILES "/home/mgs09/tiago_public_ws/src/pal_msgs/pal_interaction_msgs/package.xml")
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/mgs09/tiago_public_ws/build/pal_interaction_msgs/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
