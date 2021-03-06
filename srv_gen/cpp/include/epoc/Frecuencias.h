/* Auto-generated by genmsg_cpp for file /home/carlos/fuerte_workspace/sandbox/epoc/srv/Frecuencias.srv */
#ifndef EPOC_SERVICE_FRECUENCIAS_H
#define EPOC_SERVICE_FRECUENCIAS_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "ros/service_traits.h"




namespace epoc
{
template <class ContainerAllocator>
struct FrecuenciasRequest_ {
  typedef FrecuenciasRequest_<ContainerAllocator> Type;

  FrecuenciasRequest_()
  : sen()
  {
    sen.assign(0.0);
  }

  FrecuenciasRequest_(const ContainerAllocator& _alloc)
  : sen()
  {
    sen.assign(0.0);
  }

  typedef boost::array<double, 14>  _sen_type;
  boost::array<double, 14>  sen;


  typedef boost::shared_ptr< ::epoc::FrecuenciasRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::epoc::FrecuenciasRequest_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct FrecuenciasRequest
typedef  ::epoc::FrecuenciasRequest_<std::allocator<void> > FrecuenciasRequest;

typedef boost::shared_ptr< ::epoc::FrecuenciasRequest> FrecuenciasRequestPtr;
typedef boost::shared_ptr< ::epoc::FrecuenciasRequest const> FrecuenciasRequestConstPtr;


template <class ContainerAllocator>
struct FrecuenciasResponse_ {
  typedef FrecuenciasResponse_<ContainerAllocator> Type;

  FrecuenciasResponse_()
  : a(0.0)
  {
  }

  FrecuenciasResponse_(const ContainerAllocator& _alloc)
  : a(0.0)
  {
  }

  typedef double _a_type;
  double a;


  typedef boost::shared_ptr< ::epoc::FrecuenciasResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::epoc::FrecuenciasResponse_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct FrecuenciasResponse
typedef  ::epoc::FrecuenciasResponse_<std::allocator<void> > FrecuenciasResponse;

typedef boost::shared_ptr< ::epoc::FrecuenciasResponse> FrecuenciasResponsePtr;
typedef boost::shared_ptr< ::epoc::FrecuenciasResponse const> FrecuenciasResponseConstPtr;

struct Frecuencias
{

typedef FrecuenciasRequest Request;
typedef FrecuenciasResponse Response;
Request request;
Response response;

typedef Request RequestType;
typedef Response ResponseType;
}; // struct Frecuencias
} // namespace epoc

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::epoc::FrecuenciasRequest_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::epoc::FrecuenciasRequest_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::epoc::FrecuenciasRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "2e3ee18be322543f7d0c29962cb75137";
  }

  static const char* value(const  ::epoc::FrecuenciasRequest_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x2e3ee18be322543fULL;
  static const uint64_t static_value2 = 0x7d0c29962cb75137ULL;
};

template<class ContainerAllocator>
struct DataType< ::epoc::FrecuenciasRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "epoc/FrecuenciasRequest";
  }

  static const char* value(const  ::epoc::FrecuenciasRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::epoc::FrecuenciasRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float64[14] sen\n\
\n\
";
  }

  static const char* value(const  ::epoc::FrecuenciasRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::epoc::FrecuenciasRequest_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros


namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::epoc::FrecuenciasResponse_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::epoc::FrecuenciasResponse_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::epoc::FrecuenciasResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "8d59eeb6f47744097bbc77f6e8d9be14";
  }

  static const char* value(const  ::epoc::FrecuenciasResponse_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x8d59eeb6f4774409ULL;
  static const uint64_t static_value2 = 0x7bbc77f6e8d9be14ULL;
};

template<class ContainerAllocator>
struct DataType< ::epoc::FrecuenciasResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "epoc/FrecuenciasResponse";
  }

  static const char* value(const  ::epoc::FrecuenciasResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::epoc::FrecuenciasResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "float64 a\n\
\n\
";
  }

  static const char* value(const  ::epoc::FrecuenciasResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct IsFixedSize< ::epoc::FrecuenciasResponse_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::epoc::FrecuenciasRequest_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.sen);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct FrecuenciasRequest_
} // namespace serialization
} // namespace ros


namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::epoc::FrecuenciasResponse_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.a);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct FrecuenciasResponse_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace service_traits
{
template<>
struct MD5Sum<epoc::Frecuencias> {
  static const char* value() 
  {
    return "c12060a30a7682910d5c890d5372e100";
  }

  static const char* value(const epoc::Frecuencias&) { return value(); } 
};

template<>
struct DataType<epoc::Frecuencias> {
  static const char* value() 
  {
    return "epoc/Frecuencias";
  }

  static const char* value(const epoc::Frecuencias&) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<epoc::FrecuenciasRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "c12060a30a7682910d5c890d5372e100";
  }

  static const char* value(const epoc::FrecuenciasRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<epoc::FrecuenciasRequest_<ContainerAllocator> > {
  static const char* value() 
  {
    return "epoc/Frecuencias";
  }

  static const char* value(const epoc::FrecuenciasRequest_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct MD5Sum<epoc::FrecuenciasResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "c12060a30a7682910d5c890d5372e100";
  }

  static const char* value(const epoc::FrecuenciasResponse_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct DataType<epoc::FrecuenciasResponse_<ContainerAllocator> > {
  static const char* value() 
  {
    return "epoc/Frecuencias";
  }

  static const char* value(const epoc::FrecuenciasResponse_<ContainerAllocator> &) { return value(); } 
};

} // namespace service_traits
} // namespace ros

#endif // EPOC_SERVICE_FRECUENCIAS_H

