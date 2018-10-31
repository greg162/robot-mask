Robot Mask
=========

<div class='gfyitem' data-id=AcclaimedEmbarrassedArabianhorse></div><p> <a href="https://gfycat.com/AcclaimedEmbarrassedArabianhorse">See what it looks like here</a></p>


So, you want to dress up as a Robot for halloween? Here is the codebase for a robot mask. It has the following features:

Features
--------

  * Automatic leveling eyes!
  * 3 different eye types to choose from.
  * LED that changes color to match eyes.
  * Eyes that blink! (Press button 7 on your game pad to activate)

Setup
-----

 Here are some instructions for creating your own mask. You'll need:

  * Raspberry Pi
  * ADXL 345 G force Sensor
  * RGB LED
  * A cheap USB game pad
  * A 7 inch LED that can be powered by a 1amp 5V power supply.
  * 2 rechargable USB power supplies (1 for the RPi, 1 for the LED)

Here are some rough setup instructions, other steps might be required.

1. Create a directory in your home directory called _robot_.
2. Enter it, and clone this repository into it.
3. Install pygame, this can be done with the command `sudo apt-get install python-pygame` via the terminal.
4. Setup I2C (this can be a pain in the butt, these instructions should get you going, but Google is your friend here).
  1. Install Python smbus `sudo apt-get install -y python-smbus`.
  2. Install python i2c tools `sudo apt-get install -y i2c-tools`.
  3. Run `sudo raspi-config` go to _Interfacing Options_ then _I2C_ and enable it.
5. This is the fun bit! Time to start wiring. You can find the wiring diagram here: https://easyeda.com/greg162/pi-bot-helmet
6. Hook up all the other components.
7. Go to the terminal navigate to the face directory `cd robot` then run `python main.py`
8. With a bit of luck, you should now have the face displaying on your monitor.





