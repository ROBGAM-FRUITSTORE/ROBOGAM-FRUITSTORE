# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from pal_navigation_msgs/FollowWaypointsAction.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import actionlib_msgs.msg
import genpy
import geometry_msgs.msg
import pal_navigation_msgs.msg
import std_msgs.msg

class FollowWaypointsAction(genpy.Message):
  _md5sum = "da586c243eb0470df1237e62997462b1"
  _type = "pal_navigation_msgs/FollowWaypointsAction"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

FollowWaypointsActionGoal action_goal
FollowWaypointsActionResult action_result
FollowWaypointsActionFeedback action_feedback

================================================================================
MSG: pal_navigation_msgs/FollowWaypointsActionGoal
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalID goal_id
FollowWaypointsGoal goal

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
string frame_id

================================================================================
MSG: actionlib_msgs/GoalID
# The stamp should store the time at which this goal was requested.
# It is used by an action server when it tries to preempt all
# goals that were requested before a certain time
time stamp

# The id provides a way to associate feedback and
# result message with specific goal requests. The id
# specified must be unique.
string id


================================================================================
MSG: pal_navigation_msgs/FollowWaypointsGoal
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
# Error codes
# Note: The expected priority order of the errors should match the message order
uint32 NONE=0
uint32 UNKNOWN=600
uint32 TASK_EXECUTOR_FAILED=601

#goal definition
uint32 goal_index
uint32 number_of_loops
string bt_model_name
pal_navigation_msgs/Waypoint[] poses

================================================================================
MSG: pal_navigation_msgs/Waypoint
# Error codes
# Note: The expected priority order of the errors should match the message order
uint32 NOTHING=0
uint32 WAIT=1
uint32 ROTATE=2
uint32 DOCK=3
uint32 UNDOCK=4

uint32[] actions
geometry_msgs/PoseStamped pose
================================================================================
MSG: geometry_msgs/PoseStamped
# A Pose with reference coordinate frame and timestamp
Header header
Pose pose

================================================================================
MSG: geometry_msgs/Pose
# A representation of pose in free space, composed of position and orientation. 
Point position
Quaternion orientation

================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z

================================================================================
MSG: geometry_msgs/Quaternion
# This represents an orientation in free space in quaternion form.

float64 x
float64 y
float64 z
float64 w

================================================================================
MSG: pal_navigation_msgs/FollowWaypointsActionResult
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalStatus status
FollowWaypointsResult result

================================================================================
MSG: actionlib_msgs/GoalStatus
GoalID goal_id
uint8 status
uint8 PENDING         = 0   # The goal has yet to be processed by the action server
uint8 ACTIVE          = 1   # The goal is currently being processed by the action server
uint8 PREEMPTED       = 2   # The goal received a cancel request after it started executing
                            #   and has since completed its execution (Terminal State)
uint8 SUCCEEDED       = 3   # The goal was achieved successfully by the action server (Terminal State)
uint8 ABORTED         = 4   # The goal was aborted during execution by the action server due
                            #    to some failure (Terminal State)
uint8 REJECTED        = 5   # The goal was rejected by the action server without being processed,
                            #    because the goal was unattainable or invalid (Terminal State)
uint8 PREEMPTING      = 6   # The goal received a cancel request after it started executing
                            #    and has not yet completed execution
uint8 RECALLING       = 7   # The goal received a cancel request before it started executing,
                            #    but the action server has not yet confirmed that the goal is canceled
uint8 RECALLED        = 8   # The goal received a cancel request before it started executing
                            #    and was successfully cancelled (Terminal State)
uint8 LOST            = 9   # An action client can determine that a goal is LOST. This should not be
                            #    sent over the wire by an action server

#Allow for the user to associate a string with GoalStatus for debugging
string text


================================================================================
MSG: pal_navigation_msgs/FollowWaypointsResult
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#result definition
pal_navigation_msgs/MissedWaypoint[] missed_waypoints

================================================================================
MSG: pal_navigation_msgs/MissedWaypoint
uint32 index
geometry_msgs/PoseStamped goal
uint16 error_code
================================================================================
MSG: pal_navigation_msgs/FollowWaypointsActionFeedback
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======

Header header
actionlib_msgs/GoalStatus status
FollowWaypointsFeedback feedback

================================================================================
MSG: pal_navigation_msgs/FollowWaypointsFeedback
# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
#feedback definition
uint32 current_waypoint
"""
  __slots__ = ['action_goal','action_result','action_feedback']
  _slot_types = ['pal_navigation_msgs/FollowWaypointsActionGoal','pal_navigation_msgs/FollowWaypointsActionResult','pal_navigation_msgs/FollowWaypointsActionFeedback']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       action_goal,action_result,action_feedback

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(FollowWaypointsAction, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.action_goal is None:
        self.action_goal = pal_navigation_msgs.msg.FollowWaypointsActionGoal()
      if self.action_result is None:
        self.action_result = pal_navigation_msgs.msg.FollowWaypointsActionResult()
      if self.action_feedback is None:
        self.action_feedback = pal_navigation_msgs.msg.FollowWaypointsActionFeedback()
    else:
      self.action_goal = pal_navigation_msgs.msg.FollowWaypointsActionGoal()
      self.action_result = pal_navigation_msgs.msg.FollowWaypointsActionResult()
      self.action_feedback = pal_navigation_msgs.msg.FollowWaypointsActionFeedback()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.action_goal.header.seq, _x.action_goal.header.stamp.secs, _x.action_goal.header.stamp.nsecs))
      _x = self.action_goal.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.action_goal.goal_id.stamp.secs, _x.action_goal.goal_id.stamp.nsecs))
      _x = self.action_goal.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.action_goal.goal.goal_index, _x.action_goal.goal.number_of_loops))
      _x = self.action_goal.goal.bt_model_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.action_goal.goal.poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.action_goal.goal.poses:
        length = len(val1.actions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sI'%length
        buff.write(struct.Struct(pattern).pack(*val1.actions))
        _v1 = val1.pose
        _v2 = _v1.header
        _x = _v2.seq
        buff.write(_get_struct_I().pack(_x))
        _v3 = _v2.stamp
        _x = _v3
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v2.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v4 = _v1.pose
        _v5 = _v4.position
        _x = _v5
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v6 = _v4.orientation
        _x = _v6
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_get_struct_3I().pack(_x.action_result.header.seq, _x.action_result.header.stamp.secs, _x.action_result.header.stamp.nsecs))
      _x = self.action_result.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.action_result.status.goal_id.stamp.secs, _x.action_result.status.goal_id.stamp.nsecs))
      _x = self.action_result.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.action_result.status.status
      buff.write(_get_struct_B().pack(_x))
      _x = self.action_result.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.action_result.result.missed_waypoints)
      buff.write(_struct_I.pack(length))
      for val1 in self.action_result.result.missed_waypoints:
        _x = val1.index
        buff.write(_get_struct_I().pack(_x))
        _v7 = val1.goal
        _v8 = _v7.header
        _x = _v8.seq
        buff.write(_get_struct_I().pack(_x))
        _v9 = _v8.stamp
        _x = _v9
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v8.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v10 = _v7.pose
        _v11 = _v10.position
        _x = _v11
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v12 = _v10.orientation
        _x = _v12
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1.error_code
        buff.write(_get_struct_H().pack(_x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.action_feedback.header.seq, _x.action_feedback.header.stamp.secs, _x.action_feedback.header.stamp.nsecs))
      _x = self.action_feedback.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.action_feedback.status.goal_id.stamp.secs, _x.action_feedback.status.goal_id.stamp.nsecs))
      _x = self.action_feedback.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.action_feedback.status.status
      buff.write(_get_struct_B().pack(_x))
      _x = self.action_feedback.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.action_feedback.feedback.current_waypoint
      buff.write(_get_struct_I().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.action_goal is None:
        self.action_goal = pal_navigation_msgs.msg.FollowWaypointsActionGoal()
      if self.action_result is None:
        self.action_result = pal_navigation_msgs.msg.FollowWaypointsActionResult()
      if self.action_feedback is None:
        self.action_feedback = pal_navigation_msgs.msg.FollowWaypointsActionFeedback()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.action_goal.header.seq, _x.action_goal.header.stamp.secs, _x.action_goal.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_goal.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_goal.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_goal.goal_id.stamp.secs, _x.action_goal.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_goal.goal_id.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_goal.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_goal.goal.goal_index, _x.action_goal.goal.number_of_loops,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_goal.goal.bt_model_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_goal.goal.bt_model_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.action_goal.goal.poses = []
      for i in range(0, length):
        val1 = pal_navigation_msgs.msg.Waypoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sI'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.actions = s.unpack(str[start:end])
        _v13 = val1.pose
        _v14 = _v13.header
        start = end
        end += 4
        (_v14.seq,) = _get_struct_I().unpack(str[start:end])
        _v15 = _v14.stamp
        _x = _v15
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v14.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v14.frame_id = str[start:end]
        _v16 = _v13.pose
        _v17 = _v16.position
        _x = _v17
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v18 = _v16.orientation
        _x = _v18
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.action_goal.goal.poses.append(val1)
      _x = self
      start = end
      end += 12
      (_x.action_result.header.seq, _x.action_result.header.stamp.secs, _x.action_result.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_result.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_result.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_result.status.goal_id.stamp.secs, _x.action_result.status.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_result.status.goal_id.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_result.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.action_result.status.status,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_result.status.text = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_result.status.text = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.action_result.result.missed_waypoints = []
      for i in range(0, length):
        val1 = pal_navigation_msgs.msg.MissedWaypoint()
        start = end
        end += 4
        (val1.index,) = _get_struct_I().unpack(str[start:end])
        _v19 = val1.goal
        _v20 = _v19.header
        start = end
        end += 4
        (_v20.seq,) = _get_struct_I().unpack(str[start:end])
        _v21 = _v20.stamp
        _x = _v21
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v20.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v20.frame_id = str[start:end]
        _v22 = _v19.pose
        _v23 = _v22.position
        _x = _v23
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v24 = _v22.orientation
        _x = _v24
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        start = end
        end += 2
        (val1.error_code,) = _get_struct_H().unpack(str[start:end])
        self.action_result.result.missed_waypoints.append(val1)
      _x = self
      start = end
      end += 12
      (_x.action_feedback.header.seq, _x.action_feedback.header.stamp.secs, _x.action_feedback.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_feedback.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_feedback.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_feedback.status.goal_id.stamp.secs, _x.action_feedback.status.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_feedback.status.goal_id.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_feedback.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.action_feedback.status.status,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_feedback.status.text = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_feedback.status.text = str[start:end]
      start = end
      end += 4
      (self.action_feedback.feedback.current_waypoint,) = _get_struct_I().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.action_goal.header.seq, _x.action_goal.header.stamp.secs, _x.action_goal.header.stamp.nsecs))
      _x = self.action_goal.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.action_goal.goal_id.stamp.secs, _x.action_goal.goal_id.stamp.nsecs))
      _x = self.action_goal.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.action_goal.goal.goal_index, _x.action_goal.goal.number_of_loops))
      _x = self.action_goal.goal.bt_model_name
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.action_goal.goal.poses)
      buff.write(_struct_I.pack(length))
      for val1 in self.action_goal.goal.poses:
        length = len(val1.actions)
        buff.write(_struct_I.pack(length))
        pattern = '<%sI'%length
        buff.write(val1.actions.tostring())
        _v25 = val1.pose
        _v26 = _v25.header
        _x = _v26.seq
        buff.write(_get_struct_I().pack(_x))
        _v27 = _v26.stamp
        _x = _v27
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v26.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v28 = _v25.pose
        _v29 = _v28.position
        _x = _v29
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v30 = _v28.orientation
        _x = _v30
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
      _x = self
      buff.write(_get_struct_3I().pack(_x.action_result.header.seq, _x.action_result.header.stamp.secs, _x.action_result.header.stamp.nsecs))
      _x = self.action_result.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.action_result.status.goal_id.stamp.secs, _x.action_result.status.goal_id.stamp.nsecs))
      _x = self.action_result.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.action_result.status.status
      buff.write(_get_struct_B().pack(_x))
      _x = self.action_result.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      length = len(self.action_result.result.missed_waypoints)
      buff.write(_struct_I.pack(length))
      for val1 in self.action_result.result.missed_waypoints:
        _x = val1.index
        buff.write(_get_struct_I().pack(_x))
        _v31 = val1.goal
        _v32 = _v31.header
        _x = _v32.seq
        buff.write(_get_struct_I().pack(_x))
        _v33 = _v32.stamp
        _x = _v33
        buff.write(_get_struct_2I().pack(_x.secs, _x.nsecs))
        _x = _v32.frame_id
        length = len(_x)
        if python3 or type(_x) == unicode:
          _x = _x.encode('utf-8')
          length = len(_x)
        buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
        _v34 = _v31.pose
        _v35 = _v34.position
        _x = _v35
        buff.write(_get_struct_3d().pack(_x.x, _x.y, _x.z))
        _v36 = _v34.orientation
        _x = _v36
        buff.write(_get_struct_4d().pack(_x.x, _x.y, _x.z, _x.w))
        _x = val1.error_code
        buff.write(_get_struct_H().pack(_x))
      _x = self
      buff.write(_get_struct_3I().pack(_x.action_feedback.header.seq, _x.action_feedback.header.stamp.secs, _x.action_feedback.header.stamp.nsecs))
      _x = self.action_feedback.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_2I().pack(_x.action_feedback.status.goal_id.stamp.secs, _x.action_feedback.status.goal_id.stamp.nsecs))
      _x = self.action_feedback.status.goal_id.id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.action_feedback.status.status
      buff.write(_get_struct_B().pack(_x))
      _x = self.action_feedback.status.text
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self.action_feedback.feedback.current_waypoint
      buff.write(_get_struct_I().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      if self.action_goal is None:
        self.action_goal = pal_navigation_msgs.msg.FollowWaypointsActionGoal()
      if self.action_result is None:
        self.action_result = pal_navigation_msgs.msg.FollowWaypointsActionResult()
      if self.action_feedback is None:
        self.action_feedback = pal_navigation_msgs.msg.FollowWaypointsActionFeedback()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.action_goal.header.seq, _x.action_goal.header.stamp.secs, _x.action_goal.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_goal.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_goal.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_goal.goal_id.stamp.secs, _x.action_goal.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_goal.goal_id.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_goal.goal_id.id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_goal.goal.goal_index, _x.action_goal.goal.number_of_loops,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_goal.goal.bt_model_name = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_goal.goal.bt_model_name = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.action_goal.goal.poses = []
      for i in range(0, length):
        val1 = pal_navigation_msgs.msg.Waypoint()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sI'%length
        start = end
        s = struct.Struct(pattern)
        end += s.size
        val1.actions = numpy.frombuffer(str[start:end], dtype=numpy.uint32, count=length)
        _v37 = val1.pose
        _v38 = _v37.header
        start = end
        end += 4
        (_v38.seq,) = _get_struct_I().unpack(str[start:end])
        _v39 = _v38.stamp
        _x = _v39
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v38.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v38.frame_id = str[start:end]
        _v40 = _v37.pose
        _v41 = _v40.position
        _x = _v41
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v42 = _v40.orientation
        _x = _v42
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        self.action_goal.goal.poses.append(val1)
      _x = self
      start = end
      end += 12
      (_x.action_result.header.seq, _x.action_result.header.stamp.secs, _x.action_result.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_result.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_result.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_result.status.goal_id.stamp.secs, _x.action_result.status.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_result.status.goal_id.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_result.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.action_result.status.status,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_result.status.text = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_result.status.text = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.action_result.result.missed_waypoints = []
      for i in range(0, length):
        val1 = pal_navigation_msgs.msg.MissedWaypoint()
        start = end
        end += 4
        (val1.index,) = _get_struct_I().unpack(str[start:end])
        _v43 = val1.goal
        _v44 = _v43.header
        start = end
        end += 4
        (_v44.seq,) = _get_struct_I().unpack(str[start:end])
        _v45 = _v44.stamp
        _x = _v45
        start = end
        end += 8
        (_x.secs, _x.nsecs,) = _get_struct_2I().unpack(str[start:end])
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          _v44.frame_id = str[start:end].decode('utf-8', 'rosmsg')
        else:
          _v44.frame_id = str[start:end]
        _v46 = _v43.pose
        _v47 = _v46.position
        _x = _v47
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _get_struct_3d().unpack(str[start:end])
        _v48 = _v46.orientation
        _x = _v48
        start = end
        end += 32
        (_x.x, _x.y, _x.z, _x.w,) = _get_struct_4d().unpack(str[start:end])
        start = end
        end += 2
        (val1.error_code,) = _get_struct_H().unpack(str[start:end])
        self.action_result.result.missed_waypoints.append(val1)
      _x = self
      start = end
      end += 12
      (_x.action_feedback.header.seq, _x.action_feedback.header.stamp.secs, _x.action_feedback.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_feedback.header.frame_id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_feedback.header.frame_id = str[start:end]
      _x = self
      start = end
      end += 8
      (_x.action_feedback.status.goal_id.stamp.secs, _x.action_feedback.status.goal_id.stamp.nsecs,) = _get_struct_2I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_feedback.status.goal_id.id = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_feedback.status.goal_id.id = str[start:end]
      start = end
      end += 1
      (self.action_feedback.status.status,) = _get_struct_B().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.action_feedback.status.text = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.action_feedback.status.text = str[start:end]
      start = end
      end += 4
      (self.action_feedback.feedback.current_waypoint,) = _get_struct_I().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2I = None
def _get_struct_2I():
    global _struct_2I
    if _struct_2I is None:
        _struct_2I = struct.Struct("<2I")
    return _struct_2I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
_struct_3d = None
def _get_struct_3d():
    global _struct_3d
    if _struct_3d is None:
        _struct_3d = struct.Struct("<3d")
    return _struct_3d
_struct_4d = None
def _get_struct_4d():
    global _struct_4d
    if _struct_4d is None:
        _struct_4d = struct.Struct("<4d")
    return _struct_4d
_struct_B = None
def _get_struct_B():
    global _struct_B
    if _struct_B is None:
        _struct_B = struct.Struct("<B")
    return _struct_B
_struct_H = None
def _get_struct_H():
    global _struct_H
    if _struct_H is None:
        _struct_H = struct.Struct("<H")
    return _struct_H
