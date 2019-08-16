#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from ev3dev2.sensor.lego import ColorSensor
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from sys import stderr
from time import sleep

brick.sound.file(SoundFile.HELLO)

cl = ColorSensor()

cl.mode='COL-AMBIENT'

brick.sound.file(SoundFile.HELLO)

while True: 
    print(cl.ambient_light_intensity, end=' ', file = stderr)
    #    print(cl.reflected_light_intensity, end=' ', file = stderr)
    sleep(1)
