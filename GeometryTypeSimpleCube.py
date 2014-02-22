#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pi3d
import sys

from Geometry import Geometry
from GeometryTypes import GeometryTypes
from PaletteTypes import PaletteTypes
from ShaderTypes import ShaderTypes
from random import uniform

class GeometryTypeSimpleCube(Geometry):

  def __init__(self, camera):
    super(GeometryTypeSimpleCube, self).__init__(camera, pi3d.Cuboid(w=50, h=50, d=50, x=0, y=0, z=200.0))

