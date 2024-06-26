// Generated by gencpp from file pal_navigation_msgs/FollowWaypointsFeedback.msg
// DO NOT EDIT!


#ifndef PAL_NAVIGATION_MSGS_MESSAGE_FOLLOWWAYPOINTSFEEDBACK_H
#define PAL_NAVIGATION_MSGS_MESSAGE_FOLLOWWAYPOINTSFEEDBACK_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pal_navigation_msgs
{
template <class ContainerAllocator>
struct FollowWaypointsFeedback_
{
  typedef FollowWaypointsFeedback_<ContainerAllocator> Type;

  FollowWaypointsFeedback_()
    : current_waypoint(0)  {
    }
  FollowWaypointsFeedback_(const ContainerAllocator& _alloc)
    : current_waypoint(0)  {
  (void)_alloc;
    }



   typedef uint32_t _current_waypoint_type;
  _current_waypoint_type current_waypoint;





  typedef boost::shared_ptr< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> const> ConstPtr;

}; // struct FollowWaypointsFeedback_

typedef ::pal_navigation_msgs::FollowWaypointsFeedback_<std::allocator<void> > FollowWaypointsFeedback;

typedef boost::shared_ptr< ::pal_navigation_msgs::FollowWaypointsFeedback > FollowWaypointsFeedbackPtr;
typedef boost::shared_ptr< ::pal_navigation_msgs::FollowWaypointsFeedback const> FollowWaypointsFeedbackConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator1> & lhs, const ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator2> & rhs)
{
  return lhs.current_waypoint == rhs.current_waypoint;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator1> & lhs, const ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pal_navigation_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "177b7c637cfd197b106babd2a33fde11";
  }

  static const char* value(const ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x177b7c637cfd197bULL;
  static const uint64_t static_value2 = 0x106babd2a33fde11ULL;
};

template<class ContainerAllocator>
struct DataType< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pal_navigation_msgs/FollowWaypointsFeedback";
  }

  static const char* value(const ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"#feedback definition\n"
"uint32 current_waypoint\n"
;
  }

  static const char* value(const ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.current_waypoint);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct FollowWaypointsFeedback_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pal_navigation_msgs::FollowWaypointsFeedback_<ContainerAllocator>& v)
  {
    s << indent << "current_waypoint: ";
    Printer<uint32_t>::stream(s, indent + "  ", v.current_waypoint);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PAL_NAVIGATION_MSGS_MESSAGE_FOLLOWWAYPOINTSFEEDBACK_H
