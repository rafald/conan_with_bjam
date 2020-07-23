cmake_minimum_required(VERSION 3.1.3)
project(folly_example CXX)

set(CMAKE_VERBOSE_MAKEFILE ON)

INCLUDE(InvokeConan.cmake)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(TARGETS)

if(CMAKE_SYSTEM_NAME STREQUAL "Windows")
  # Check target architecture
  if (NOT CMAKE_SIZEOF_VOID_P EQUAL 8)
    message(FATAL_ERROR "Folly requires a 64bit target architecture.")
  endif()
endif()

add_executable(${PROJECT_NAME} main.cpp)
target_link_libraries(${PROJECT_NAME} CONAN_PKG::folly)
set_target_properties(${PROJECT_NAME} PROPERTIES CXX_STANDARD 14)
