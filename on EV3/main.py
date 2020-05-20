#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
#from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
import secrets
import airtable

# Write your program here
ev3 = EV3Brick()
ev3.speaker.beep()
motorA=Motor(Port.A)

while True:

   voice_command = airtable.Get_AT("Table 1","Name")
   print(voice_command)
   if voice_command=="Class 1: Open":
       motorA.run(50)
   elif voice_command=="Class 2: Close":
       motorA.stop()
   else:
       pass

   wait(100)


'''
By calling Get_AT, you will receive the name of the most likely sound, after you've trained your model.
Use conditional statements (think "if the sound is _____, then do ____") to move your dog. 
Don't forget to put your APIKey and your Tag!
'''
