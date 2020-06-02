import rclpy
from rclpy.node import Node
from rclpy.qos import DurabilityPolicy
from rclpy.qos import QoSProfile
from rclpy.qos_event import SubscriptionEventCallbacks

from std_msgs.msg import String


class MinimalSubscriber(Node):

    def __init__(self):

        qos = QoSProfile(depth=10)
        qos.durability = DurabilityPolicy.RMW_QOS_POLICY_DURABILITY_TRANSIENT_LOCAL

        custom_callback = lambda event: print("Custom Incompatible Callback!")
        callbacks = SubscriptionEventCallbacks()
        callbacks.incompatible_qos = custom_callback

        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            String,
            'topic',
            self.listener_callback,
            qos,
            event_callbacks=callbacks)

    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()