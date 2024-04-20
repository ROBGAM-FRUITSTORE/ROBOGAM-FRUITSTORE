// Auto-generated. Do not edit!

// (in-package pal_navigation_msgs.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class FollowWaypointsFeedback {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.current_waypoint = null;
    }
    else {
      if (initObj.hasOwnProperty('current_waypoint')) {
        this.current_waypoint = initObj.current_waypoint
      }
      else {
        this.current_waypoint = 0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type FollowWaypointsFeedback
    // Serialize message field [current_waypoint]
    bufferOffset = _serializer.uint32(obj.current_waypoint, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type FollowWaypointsFeedback
    let len;
    let data = new FollowWaypointsFeedback(null);
    // Deserialize message field [current_waypoint]
    data.current_waypoint = _deserializer.uint32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'pal_navigation_msgs/FollowWaypointsFeedback';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '177b7c637cfd197b106babd2a33fde11';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    # ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======
    #feedback definition
    uint32 current_waypoint
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new FollowWaypointsFeedback(null);
    if (msg.current_waypoint !== undefined) {
      resolved.current_waypoint = msg.current_waypoint;
    }
    else {
      resolved.current_waypoint = 0
    }

    return resolved;
    }
};

module.exports = FollowWaypointsFeedback;