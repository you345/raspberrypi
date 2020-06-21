from LCD import LCD
import time, sys
import commands
#import RPi.GPIO as GPIO

# https://github.com/sterlingbeason/LCD-1602-I2C

lcd = LCD(2,0x27,True)

lcd.message("Hello World!", 1) # display 'Hello World!' on line 1 of LCD
time.sleep(5.0)

myip = commands.getoutput('hostname -I')
lcd.message(str(myip), 1) # display 'my ipaddr' on line 1 of LCD

while True:
  try:
    res = commands.getoutput('date "+%H:%M:%S %m/%d"')
    lcd.message(str(res), 2) # display 'Hello World!' on line 1 of LCD
    time.sleep(0.1)
  except KeyboardInterrupt:
    break

lcd.clear() # clear LCD display
#GPIO.cleanup()
sys.exit()
