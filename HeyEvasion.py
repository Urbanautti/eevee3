#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor.lego import InfraredSensor
from sys import stderr
from time import sleep 

pariliike = MoveTank(OUTPUT_A, OUTPUT_B)
ir = InfraredSensor()
# proximity value of 40 equals 30 cm (JUST SO YOU KNOW)
brick.sound.file(SoundFile.HELLO)
while True:
    pariliike.on_for_seconds(30,30,0.4)
    distance = ir.proximity
    if distance<= 25:
        print('Deploy evasive maneuvers!', end=' ')
        sleep(0.5)
        pariliike.on_for_seconds(-20,-20,3)
        pariliike.on_for_seconds(-50,50,4)
        brick.sound.file(SoundFile.T_REX_ROAR)
        break 
