#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import randrange, uniform
import time

from Presets import preset

class AnimationState(object):
  
  millis = int(round(time.time() * 1000))
  frameCount = 0
  millisDelta = 0
  
  # the state is stored in 3-dim array where
  # the first element defines the affected part of the drawing
  # the second is the aspect being defined
  # the third is the quality of the aspect
  
  # initialise all to zero (overwritten in __init__)
  # note that if you use this nested way of defining matrixes,
  # the first index length goes last and the last index length goes first.
  state = [[[0 for i in range(6)] for j in range(3)] for k in range(3)]

  # affected part of the drawing
  background =  0
  midground = 1
  foreground = 2
  
  # aspect being defined
  geometry = 0
  shader = 1
  palette = 2
  
  # quality of the aspect
  theType = 0
  scale = 1
  animationType = 2
  animationSpeed = 3
  petalSmooth = 4 # value passed to shader controls either petals or smoothing
  powerRing = 5 # exponent of atan() function or ring multiplier

  """
  [][0][1] scale is 1 + this value % 5, background alway 20.0
  [][0][2] spinZ, spinX, spinY, spinZSpinX, spinXSpinYSpinZ, noise
  [][0][3] backfast, backmid, backslow, halt, slow, mid, fast

  [][1][0] index of ShaderTypes.shadersTable: dot, rings, gradient, stripe
  [][1][1] scale multiplier for dots, rings, stripes
  [][1][4] petals for dot, smoothing for ring 0-7 increases both
  [][1][5] formula exponent for dot shader. 0-3 petals grow from middle
            4-5 circular dots 6-10 shard pattern. For ring shader this
            controls the number of rings

  [1][2][0] index PaletteTypes.paletteTable 45 entries NB on midgound used
  [][2][1] inverts palletteEntry colours if odd value
  [][2][2] colour change every 8 frames just for one frame
            0 -> swap
            1 -> 8th frame halve, 4th frame double rgb values
            2 -> randomise rgb values
            3 -> flash, col1 and col2 to white
  """

  def randomiseOne(self):
    dim1 = randrange(0, 3)
    dim2 = randrange(0, 3)
    dim3 = randrange(0, 6)
    self.state[dim1][dim2][dim3] = uniform(0, 147)
  
  def updateTimeAndFrameCount(self):
    curTime = int(round(time.time() * 1000))
    self.millisDelta = int(curTime - self.millis)
    self.millis = curTime
    self.frameCount += 1

  def jumpToPreset(self, num=0):
    num = (num - 1) % len(preset)
    for i in range(2):
      for j in range(3):
        for k in range(6):
          if preset[num][i][j][k] != None: #i.e. only overwrite part of state with values not None
            self.state[i][j][k] = preset[num][i][j][k]
  
  # you can also make a method to undo / redo
  # you can make a method to mark one or two states and periodically
  # go back to those
 
  def __init__(self):
    self.jumpToPreset(num=0)
    self.jumpToPreset(num=1)

