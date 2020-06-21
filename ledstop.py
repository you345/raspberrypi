# -*- coding: utf-8 -*-
#!/usr/bin/env python

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)

GPIO.output(37, False)

GPIO.cleanup()
