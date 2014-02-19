Raspberry-pi-autoVj
===================

Automatic motion graphics for Raspberry pi using pi3d framework.

Either download pi3d https://github.com/tipam/pi3d into a directory in your
/home/pi directory or install it using the alternative methods outlined
here: http://pi3d.github.io/html/ReadMe.html You can add this project anywhere
convenient there is a demo.py file that 'points' to the pi3d directory
which you might need to alter if you did anything non-standard.

Then run Geany (Programming -> Geany) load the file  AutoVJ.py and press the
"gears" icon to run.

Press esc to exit.

Press space to 'bump' the random effect changer.

AutoVJ works by simply modifying the properties of two primitives (a cube
and a background plane). Properties can be: the shader, the scale of the
shader, the scale of the object, the rotation speed, the palette. Some
extra effects kick-in randomly such as flashing, inverting the colors,
and changing the orientation of the gradients.

Status of code: the code was using for prototyping something else, so you'll
see a lot of weird code in weird places doing nothing.

http://www.youtube.com/watch?v=NLW30kXaIkA
