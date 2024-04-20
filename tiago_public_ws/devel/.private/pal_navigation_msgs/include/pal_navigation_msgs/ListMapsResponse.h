// Generated by gencpp from file pal_navigation_msgs/ListMapsResponse.msg
// DO NOT EDIT!


#ifndef PAL_NAVIGATION_MSGS_MESSAGE_LISTMAPSRESPONSE_H
#define PAL_NAVIGATION_MSGS_MESSAGE_LISTMAPSRESPONSE_H


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
struct ListMapsResponse_
{
  typedef ListMapsResponse_<ContainerAllocator> Type;

  ListMapsResponse_()
    : success(false)
    , maps()  {
    }
  ListMapsResponse_(const ContainerAllocator& _alloc)
    : success(false)
    , maps(_alloc)  {
  (void)_alloc;
    }



   typedef uint8_t _success_type;
  _success_type success;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> _maps_type;
  _maps_type maps;





  typedef boost::shared_ptr< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> const> ConstPtr;

}; // struct ListMapsResponse_

typedef ::pal_navigation_msgs::ListMapsResponse_<std::allocator<void> > ListMapsResponse;

typedef boost::shared_ptr< ::pal_navigation_msgs::ListMapsResponse > ListMapsResponsePtr;
typedef boost::shared_ptr< ::pal_navigation_msgs::ListMapsResponse const> ListMapsResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator1> & lhs, const ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator2> & rhs)
{
  return lhs.success == rhs.success &&
    lhs.maps == rhs.maps;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator1> & lhs, const ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pal_navigation_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1ab49819563e07b1a3a5b6c08ee434d1";
  }

  static const char* value(const ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1ab49819563e07b1ULL;
  static const uint64_t static_value2 = 0xa3a5b6c08ee434d1ULL;
};

template<class ContainerAllocator>
struct DataType< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pal_navigation_msgs/ListMapsResponse";
  }

  static const char* value(const ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool success\n"
"string[] maps\n"
"\n"
;
  }

  static const char* value(const ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.success);
      stream.next(m.maps);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ListMapsResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pal_navigation_msgs::ListMapsResponse_<ContainerAllocator>& v)
  {
    s << indent << "success: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.success);
    s << indent << "maps[]" << std::endl;
    for (size_t i = 0; i < v.maps.size(); ++i)
    {
      s << indent << "  maps[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.maps[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // PAL_NAVIGATION_MSGS_MESSAGE_LISTMAPSRESPONSE_H
