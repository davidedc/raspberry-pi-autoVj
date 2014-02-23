#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pi3d

class ShaderTypes(object):
  
  # the palette names are just indexes into a table
  dots = 0
  rings = 1
  stripes = 2
  gradient = 3

  shadersTable = []
  petalTable = []
  powerTable = []

  def __init__(self):
    ShaderTypes.shadersTable = [
      pi3d.Shader('shaders/mat_dots_color'),
      pi3d.Shader('shaders/mat_rings_color'),
      pi3d.Shader('shaders/mat_grad_color'),
      pi3d.Shader('shaders/mat_stripe_color'),
      pi3d.Shader('shaders/mat_noise_color')
   ]
    
    ShaderTypes.petalTable = [0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35]
    ShaderTypes.powerTable = [-2.0, -1.5, -1.02, -0.1, -0.000, 0.000, 0.02, 0.1, 1.0, 1.4, 3.0]
