// Generated by gencpp from file pal_detection_msgs/SelectTexturedObjectRequest.msg
// DO NOT EDIT!


#ifndef PAL_DETECTION_MSGS_MESSAGE_SELECTTEXTUREDOBJECTREQUEST_H
#define PAL_DETECTION_MSGS_MESSAGE_SELECTTEXTUREDOBJECTREQUEST_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace pal_detection_msgs
{
template <class ContainerAllocator>
struct SelectTexturedObjectRequest_
{
  typedef SelectTexturedObjectRequest_<ContainerAllocator> Type;

  SelectTexturedObjectRequest_()
    : imageFullPathFileName()
    , width(0.0)
    , height(0.0)  {
    }
  SelectTexturedObjectRequest_(const ContainerAllocator& _alloc)
    : imageFullPathFileName(_alloc)
    , width(0.0)
    , height(0.0)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _imageFullPathFileName_type;
  _imageFullPathFileName_type imageFullPathFileName;

   typedef double _width_type;
  _width_type width;

   typedef double _height_type;
  _height_type height;





  typedef boost::shared_ptr< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> const> ConstPtr;

}; // struct SelectTexturedObjectRequest_

typedef ::pal_detection_msgs::SelectTexturedObjectRequest_<std::allocator<void> > SelectTexturedObjectRequest;

typedef boost::shared_ptr< ::pal_detection_msgs::SelectTexturedObjectRequest > SelectTexturedObjectRequestPtr;
typedef boost::shared_ptr< ::pal_detection_msgs::SelectTexturedObjectRequest const> SelectTexturedObjectRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator1> & lhs, const ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator2> & rhs)
{
  return lhs.imageFullPathFileName == rhs.imageFullPathFileName &&
    lhs.width == rhs.width &&
    lhs.height == rhs.height;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator1> & lhs, const ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pal_detection_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "9e19a1b55ded74005b343f07cfe126b1";
  }

  static const char* value(const ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x9e19a1b55ded7400ULL;
  static const uint64_t static_value2 = 0x5b343f07cfe126b1ULL;
};

template<class ContainerAllocator>
struct DataType< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pal_detection_msgs/SelectTexturedObjectRequest";
  }

  static const char* value(const ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# This service message allows specifying to the texture_detector node\n"
"# which object it must look for.\n"
"#\n"
"\n"
"string imageFullPathFileName # image filename including full path and file extension (always .png)\n"
"                             # The file must exist in the computer where the texture_detector node\n"
"                             # is running. The image must contain a frontal view of a planar textured object.\n"
"float64 width                # width of the planar object in meters. Set to 0 if no pose estimation is required.\n"
"float64 height               # height of the planar object in meters. Set to 0 if no pose estimation is required.\n"
;
  }

  static const char* value(const ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.imageFullPathFileName);
      stream.next(m.width);
      stream.next(m.height);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct SelectTexturedObjectRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pal_detection_msgs::SelectTexturedObjectRequest_<ContainerAllocator>& v)
  {
    s << indent << "imageFullPathFileName: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.imageFullPathFileName);
    s << indent << "width: ";
    Printer<double>::stream(s, indent + "  ", v.width);
    s << indent << "height: ";
    Printer<double>::stream(s, indent + "  ", v.height);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PAL_DETECTION_MSGS_MESSAGE_SELECTTEXTUREDOBJECTREQUEST_H
