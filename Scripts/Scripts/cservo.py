import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(int(sys.argv[1]), GPIO.OUT)
angle = float(sys.argv[2])
pwm=GPIO.PWM(int(sys.argv[1]),50)
pwm.start(angle)
time.sleep(0.5)
GPIO.cleanup

