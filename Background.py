#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pi3d
import sys

from Geometry import Geometry
from PaletteTypes import PaletteTypes
from ShaderTypes import ShaderTypes
from random import uniform

class Background(Geometry):

  def __init__(self, camera):
    super(Background, self).__init__(camera,
          pi3d.EnvironmentCube(size=40.0, maptype='FACES'), fground=False)
    #      pi3d.Sprite(w=100, h=100, x=0, y=0, z=100.0), fground=False)
