cmake_minimum_required(VERSION 3.5)
project(test_qos_callbacks_cpp)

# Default to C99
if(NOT CMAKE_C_STANDARD)
  set(CMAKE_C_STANDARD 99)
endif()

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)

find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(listener_custom src/listener_custom.cpp)
ament_target_dependencies(listener_custom rclcpp std_msgs)

install(TARGETS
        listener_custom
        DESTINATION lib/${PROJECT_NAME})

add_executable(listener_default src/listener_default.cpp)
ament_target_dependencies(listener_default rclcpp std_msgs)

install(TARGETS
        listener_default
        DESTINATION lib/${PROJECT_NAME})

add_executable(talker_incompatible src/talker_incompatible.cpp)
ament_target_dependencies(talker_incompatible rclcpp std_msgs)

install(TARGETS
        talker_incompatible
        DESTINATION lib/${PROJECT_NAME})

ament_package()
