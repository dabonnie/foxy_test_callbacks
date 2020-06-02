#include <chrono>
#include <iostream>
#include <functional>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);

  auto node = std::make_shared<rclcpp::Node>("qos_callback_talker_compatible");
  rclcpp::PublisherOptions options;

  rclcpp::QoS qos(1);
  qos.best_effort();
  qos.durability_volatile();

  auto publisher = node->create_publisher<std_msgs::msg::String>(
    "chatter",
    qos);
  auto timer = node->create_wall_timer(std::chrono::seconds(1), [publisher]() {
    auto message = std_msgs::msg::String();
    message.data = "Hello, world!";
    publisher->publish(message);
  });

  rclcpp::spin(node);
  return 0;
}
