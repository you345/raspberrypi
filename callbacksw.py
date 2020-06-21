# coding: utf-8
import RPi.GPIO as GPIO
import time
import subprocess

SHUTTER_PIN=4 #board7
RLED_PIN=21   #board40
ALED_PIN=20   #board38
GLED_PIN=16   #board36

cmd = 'date'

def main():
  GPIO.setwarnings(False)
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(SHUTTER_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
  GPIO.setup(RLED_PIN, GPIO.OUT)
  GPIO.add_event_detect(SHUTTER_PIN, GPIO.BOTH, callback=callback, bouncetime=40)

  try:
    while(True):
      time.sleep(0.1)
  except KeyboardInterrupt:
    print("break")
    GPIO.output(RLED_PIN, GPIO.LOW)
    GPIO.cleanup()

def callback(gpio_pin):
  if(GPIO.input(gpio_pin) == 1):
    print(gpio_pin)
    GPIO.output(RLED_PIN, GPIO.HIGH)
    ret = subprocess.check_output(cmd, shell=True)
    print(ret)
  else:
    GPIO.output(RLED_PIN, GPIO.LOW)

if __name__ == "__main__":
  main()
