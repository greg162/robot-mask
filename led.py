#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

class Led:

def __init__(self):

  self.pins = {'pin_R':11, 'pin_G':12, 'pin_B':13}  # pins is a dict

  GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
  for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)   # Set pins' mode is output
    GPIO.output(pins[i], GPIO.HIGH) # Set pins to high(+3.3V) to off led

  self.p_R = GPIO.PWM(pins['pin_R'], 2000)  # set Frequece to 2KHz
  self.p_G = GPIO.PWM(pins['pin_G'], 2000)
  self.p_B = GPIO.PWM(pins['pin_B'], 5000)

  self.p_R.start(0)      # Initial duty Cycle = 0(leds off)
  self.p_G.start(0)
  self.p_B.start(0)

def map(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setColor(col):   # For example : col = 0x112233
  R_val = (col & 0xFF0000) >> 16
  G_val = (col & 0x00FF00) >> 8
  B_val = (col & 0x0000FF) >> 0
	
  R_val = map(R_val, 0, 255, 0, 100)
  G_val = map(G_val, 0, 255, 0, 100)
  B_val = map(B_val, 0, 255, 0, 100)
	
  self.p_R.ChangeDutyCycle(R_val)     # Change duty cycle
  self.p_G.ChangeDutyCycle(G_val)
  self.p_B.ChangeDutyCycle(B_val)

def stop():
  self.p_R.stop()
  self.p_G.stop()
  self.p_B.stop()
  for i in self.pins:
    GPIO.output(self.pins[i], GPIO.HIGH)    # Turn off all leds
  GPIO.cleanup()




