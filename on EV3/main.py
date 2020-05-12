#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import math
import ubinascii, ujson, urequests, utime
import airtable
brick.sound.beep()   
Sound = airtable.Get_AT("Table 1","Name")
print(Sound)

'''
By calling Get_AT, you will receive the name of the most likely sound, after you've trained your model.
Use conditional statements (think "if the sound is _____, then do ____") to move your dog. 
Don't forget to put your APIKey and your Tag!
'''
