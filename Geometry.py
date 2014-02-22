#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pi3d
import sys

from   GeometryTypes import   GeometryTypes
from   PaletteTypes import   PaletteTypes
from   ShaderTypes import   ShaderTypes
from random import uniform

class Geometry(object):
  """ Background and GeometryTypeSimpleCube inherit from this
  """
  geometry = None
  cameraToUse = None
  shaderFlat = None
  tex = None

  def __init__(self, camera, geometry, fground=True):
    self.cameraToUse = camera
    self.geometry = geometry
    self.geometry.set_material((1.0, 0.0, 0.0))
    self.fground = fground
    # add myself to the list of geometries so I can be picked
    # for drawing
    GeometryTypes.add(self)
    
  def draw(self, ani_state):
    geometry = self.geometry # little shortcut
    fground = self.fground
    if fground:
      state_part = ani_state.midground
    else:
      state_part = ani_state.background
    speedType = (int(
        ani_state.state[state_part][ani_state.geometry][ani_state.animationSpeed]
        )) % 7 # backfast, backmid, backslow, halt, slow, mid, fast
    speedMillisDivider = 1.0
    if speedType == 0:
      speedMillisDivider = -1
    elif speedType == 1:
      speedMillisDivider = -10
    elif speedType == 2:
      speedMillisDivider = -100
    elif speedType == 3:
      speedMillisDivider = -100000
    elif speedType == 4:
      speedMillisDivider = 100
    elif speedType == 5:
      speedMillisDivider = 10
    elif speedType == 6:
      speedMillisDivider = 1
    animationSpeed = ani_state.millisDelta / speedMillisDivider
    if not fground:
      # the background should move slower to give a parallax effect
      animationSpeed /= 50

    animationType = (int(
        ani_state.state[state_part][ani_state.geometry][ani_state.animationType]
        )) % 6 # spinZ, spinX, spinY, spinZSpinX, spinXSpinYSpinZ, noise
    if animationType == 0:
      geometry.rotateIncZ(animationSpeed)
    elif animationType == 1:
      geometry.rotateIncX(animationSpeed)
    elif animationType == 2:
      geometry.rotateIncY(animationSpeed)
    elif animationType == 3:
      geometry.rotateIncZ(animationSpeed)
      #if fground:
      geometry.rotateIncX(animationSpeed)
    elif animationType == 4:
      #if fground:
      geometry.rotateIncX(animationSpeed)
      geometry.rotateIncY(animationSpeed)
      geometry.rotateIncZ(animationSpeed)
    elif animationType == 5:
      #if fground:
      geometry.rotateIncX(animationSpeed * uniform(-1, 1))
      geometry.rotateIncY(animationSpeed * uniform(-1, 1))
      geometry.rotateIncZ(animationSpeed * uniform(-1, 1))

    scale = ani_state.state[state_part][ani_state.geometry][ani_state.scale]
    if fground:
      scale = 1.0 + int(scale % 5) # from 0,10 to 1,5
    else:
      scale = 15.0 + int(scale % 5)
    geometry.scale(scale, scale, scale)

    shaderType = (int(
        ani_state.state[state_part][ani_state.shader][ani_state.theType]
        )) % len(ShaderTypes.shadersTable)
    shader = ShaderTypes.shadersTable[shaderType]
    geometry.set_shader(shader)


    # use the palette scale to invert the colors
    paletteInvert = (int(
        ani_state.state[state_part][ani_state.palette][ani_state.scale]
        )) % 2
    paletteEntry =   PaletteTypes.paletteTable[
      (int(
        ani_state.state[ani_state.midground][ani_state.palette][ani_state.theType]
        )) % len(PaletteTypes.paletteTable)]
    col1 = [paletteEntry[0][0], paletteEntry[0][1], paletteEntry[0][1]]
    col2 = [paletteEntry[1][0], paletteEntry[1][1], paletteEntry[1][1]]
    if paletteInvert:
      col1,col2 = col2,col1

    # goes from 0 to 5, only the first four do something
    # swap, shades, random, flash
    paletteAnimationType = (int(
        ani_state.state[state_part][ani_state.palette][ani_state.animationType]
        )) % 6 # i.e. if 4, 5 will have no effect
    if paletteAnimationType == 0:
      if ani_state.frameCount % 8 == 0:
        col1,col2 = col2,col1
    elif paletteAnimationType == 1:
      if ani_state.frameCount % 8 == 0:
        col1[0] = col1[0]*2
        col1[1] = col1[1]*2
        col1[2] = col1[2]*2
        col2[0] = col2[0]/2
        col2[1] = col2[1]/2
        col2[2] = col2[2]/2
      elif ani_state.frameCount % 8 == 4:
        col1[0] = col1[0]/2
        col1[1] = col1[1]/2
        col1[2] = col1[2]/2
        col2[0] = col2[0]*2
        col2[1] = col2[1]*2
        col2[2] = col2[2]*2
    elif paletteAnimationType == 2:
      if ani_state.frameCount % 8 == 0:
        col1[0] = uniform(0,1)
        col1[1] = uniform(0,1)
        col1[2] = uniform(0,1)
        col2[0] = uniform(0,1)
        col2[1] = uniform(0,1)
        col2[2] = uniform(0,1)
    elif paletteAnimationType == 3:
      if ani_state.frameCount % 8 == 0:
        col1=  [0.9,1.0,1.0]
        col2=  [1.0,0.9,1.0]

    geometry.set_custom_data(48, col1)
    geometry.set_custom_data(51, col2)

    shaderScale = int(ani_state.state[state_part][ani_state.shader][ani_state.scale]) % 10.0
    # with the dots shader, too few dots don't look super-cool, so adjust
    if shaderType == ShaderTypes.dots:
      shaderScale = 2.0 * (10.0 + shaderScale)
      
    i = int(ani_state.state[state_part][ani_state.shader][ani_state.petalSmooth])
    petalSmooth = ShaderTypes.petalTable[i % len(ShaderTypes.petalTable)]

    i = int(ani_state.state[state_part][ani_state.shader][ani_state.powerRing])
    powerRing = ShaderTypes.powerTable[i % len(ShaderTypes.powerTable)]

    geometry.set_custom_data(54, [shaderScale, petalSmooth, powerRing]) # number of stripes etc

    geometry.draw(camera=self.cameraToUse)
 
