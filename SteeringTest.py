#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color, SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase
from ev3dev2.motor import MoveSteering, OUTPUT_A, OUTPUT_B

# Write your program here
brick.sound.file(SoundFile.FANFARE)
# Toinen idea steeringin kautta
steering_pari = MoveSteering(OUTPUT_A,OUTPUT_B)
steering_pari.on_for_rotations(steering=-20, speed=-75, rotations=10)
brick.sound.file(SoundFile.STOP)

