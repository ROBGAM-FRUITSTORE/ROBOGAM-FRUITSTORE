// Generated by gencpp from file tf_lookup/lookupTransformResponse.msg
// DO NOT EDIT!


#ifndef TF_LOOKUP_MESSAGE_LOOKUPTRANSFORMRESPONSE_H
#define TF_LOOKUP_MESSAGE_LOOKUPTRANSFORMRESPONSE_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <geometry_msgs/TransformStamped.h>

namespace tf_lookup
{
template <class ContainerAllocator>
struct lookupTransformResponse_
{
  typedef lookupTransformResponse_<ContainerAllocator> Type;

  lookupTransformResponse_()
    : transform()  {
    }
  lookupTransformResponse_(const ContainerAllocator& _alloc)
    : transform(_alloc)  {
  (void)_alloc;
    }



   typedef  ::geometry_msgs::TransformStamped_<ContainerAllocator>  _transform_type;
  _transform_type transform;





  typedef boost::shared_ptr< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> const> ConstPtr;

}; // struct lookupTransformResponse_

typedef ::tf_lookup::lookupTransformResponse_<std::allocator<void> > lookupTransformResponse;

typedef boost::shared_ptr< ::tf_lookup::lookupTransformResponse > lookupTransformResponsePtr;
typedef boost::shared_ptr< ::tf_lookup::lookupTransformResponse const> lookupTransformResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::tf_lookup::lookupTransformResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::tf_lookup::lookupTransformResponse_<ContainerAllocator1> & lhs, const ::tf_lookup::lookupTransformResponse_<ContainerAllocator2> & rhs)
{
  return lhs.transform == rhs.transform;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::tf_lookup::lookupTransformResponse_<ContainerAllocator1> & lhs, const ::tf_lookup::lookupTransformResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace tf_lookup

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "627ebb4e09bbb127f87308bbfdbaec08";
  }

  static const char* value(const ::tf_lookup::lookupTransformResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x627ebb4e09bbb127ULL;
  static const uint64_t static_value2 = 0xf87308bbfdbaec08ULL;
};

template<class ContainerAllocator>
struct DataType< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "tf_lookup/lookupTransformResponse";
  }

  static const char* value(const ::tf_lookup::lookupTransformResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "geometry_msgs/TransformStamped transform \n"
"\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/TransformStamped\n"
"# This expresses a transform from coordinate frame header.frame_id\n"
"# to the coordinate frame child_frame_id\n"
"#\n"
"# This message is mostly used by the \n"
"# <a href=\"http://wiki.ros.org/tf\">tf</a> package. \n"
"# See its documentation for more information.\n"
"\n"
"Header header\n"
"string child_frame_id # the frame id of the child frame\n"
"Transform transform\n"
"\n"
"================================================================================\n"
"MSG: std_msgs/Header\n"
"# Standard metadata for higher-level stamped data types.\n"
"# This is generally used to communicate timestamped data \n"
"# in a particular coordinate frame.\n"
"# \n"
"# sequence ID: consecutively increasing ID \n"
"uint32 seq\n"
"#Two-integer timestamp that is expressed as:\n"
"# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n"
"# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n"
"# time-handling sugar is provided by the client library\n"
"time stamp\n"
"#Frame this data is associated with\n"
"string frame_id\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Transform\n"
"# This represents the transform between two coordinate frames in free space.\n"
"\n"
"Vector3 translation\n"
"Quaternion rotation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Vector3\n"
"# This represents a vector in free space. \n"
"# It is only meant to represent a direction. Therefore, it does not\n"
"# make sense to apply a translation to it (e.g., when applying a \n"
"# generic rigid transformation to a Vector3, tf2 will only apply the\n"
"# rotation). If you want your data to be translatable too, use the\n"
"# geometry_msgs/Point message instead.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::tf_lookup::lookupTransformResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.transform);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct lookupTransformResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::tf_lookup::lookupTransformResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::tf_lookup::lookupTransformResponse_<ContainerAllocator>& v)
  {
    s << indent << "transform: ";
    s << std::endl;
    Printer< ::geometry_msgs::TransformStamped_<ContainerAllocator> >::stream(s, indent + "  ", v.transform);
  }
};

} // namespace message_operations
} // namespace ros

#endif // TF_LOOKUP_MESSAGE_LOOKUPTRANSFORMRESPONSE_H
