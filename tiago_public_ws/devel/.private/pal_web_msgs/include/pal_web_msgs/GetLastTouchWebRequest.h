// Generated by gencpp from file pal_web_msgs/GetLastTouchWebRequest.msg
// DO NOT EDIT!


#ifndef PAL_WEB_MSGS_MESSAGE_GETLASTTOUCHWEBREQUEST_H
#define PAL_WEB_MSGS_MESSAGE_GETLASTTOUCHWEBREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pal_web_msgs
{
template <class ContainerAllocator>
struct GetLastTouchWebRequest_
{
  typedef GetLastTouchWebRequest_<ContainerAllocator> Type;

  GetLastTouchWebRequest_()
    {
    }
  GetLastTouchWebRequest_(const ContainerAllocator& _alloc)
    {
  (void)_alloc;
    }







  typedef boost::shared_ptr< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> const> ConstPtr;

}; // struct GetLastTouchWebRequest_

typedef ::pal_web_msgs::GetLastTouchWebRequest_<std::allocator<void> > GetLastTouchWebRequest;

typedef boost::shared_ptr< ::pal_web_msgs::GetLastTouchWebRequest > GetLastTouchWebRequestPtr;
typedef boost::shared_ptr< ::pal_web_msgs::GetLastTouchWebRequest const> GetLastTouchWebRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


} // namespace pal_web_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "d41d8cd98f00b204e9800998ecf8427e";
  }

  static const char* value(const ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xd41d8cd98f00b204ULL;
  static const uint64_t static_value2 = 0xe9800998ecf8427eULL;
};

template<class ContainerAllocator>
struct DataType< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pal_web_msgs/GetLastTouchWebRequest";
  }

  static const char* value(const ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "\n"
;
  }

  static const char* value(const ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream&, T)
    {}

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetLastTouchWebRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream&, const std::string&, const ::pal_web_msgs::GetLastTouchWebRequest_<ContainerAllocator>&)
  {}
};

} // namespace message_operations
} // namespace ros

#endif // PAL_WEB_MSGS_MESSAGE_GETLASTTOUCHWEBREQUEST_H
