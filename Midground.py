#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from GeometryTypes import GeometryTypes
from AnimationState import AnimationState

class Midground(object):

  def draw(self, animation_state):
    # get the right geometry based on the state
    # and invoke the draw command on it.
    GeometryTypes.get(      
        # the index of the geometry type is
        # stored in a particular element of
        # the state matrix, go fetch it
        # also take the floor because it
        # can be an arbitrary float
        int(math.floor(
          animation_state.state
            [AnimationState.midground]
            [AnimationState.geometry]
            [AnimationState.theType]
        ))
        # modulo the value so one can never
        # reference an unexisting geometry
        % GeometryTypes.length()
      ).draw(animation_state)
 
