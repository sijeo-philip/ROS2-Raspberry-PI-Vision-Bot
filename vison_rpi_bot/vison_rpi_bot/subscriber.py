import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class MinimalSubscriber(Node):
    """A ROS2 Node that receives and AmazingQuote and prints out its info"""

    def __init__(self):
        super().__init__('simple_rpi_subscriber')
        self.subscription = self.create_subscription(
            msg_type=Int16,
            topic='/pub_topic',
            callback=self.listner_callback,
            qos_profile=1)
        
    def listner_callback(self, msg):
        """Method that is called when a new msg is received by the node"""

        self.get_logger().info('I heard: "%d"' %msg.data)

def main(args = None):
    """
    The Main function. 
    :param args: Not used directly by the user, but used by ROS2 to configure
    certain aspects of the Node.
    """

    try:
        rclpy.init(args=args)
        minimal_subscriber = MinimalSubscriber()

        rclpy.spin(minimal_subscriber)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)

    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

