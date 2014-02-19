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
  if (animation_state.frameCount % 5) == 0:
    animation_state.randomiseOne()
  background.draw(animation_state)
  midground.draw(animation_state)

  theKey = mykeys.read()
  if theKey == 27: # esc
    mykeys.close()
    DISPLAY.destroy()
    break
  elif theKey == 32: # space
    #pi3d.screenshot("screenshots/" + str(animation_state.frameCount)+".png")
    animation_state.randomiseSeveral(40)
