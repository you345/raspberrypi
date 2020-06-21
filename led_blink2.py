import RPi.GPIO as GPIO
import time, sys

GPIO.setmode(GPIO.BCM)

RPORT=21 #GPIO21(R)
YPORT=20 #GPIO20(A/Y)
BPORT=16 #GPIO16(B)
GPIO.setup(RPORT,GPIO.OUT)
GPIO.setup(YPORT,GPIO.OUT)
GPIO.setup(BPORT,GPIO.OUT)

while True:
  try:
    GPIO.output(RPORT, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(RPORT, GPIO.LOW)
    GPIO.output(YPORT, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(YPORT, GPIO.LOW)
    GPIO.output(BPORT, GPIO.HIGH)
    time.sleep(0.8)
    GPIO.output(BPORT, GPIO.LOW)
  except KeyboardInterrupt:
    GPIO.cleanup()
    sys.exit()


