; Auto-generated. Do not edit!


(cl:in-package pal_visual_localization_msgs-msg)


;//! \htmlinclude VisualLocRecognizeAction.msg.html

(cl:defclass <VisualLocRecognizeAction> (roslisp-msg-protocol:ros-message)
  ((action_goal
    :reader action_goal
    :initarg :action_goal
    :type pal_visual_localization_msgs-msg:VisualLocRecognizeActionGoal
    :initform (cl:make-instance 'pal_visual_localization_msgs-msg:VisualLocRecognizeActionGoal))
   (action_result
    :reader action_result
    :initarg :action_result
    :type pal_visual_localization_msgs-msg:VisualLocRecognizeActionResult
    :initform (cl:make-instance 'pal_visual_localization_msgs-msg:VisualLocRecognizeActionResult))
   (action_feedback
    :reader action_feedback
    :initarg :action_feedback
    :type pal_visual_localization_msgs-msg:VisualLocRecognizeActionFeedback
    :initform (cl:make-instance 'pal_visual_localization_msgs-msg:VisualLocRecognizeActionFeedback)))
)

(cl:defclass VisualLocRecognizeAction (<VisualLocRecognizeAction>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <VisualLocRecognizeAction>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'VisualLocRecognizeAction)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name pal_visual_localization_msgs-msg:<VisualLocRecognizeAction> is deprecated: use pal_visual_localization_msgs-msg:VisualLocRecognizeAction instead.")))

(cl:ensure-generic-function 'action_goal-val :lambda-list '(m))
(cl:defmethod action_goal-val ((m <VisualLocRecognizeAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pal_visual_localization_msgs-msg:action_goal-val is deprecated.  Use pal_visual_localization_msgs-msg:action_goal instead.")
  (action_goal m))

(cl:ensure-generic-function 'action_result-val :lambda-list '(m))
(cl:defmethod action_result-val ((m <VisualLocRecognizeAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pal_visual_localization_msgs-msg:action_result-val is deprecated.  Use pal_visual_localization_msgs-msg:action_result instead.")
  (action_result m))

(cl:ensure-generic-function 'action_feedback-val :lambda-list '(m))
(cl:defmethod action_feedback-val ((m <VisualLocRecognizeAction>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader pal_visual_localization_msgs-msg:action_feedback-val is deprecated.  Use pal_visual_localization_msgs-msg:action_feedback instead.")
  (action_feedback m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <VisualLocRecognizeAction>) ostream)
  "Serializes a message object of type '<VisualLocRecognizeAction>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_goal) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_result) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'action_feedback) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <VisualLocRecognizeAction>) istream)
  "Deserializes a message object of type '<VisualLocRecognizeAction>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_goal) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_result) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'action_feedback) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<VisualLocRecognizeAction>)))
  "Returns string type for a message object of type '<VisualLocRecognizeAction>"
  "pal_visual_localization_msgs/VisualLocRecognizeAction")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'VisualLocRecognizeAction)))
  "Returns string type for a message object of type 'VisualLocRecognizeAction"
  "pal_visual_localization_msgs/VisualLocRecognizeAction")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<VisualLocRecognizeAction>)))
  "Returns md5sum for a message object of type '<VisualLocRecognizeAction>"
  "32838540444654e8e6d15b3145b36be2")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'VisualLocRecognizeAction)))
  "Returns md5sum for a message object of type 'VisualLocRecognizeAction"
  "32838540444654e8e6d15b3145b36be2")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<VisualLocRecognizeAction>)))
  "Returns full string definition for message of type '<VisualLocRecognizeAction>"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%VisualLocRecognizeActionGoal action_goal~%VisualLocRecognizeActionResult action_result~%VisualLocRecognizeActionFeedback action_feedback~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%VisualLocRecognizeGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal definition~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%VisualLocRecognizeResult result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%bool success                                               # return true if get successful recognition~%float64 confidence                                         # recognition confidence~%geometry_msgs/PoseWithCovarianceStamped estimatedPose      # estimated pose (use this only when success == true)~%~%================================================================================~%MSG: geometry_msgs/PoseWithCovarianceStamped~%# This expresses an estimated pose with a reference coordinate frame and timestamp~%~%Header header~%PoseWithCovariance pose~%~%================================================================================~%MSG: geometry_msgs/PoseWithCovariance~%# This represents a pose in free space with uncertainty.~%~%Pose pose~%~%# Row-major representation of the 6x6 covariance matrix~%# The orientation parameters use a fixed-axis representation.~%# In order, the parameters are:~%# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)~%float64[36] covariance~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%VisualLocRecognizeFeedback feedback~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'VisualLocRecognizeAction)))
  "Returns full string definition for message of type 'VisualLocRecognizeAction"
  (cl:format cl:nil "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%VisualLocRecognizeActionGoal action_goal~%VisualLocRecognizeActionResult action_result~%VisualLocRecognizeActionFeedback action_feedback~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeActionGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalID goal_id~%VisualLocRecognizeGoal goal~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: actionlib_msgs/GoalID~%# The stamp should store the time at which this goal was requested.~%# It is used by an action server when it tries to preempt all~%# goals that were requested before a certain time~%time stamp~%~%# The id provides a way to associate feedback and~%# result message with specific goal requests. The id~%# specified must be unique.~%string id~%~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeGoal~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#goal definition~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeActionResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%VisualLocRecognizeResult result~%~%================================================================================~%MSG: actionlib_msgs/GoalStatus~%GoalID goal_id~%uint8 status~%uint8 PENDING         = 0   # The goal has yet to be processed by the action server~%uint8 ACTIVE          = 1   # The goal is currently being processed by the action server~%uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing~%                            #   and has since completed its execution (Terminal State)~%uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)~%uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due~%                            #    to some failure (Terminal State)~%uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,~%                            #    because the goal was unattainable or invalid (Terminal State)~%uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing~%                            #    and has not yet completed execution~%uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,~%                            #    but the action server has not yet confirmed that the goal is canceled~%uint8 RECALLED        = 8   # The goal received a cancel request before it started executing~%                            #    and was successfully cancelled (Terminal State)~%uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be~%                            #    sent over the wire by an action server~%~%#Allow for the user to associate a string with GoalStatus for debugging~%string text~%~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeResult~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#result definition~%bool success                                               # return true if get successful recognition~%float64 confidence                                         # recognition confidence~%geometry_msgs/PoseWithCovarianceStamped estimatedPose      # estimated pose (use this only when success == true)~%~%================================================================================~%MSG: geometry_msgs/PoseWithCovarianceStamped~%# This expresses an estimated pose with a reference coordinate frame and timestamp~%~%Header header~%PoseWithCovariance pose~%~%================================================================================~%MSG: geometry_msgs/PoseWithCovariance~%# This represents a pose in free space with uncertainty.~%~%Pose pose~%~%# Row-major representation of the 6x6 covariance matrix~%# The orientation parameters use a fixed-axis representation.~%# In order, the parameters are:~%# (x, y, z, rotation about X axis, rotation about Y axis, rotation about Z axis)~%float64[36] covariance~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeActionFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%~%Header header~%actionlib_msgs/GoalStatus status~%VisualLocRecognizeFeedback feedback~%~%================================================================================~%MSG: pal_visual_localization_msgs/VisualLocRecognizeFeedback~%# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======~%#feedback~%~%~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <VisualLocRecognizeAction>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_goal))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_result))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'action_feedback))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <VisualLocRecognizeAction>))
  "Converts a ROS message object to a list"
  (cl:list 'VisualLocRecognizeAction
    (cl:cons ':action_goal (action_goal msg))
    (cl:cons ':action_result (action_result msg))
    (cl:cons ':action_feedback (action_feedback msg))
))