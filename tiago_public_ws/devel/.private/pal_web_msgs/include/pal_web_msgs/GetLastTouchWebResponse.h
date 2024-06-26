// Generated by gencpp from file pal_web_msgs/GetLastTouchWebResponse.msg
// DO NOT EDIT!


#ifndef PAL_WEB_MSGS_MESSAGE_GETLASTTOUCHWEBRESPONSE_H
#define PAL_WEB_MSGS_MESSAGE_GETLASTTOUCHWEBRESPONSE_H


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
struct GetLastTouchWebResponse_
{
  typedef GetLastTouchWebResponse_<ContainerAllocator> Type;

  GetLastTouchWebResponse_()
    : project()
    , page()  {
    }
  GetLastTouchWebResponse_(const ContainerAllocator& _alloc)
    : project(_alloc)
    , page(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _project_type;
  _project_type project;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _page_type;
  _page_type page;





  typedef boost::shared_ptr< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> const> ConstPtr;

}; // struct GetLastTouchWebResponse_

typedef ::pal_web_msgs::GetLastTouchWebResponse_<std::allocator<void> > GetLastTouchWebResponse;

typedef boost::shared_ptr< ::pal_web_msgs::GetLastTouchWebResponse > GetLastTouchWebResponsePtr;
typedef boost::shared_ptr< ::pal_web_msgs::GetLastTouchWebResponse const> GetLastTouchWebResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator1> & lhs, const ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator2> & rhs)
{
  return lhs.project == rhs.project &&
    lhs.page == rhs.page;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator1> & lhs, const ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pal_web_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f9395367802b9132f5764b023404f09b";
  }

  static const char* value(const ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf9395367802b9132ULL;
  static const uint64_t static_value2 = 0xf5764b023404f09bULL;
};

template<class ContainerAllocator>
struct DataType< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pal_web_msgs/GetLastTouchWebResponse";
  }

  static const char* value(const ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string project\n"
"string page\n"
;
  }

  static const char* value(const ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.project);
      stream.next(m.page);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetLastTouchWebResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pal_web_msgs::GetLastTouchWebResponse_<ContainerAllocator>& v)
  {
    s << indent << "project: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.project);
    s << indent << "page: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.page);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PAL_WEB_MSGS_MESSAGE_GETLASTTOUCHWEBRESPONSE_H
