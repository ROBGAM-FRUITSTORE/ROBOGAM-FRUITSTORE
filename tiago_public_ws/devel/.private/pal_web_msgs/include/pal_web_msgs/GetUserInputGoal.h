// Generated by gencpp from file pal_web_msgs/GetUserInputGoal.msg
// DO NOT EDIT!


#ifndef PAL_WEB_MSGS_MESSAGE_GETUSERINPUTGOAL_H
#define PAL_WEB_MSGS_MESSAGE_GETUSERINPUTGOAL_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <pal_web_msgs/WebGoTo.h>
#include <pal_interaction_msgs/TtsGoal.h>
#include <pal_interaction_msgs/TtsGoal.h>

namespace pal_web_msgs
{
template <class ContainerAllocator>
struct GetUserInputGoal_
{
  typedef GetUserInputGoal_<ContainerAllocator> Type;

  GetUserInputGoal_()
    : web_go_to()
    , question_tts()
    , valid_asr_inputs()
    , asr_language()
    , asr_timeout()
    , retry_asr(false)
    , retry_tts()
    , wait_for_interaction(false)  {
    }
  GetUserInputGoal_(const ContainerAllocator& _alloc)
    : web_go_to(_alloc)
    , question_tts(_alloc)
    , valid_asr_inputs(_alloc)
    , asr_language(_alloc)
    , asr_timeout()
    , retry_asr(false)
    , retry_tts(_alloc)
    , wait_for_interaction(false)  {
  (void)_alloc;
    }



   typedef  ::pal_web_msgs::WebGoTo_<ContainerAllocator>  _web_go_to_type;
  _web_go_to_type web_go_to;

   typedef  ::pal_interaction_msgs::TtsGoal_<ContainerAllocator>  _question_tts_type;
  _question_tts_type question_tts;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> _valid_asr_inputs_type;
  _valid_asr_inputs_type valid_asr_inputs;

   typedef std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> _asr_language_type;
  _asr_language_type asr_language;

   typedef ros::Duration _asr_timeout_type;
  _asr_timeout_type asr_timeout;

   typedef uint8_t _retry_asr_type;
  _retry_asr_type retry_asr;

   typedef  ::pal_interaction_msgs::TtsGoal_<ContainerAllocator>  _retry_tts_type;
  _retry_tts_type retry_tts;

   typedef uint8_t _wait_for_interaction_type;
  _wait_for_interaction_type wait_for_interaction;





  typedef boost::shared_ptr< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> const> ConstPtr;

}; // struct GetUserInputGoal_

typedef ::pal_web_msgs::GetUserInputGoal_<std::allocator<void> > GetUserInputGoal;

typedef boost::shared_ptr< ::pal_web_msgs::GetUserInputGoal > GetUserInputGoalPtr;
typedef boost::shared_ptr< ::pal_web_msgs::GetUserInputGoal const> GetUserInputGoalConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator1> & lhs, const ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator2> & rhs)
{
  return lhs.web_go_to == rhs.web_go_to &&
    lhs.question_tts == rhs.question_tts &&
    lhs.valid_asr_inputs == rhs.valid_asr_inputs &&
    lhs.asr_language == rhs.asr_language &&
    lhs.asr_timeout == rhs.asr_timeout &&
    lhs.retry_asr == rhs.retry_asr &&
    lhs.retry_tts == rhs.retry_tts &&
    lhs.wait_for_interaction == rhs.wait_for_interaction;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator1> & lhs, const ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace pal_web_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "f9981492f9db592397a82220d62ebd0e";
  }

  static const char* value(const ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0xf9981492f9db5923ULL;
  static const uint64_t static_value2 = 0x97a82220d62ebd0eULL;
};

template<class ContainerAllocator>
struct DataType< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "pal_web_msgs/GetUserInputGoal";
  }

  static const char* value(const ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> >
{
  static const char* value()
  {
    return "# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"pal_web_msgs/WebGoTo web_go_to # Web to display for requesting feedback\n"
"pal_interaction_msgs/TtsGoal question_tts # TTS question, asked before waiting for feedback\n"
"string[] valid_asr_inputs # empty is no ASR, can be regex\n"
"string asr_language # empty is current default\n"
"duration asr_timeout\n"
"bool retry_asr\n"
"pal_interaction_msgs/TtsGoal retry_tts # If retrying, say this setence\n"
"bool wait_for_interaction # If true, wait for an interaction before starting the ASR\n"
"\n"
"================================================================================\n"
"MSG: pal_web_msgs/WebGoTo\n"
"uint8 IMAGE = 0\n"
"uint8 VIDEO = 1\n"
"uint8 URI   = 2\n"
"uint8 URL = 3\n"
"uint8 TOUCH_PAGE = 4\n"
"uint8 TOUCH_PROJECT = 5\n"
"uint8 type # one of the enum above\n"
"\n"
"string value # Destination (an image, a video or a uri)\n"
"\n"
"================================================================================\n"
"MSG: pal_interaction_msgs/TtsGoal\n"
"# ====== DO NOT MODIFY! AUTOGENERATED FROM AN ACTION DEFINITION ======\n"
"## goal definition\n"
"\n"
"# utterance will contain indications to construct\n"
"# the text to be spoken.\n"
"# It must be specified in a section/key format \n"
"# for internationalisation. The actual text will\n"
"# be obtained from configuration files as in pal_tts_cfg pkg.\n"
" \n"
"I18nText text\n"
"TtsText rawtext\n"
"\n"
"# This is to suggest a voice name to the \n"
"# tts engine. For the same language we might have\n"
"# a variety of voices available, and this variable \n"
"# is to choose one among them. \n"
"# (not implemented yet)\n"
"string speakerName\n"
"\n"
"# Time to wait before synthesising the text itself.\n"
"# It can be used to produced delayed speech.\n"
"float64 wait_before_speaking\n"
"\n"
"\n"
"================================================================================\n"
"MSG: pal_interaction_msgs/I18nText\n"
"# section/key is used as in examples in the pal_tts_cfg pkg.\n"
"string section\n"
"string key\n"
"\n"
"# language id, must be speficied using RFC 3066\n"
"string lang_id\n"
"\n"
"# arguments contain the values by which \n"
"# occurrences of '%s' will be replaced in the \n"
"# main text.\n"
"# This only supports up to 2 arguments and no recursion.\n"
"# However, recursion and more argumnents are\n"
"# planned to be supported in the future.\n"
"I18nArgument[] arguments\n"
"\n"
"================================================================================\n"
"MSG: pal_interaction_msgs/I18nArgument\n"
"# section key, override the value in expanded.\n"
"# Use expanded for text that do not need expansion.\n"
"# Please note that expanded here will not be translated \n"
"# to any language.\n"
"\n"
"string section\n"
"string key\n"
"string expanded\n"
"\n"
"\n"
"================================================================================\n"
"MSG: pal_interaction_msgs/TtsText\n"
"# this message is to specify \n"
"# raw text to the TTS server. \n"
"\n"
"string text\n"
"\n"
"# Language id in RFC 3066 format\n"
"# This field is mandatory\n"
"string lang_id\n"
;
  }

  static const char* value(const ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.web_go_to);
      stream.next(m.question_tts);
      stream.next(m.valid_asr_inputs);
      stream.next(m.asr_language);
      stream.next(m.asr_timeout);
      stream.next(m.retry_asr);
      stream.next(m.retry_tts);
      stream.next(m.wait_for_interaction);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct GetUserInputGoal_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::pal_web_msgs::GetUserInputGoal_<ContainerAllocator>& v)
  {
    s << indent << "web_go_to: ";
    s << std::endl;
    Printer< ::pal_web_msgs::WebGoTo_<ContainerAllocator> >::stream(s, indent + "  ", v.web_go_to);
    s << indent << "question_tts: ";
    s << std::endl;
    Printer< ::pal_interaction_msgs::TtsGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.question_tts);
    s << indent << "valid_asr_inputs[]" << std::endl;
    for (size_t i = 0; i < v.valid_asr_inputs.size(); ++i)
    {
      s << indent << "  valid_asr_inputs[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.valid_asr_inputs[i]);
    }
    s << indent << "asr_language: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>::stream(s, indent + "  ", v.asr_language);
    s << indent << "asr_timeout: ";
    Printer<ros::Duration>::stream(s, indent + "  ", v.asr_timeout);
    s << indent << "retry_asr: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.retry_asr);
    s << indent << "retry_tts: ";
    s << std::endl;
    Printer< ::pal_interaction_msgs::TtsGoal_<ContainerAllocator> >::stream(s, indent + "  ", v.retry_tts);
    s << indent << "wait_for_interaction: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.wait_for_interaction);
  }
};

} // namespace message_operations
} // namespace ros

#endif // PAL_WEB_MSGS_MESSAGE_GETUSERINPUTGOAL_H
