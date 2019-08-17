# EV3-project

## Battery situation

* We burned first set of batteries on 8.6.2019, expenses even to both parties.
* Second set of batteries now in use, cost by Zeick. (It's quite frustrating how quickly the voltage drops 😢)
* Current set of batteries (as of 26.07.2019) is still functional)
* Next set of batteries will be provided by Urbanautti.

<<<<<<< HEAD
## 16.8.2019 

We had a success with trying out the color sensor with another mode. We tested the sensors COL-AMBIENT mode which measures the intesity of surrounding light.

Although the figure for a normally lit room varies between 1 and 2 in the sensor readings, the sensor is able to distinguish between dark and bright. 

We ran a test, where the "Eevee" robot unit ran in a bright environment with both engines running, if the run became dark the unit stopped and rotated around 360 degrees. 

The aforementioned test was a success. 

**NOTE**! The color sensor has different led colors. In COL-REFLECT the led is red and in COL-AMBIENT mode the led is blue 
=======
## 16.8.2019

We did something... but what? 🤔
>>>>>>> 2503002f4d492e7440d09470a0aeb94f0a35eb1c

## 25-26.7.2019

We ran a successful trial with the EV3 color sensor in COL-REFLECT mode. We removed the [Inception](https://www.imdb.com/title/tt1375666/) soundbyte file from the working directory (at last), since it was being again and again reuploaded to the brick. 

The trial run using the color sensor was measuring the levels of light intensity correctly. The device returns a number 0-100 corresponding to the percentage of light reflected back to detector. We got around 98 on shiny yellow/white surface, 80 on nonshiny yellow/white surface and 20 on shiny black surface.

During the next part, we will test the COL-AMBIENT and COL-COLOR modes of the sensor.

**NOTE! LEST WE FORGET!** The procedure for printing the data on the VSC terminal panel requires we specify the output as [standard error stream](https://en.wikipedia.org/wiki/Standard_streams), or stderr in short. This is achieved by

```python
print(cl.reflected_light_intensity, end=' ', file = stderr)
```

This is used in [HeyColor.py](HeyColor.py).

**SECOND NOTE!** Upon checking EV3 page for instructions make sure you have the instruction for the _matching_ version of Python. For example, today we used [sensor manual](https://sites.google.com/site/ev3devpython/learn_ev3_python/using-sensors).

## 8.6.2019
We are using [EV3 Python 2 manual (using motors)](https://sites.google.com/site/ev3devpython/learn_ev3_python/using-motors) as a useful resource.
We have finally removed the old soundbyte files from the EV3 brick.
We were able to incorporate the infrared proximity sensor to the eevee chassis.
After a myriad of trial-and-error test runs, we were able to get the the eevee robot to react and respond to obstacles. 

Notes: Proximity of 40 is 30 cm, the EV3 brick needs to be connected and visual code rebooted to make connection. 

Suggestions have been made to incorporate the pressure sensor for a "Secondary protocol program".  

## 26.5.2019
Both participants are at an equipoise with their python course
Also we have agreed that the next eevee3 run will add a distance sensor input to the existing program script. 

## 19.5.2019
We managed to get the robot move a square. In the future we will apply sensor data.

