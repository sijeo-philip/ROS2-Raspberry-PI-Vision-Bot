import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16
import RPi.GPIO as GPIO
from geometry_msgs.msg import Twist

class VelocitySubscriber(Node):

    def __init__(self):
        super().__init__('cmd_vel_subscriber')
        self.subscription = self.create_subscription(
            msg_type=Twist,
            topic='/cmd_vel',
            callback=self.cmd_to_pwm_callback,
            qos_profile=1)
        right_motor_a = 20
        right_motor_b = 21
        right_motor_en = 16

        left_motor_a = 24
        left_motor_b = 25
        left_motor_en = 23

        GPIO.setmode(GPIO.BCM)

        GPIO.setup(right_motor_a, GPIO.OUT)
        GPIO.setup(right_motor_b, GPIO.OUT)
        GPIO.setup(right_motor_en, GPIO.OUT)

        GPIO.setup(left_motor_a, GPIO.OUT)
        GPIO.setup(left_motor_b, GPIO.OUT)
        GPIO.setup(left_motor_en, GPIO.OUT)

        self.pwm_r = GPIO.PWM(right_motor_en, 1000)
        self.pwm_l = GPIO.PWM(left_motor_en, 1000)

        self.pwm_r.start(75)
        self.pwm_l.start(75)
        self.mr_a = right_motor_a
        self.mr_b = right_motor_b
        self.ml_a = left_motor_a
        self.ml_b = left_motor_b
        
    def cmd_to_pwm_callback(self, msg):
        """Method that is called when a new msg is received by the node"""
        right_wheel_vel = ( msg.linear.x + msg.angular.z )/2
        left_wheel_vel = ( msg.linear.x - msg.angular.z )/2
        print("{} / {}".format(right_wheel_vel, left_wheel_vel))

        GPIO.output(self.mr_a, right_wheel_vel < 0)
        GPIO.output(self.mr_b, right_wheel_vel > 0)
        GPIO.output(self.ml_a, left_wheel_vel < 0)
        GPIO.output(self.ml_b, left_wheel_vel > 0)


def main(args = None):
    try:
        rclpy.init(args=args)
        velocity_subscriber = VelocitySubscriber()

        rclpy.spin(velocity_subscriber)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(e)

    velocity_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

