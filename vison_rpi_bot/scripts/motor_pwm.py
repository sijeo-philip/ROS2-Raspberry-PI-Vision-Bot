import RPi.GPIO as GPIO
import time 

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

pwm_r = GPIO.PWM(right_motor_en, 1000)
pwm_l = GPIO.PWM(left_motor_en, 1000)

pwm_r.start(75)
pwm_l.start(75)

def reverse( secs ):
    print("Moving Forward for {} seconds\n".format(secs))
    GPIO.output(right_motor_a, GPIO.HIGH)
    GPIO.output(right_motor_b, GPIO.LOW)
    GPIO.output(left_motor_a, GPIO.HIGH)
    GPIO.output(left_motor_b, GPIO.LOW)
    time.sleep(secs)

def forward( secs ):
    print("Moving Reverse for {} seconds\n".format(secs))
    GPIO.output(right_motor_a, GPIO.LOW)
    GPIO.output(right_motor_b, GPIO.HIGH)
    GPIO.output(left_motor_a, GPIO.LOW)
    GPIO.output(left_motor_b, GPIO.HIGH)
    time.sleep(secs)

def right(secs):
    print("Moving Left for {} seconds\n".format(secs))
    GPIO.output(right_motor_a, GPIO.LOW)
    GPIO.output(right_motor_b, GPIO.HIGH)
    GPIO.output(left_motor_a, GPIO.HIGH)
    GPIO.output(left_motor_b, GPIO.LOW)
    time.sleep(secs)

def left(secs):
    print("Moving Right for {} seconds\n".format(secs))
    GPIO.output(right_motor_a, GPIO.HIGH)
    GPIO.output(right_motor_b, GPIO.LOW)
    GPIO.output(left_motor_a, GPIO.LOW)
    GPIO.output(left_motor_b, GPIO.HIGH)
    time.sleep(secs)

def stop():
    print("Stopping the Robot\n")
    pwm_l.ChangeDutyCycle(0)
    pwm_r.ChangeDutyCycle(0)


def exit_():
    GPIO.cleanup()

def main():
    forward(2)
    reverse(2)
    left(2)
    right(2)
    stop()
    exit_()

if __name__ == '__main__':
    main()