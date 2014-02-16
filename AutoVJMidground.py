#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from AutoVJGeometryTypes import AutoVJGeometryTypes
from AutoVJAnimationState import AutoVJAnimationState

class AutoVJMidground:
	
		
	def draw(self, autoVJAnimationState):
		# get the right geometry based on the state
		# and invoke the draw command on it.
		AutoVJGeometryTypes.get(			
				# the index of the geometry type is
				# stored in a particular element of
				# the state matrix, go fetch it
				# also take the floor because it
				# can be an arbitrary float
				int(math.floor(
					autoVJAnimationState.state
						[AutoVJAnimationState.midground]
						[AutoVJAnimationState.geometry]
						[AutoVJAnimationState.theType]
				))
				# modulo the value so one can never
				# reference an unexisting geometry
				% AutoVJGeometryTypes.length()
			).draw(autoVJAnimationState)
 
