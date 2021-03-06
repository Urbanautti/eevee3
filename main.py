#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B


# Write your program here
brick.sound.file(SoundFile.HELLO)
# Moottorit
#vasen = Motor(Port.A, Direction.COUNTERCLOCKWISE)
#oikea = Motor(Port.B, Direction.COUNTERCLOCKWISE)
pariliike = MoveTank(OUTPUT_A, OUTPUT_B)
#vasen.run_time(300, 5000)
#oikea.run_time(300, 5000)
#pariliike.on_for_rotations(left_speed=30, right_speed=60, rotations=5)
pariliike.on_for_seconds(20,20,2)
pariliike.on_for_seconds(50,0,2)
pariliike.on_for_seconds(75,75,1)
pariliike.on_for_seconds(0,50,2)
pariliike.on_for_seconds(75,75,2)
pariliike.on_for_seconds(0,50,2)
pariliike.on_for_seconds(75,75,2)
pariliike.on_for_seconds(0,50,2)
pariliike.on_for_seconds(75,75,2)
pariliike.on_for_seconds(0,50,2)
pariliike.on_for_seconds(75,75,1)
pariliike.on_for_seconds(-50,50,1)
brick.sound.file(SoundFile.T_REX_ROAR)

# Toinen idea steeringin kautta
# steering_pari = 