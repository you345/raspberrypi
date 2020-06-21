import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BCM)

LEDPORT=5
SWPORT=6
GPIO.setup(LEDPORT,GPIO.OUT)
GPIO.setup(SWPORT,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
  try:
    if GPIO.input(SWPORT) == GPIO.HIGH:
      GPIO.output(LEDPORT, GPIO.HIGH)
      # time.sleep(0.8)
      # GPIO.output(LEDPORT, GPIO.LOW)
      # time.sleep(0.8)
    else:
      GPIO.output(LEDPORT, GPIO.LOW)
    time.sleep(0.1)
  except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()


