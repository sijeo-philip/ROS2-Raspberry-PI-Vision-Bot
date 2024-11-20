import rclpy
from rclpy.node import Node

from std_msgs.msg import Int16

class MinimalPublisher(Node):
    """A ROS2 Node that publishes an amazing quote"""

    def __init__(self):
        super().__init__('simple_rpi_publisher')

        self.publisher_ = self.create_publisher(
            msg_type=Int16,
            topic='/pub_topic',
            qos_profile=1
        )
        timer_period: float = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.incremental_id: int = 0

    def timer_callback(self):
        """ Method that is periodically called by the timer"""
        msg = Int16()

        msg.data = self.incremental_id

        self.publisher_.publish(msg)

        self.get_logger().info('Publishing: "%d"'%msg.data)

        self.incremental_id += 1

def main(args=None):
    """
    The main function. 
    :param args: Not used directly by the user, but used by ROS2
    configure certain aspects of the Node."
    """

    try:
        rclpy.init(args=args)
        minimal_publisher = MinimalPublisher()

        rclpy.spin(minimal_publisher)
    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()

