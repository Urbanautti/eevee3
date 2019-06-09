#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from ev3dev2.sensor.lego import InfraredSensor
from sys import stderr
from time import sleep 

ir = InfraredSensor()

brick.sound.file(SoundFile.HELLO)
while True:
    for i in range(10):
        # try replacin with ir.heading()
        # or ir.heading_and_distance()
        distance = ir.proximity
        if distance==None:
            # distance() returns None if no beacon detected 
            print('Beacon offline?', end=' ')
            print('Beacon offline?', end=' ', file=stderr)
        else:
            # print to EV3 LC screen
            # print a space instead of starting a new line 
            print(distance, end=' ')
            # print to VS Code output panel 
            print(distance, end=' ', file=stderr)
        sleep(0.5)
print('')  #start new line on EV# screen
print('', file=stderr) # start new line VS code    

