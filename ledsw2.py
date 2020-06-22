# coding: utf-8
import RPi.GPIO as GPIO
import time
import subprocess

SHUTTER_PIN=4 #board7
LED_PIN=5     #board25
RLED_PIN=21   #board40
ALED_PIN=20   #board38
GLED_PIN=16   #board36

cmd = 'date'
flag = 0

def main():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(SHUTTER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(LED_PIN, GPIO.OUT)
  GPIO.setup(RLED_PIN, GPIO.OUT)
  GPIO.setup(ALED_PIN, GPIO.OUT)
  GPIO.setup(GLED_PIN, GPIO.OUT)
  GPIO.add_event_detect(SHUTTER_PIN, GPIO.BOTH, callback=callback, bouncetime=40)

  try:
    while(True):
      time.sleep(0.1)
  except KeyboardInterrupt:
    print("break")
    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.output(RLED_PIN, GPIO.LOW)
    GPIO.output(ALED_PIN, GPIO.LOW)
    GPIO.output(GLED_PIN, GPIO.LOW)
    GPIO.cleanup()

def callback(gpio_pin):
  if(GPIO.input(gpio_pin) == 1):
    print(gpio_pin)
    GPIO.output(LED_PIN, GPIO.HIGH)
    ret = subprocess.check_output(cmd, shell=True)
    print(ret)

    global flag

    if( flag == 0):
      GPIO.output(RLED_PIN, GPIO.HIGH)
      GPIO.output(ALED_PIN, GPIO.LOW)
      GPIO.output(GLED_PIN, GPIO.LOW)
      time.sleep(1.0)
      GPIO.output(RLED_PIN, GPIO.LOW)
    elif( flag == 1):
      GPIO.output(RLED_PIN, GPIO.LOW)
      GPIO.output(ALED_PIN, GPIO.HIGH)
      GPIO.output(GLED_PIN, GPIO.LOW)
      time.sleep(1.0)
      GPIO.output(ALED_PIN, GPIO.LOW)
    elif( flag == 2):
      GPIO.output(RLED_PIN, GPIO.LOW)
      GPIO.output(ALED_PIN, GPIO.LOW)
      GPIO.output(GLED_PIN, GPIO.HIGH)
      time.sleep(1.0)
      GPIO.output(GLED_PIN, GPIO.LOW)
    flag = flag + 1
    flag = flag % 3
      
  else:
    GPIO.output(LED_PIN, GPIO.LOW)

if __name__ == "__main__":
  main()
