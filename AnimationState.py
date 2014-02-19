#!/usr/bin/env python
# -*- coding: utf-8 -*-


from random import randrange, uniform
import time

class AnimationState(object):
  
  millis = int(round(time.time() * 1000))
  frameCount = 0
  millisDelta = 0
  
  # the state is stored in 3-dim array where
  # the first element defines the affected part of the drawing
  # the second is the aspect being defined
  # the third is the quality of the aspect
  
  # initialise all to zero
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

  # midgroundGeometryType # cube, multiple cubes, random lines, random polygons, voronoy...
  # midgroundGeometryScale # small, mid, large
  # midgroundGeometryAnimationType # smooth spin, wobble, noise...
  # midgroundGeometryAnimationSpeed # halt, slow, mid, fast

  # midgroundShaderType # stripes, solid, dots, gradient
  # midgroundShaderScale # small, mid, large
  # midgroundShaderAnimationType # wobble, noise
  # midgroundShaderAnimationSpeed # halt, slow, mid, fast

  # midgroundPaletteType # b/w...
  # no palette scale
  # midgroundPaletteAnimationType # cross-fade, wobble, noise
  # midgroundPaletteAnimationSpeed # halt, slow, mid, fast

  def randomiseOne(self):
    dim1 = randrange(0, 3)
    dim2 = randrange(0, 3)
    dim3 = randrange(0, 6)
    self.state[dim1][dim2][dim3] = uniform(0,11)
  
  def updateTimeAndFrameCount(self):
    curTime = int(round(time.time() * 1000))
    self.millisDelta = int(curTime - self.millis)
    self.millis = curTime
    self.frameCount += 1
    
  
  # you can also make a method to undo / redo
  # you can make a method to mark one or two states and periodically
  # go back to those
 
