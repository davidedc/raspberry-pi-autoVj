#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals
""" A very simple gradient-colored cube and a simple solid colored box """
import demo
import pi3d
import threading
import time
import sys
import re
import math

from Background import Background

from AnimationState import AnimationState
from GeometryTypeSimpleCube import GeometryTypeSimpleCube
from Midground import Midground
from ShaderTypes import ShaderTypes

counter = [None]*5
counter[0] = 0

DISPLAY = pi3d.Display.create(frames_per_second=30)

ShaderTypes()

mykeys = pi3d.Keyboard()

perspectiveCamera = pi3d.Camera(is_3d=True)
ortographicCamera = pi3d.Camera(is_3d=False)

box = GeometryTypeSimpleCube(perspectiveCamera)
background = Background(perspectiveCamera)

animation_state = AnimationState()
midground = Midground()

writeState = 0 # waiting / sliding in / blink-in / showing / blinkout / sliding out
startSlideInMs = 0
startBlinkInMS = 0
startShowInMS = 0
startBlinkOutMS = 0
startSlideOutMS = 0

while DISPLAY.loop_running():

  animation_state.updateTimeAndFrameCount()
  if (animation_state.frameCount % 10) == 0:
    animation_state.randomiseOne()
  midground.draw(animation_state)
  background.draw(animation_state)

  theKey = mykeys.read()
  if theKey == 27: # esc
    mykeys.close()
    DISPLAY.destroy()
    break
  elif theKey == 32: # space
    #pi3d.screenshot("screenshots/" + str(animation_state.frameCount)+".png")
    #try to debug occasional cube disappearance
    s = animation_state.state[1]
    print("scale={:4.2f} spin_type={:4.2f} speed={:4.2f}".format(s[0][1] % 5, s[0][2] % 6, s[0][3] % 7))
    print("shader={:4.2f} dotscale={:4.2f} petal={:4.2f} power={:4.2f} cols={:4.2f}".format(s[1][0] % 5, s[1][1], s[1][4] % 8, s[1][5] % 11, s[2][0]))
  elif theKey >= 48 and theKey <= 57:
    animation_state.jumpToPreset(theKey - 48)
