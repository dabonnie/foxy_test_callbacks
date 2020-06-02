#include <iostream>
#include <functional>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

int main(int argc, char ** argv)
{
  rclcpp::init(argc, argv);

  auto node = std::make_shared<rclcpp::Node>("qos_callback_listener");
  rclcpp::SubscriptionOptions options;

  rclcpp::QoS qos(0);
  qos.reliable();
  qos.durability(RMW_QOS_POLICY_DURABILITY_TRANSIENT_LOCAL);

  options.use_default_callbacks = false;
  options.event_callbacks.incompatible_qos_callback = [](rclcpp::QOSOfferedIncompatibleQoSInfo & event) {
    std::cout << "Custom Incompatible Callback!" << std::endl;
  };

  auto subscriber = node->create_subscription<std_msgs::msg::String>(
    "/chatter",
    qos,
    [](const std_msgs::msg::String::SharedPtr) {
      std::cout << "Heard a message" << std::endl;
    },
    options);

  rclcpp::spin(node);
  return 0;
}
