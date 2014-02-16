#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pi3d
import sys

from AutoVJPaletteTypes import AutoVJPaletteTypes
from AutoVJShaderTypes import AutoVJShaderTypes
from random import uniform

class AutoVJBackground:
	
	geometry =  None
	cameraToUse = None
	shaderFlat = None
	tex = None

	# return an array of copies of the colors
	def __init__(self,camera1, shaderFlat1, texture):
		self.cameraToUse = camera1
		self.shaderFlat = shaderFlat1
		self.tex = texture
		self.geometry = pi3d.Sprite(w=100, h=100, x=0, y=0, z=100.0)
		sys.stderr.write(str(self.geometry))
		self.geometry.set_draw_details(self.shaderFlat,[self.tex],1.0,0.1)
		# unfortunately alpha doesn't seem to work
		self.geometry.set_material((1.0,0,0,0.1))
		
	def draw(self, autoVJAnimationState):
		#geometry = self.geometry
		#geometry.rotateIncZ(1.1)
		#geometry.position(0.0, 0.0, 900.1)
		#geometry.scale(20,20,20)
		#geometry.set_custom_data(48, [1.0,0.0,0.0])
		#geometry.set_custom_data(51, [0.0,0.0,1.0])
		#geometry.set_custom_data(54, [2.0]) # number of stripes
		#geometry.draw(camera=self.cameraToUse)
 		geometry = self.geometry # little shortcut
		speedType = (int(
				autoVJAnimationState.state[autoVJAnimationState.midground][autoVJAnimationState.geometry][autoVJAnimationState.animationSpeed]
				)) % 8 # backfast, backmid, backslow, halt, slow, mid, fast
		speedMillisDivider = 1.0
		if speedType == 0:
			speedMillisDivider = -1
		elif speedType == 1:
			speedMillisDivider = -10
		elif speedType == 2:
			speedMillisDivider = -100
		elif speedType == 3:
			speedMillisDivider = -1000
		elif speedType == 4:
			speedMillisDivider = 1
		elif speedType == 5:
			speedMillisDivider = 10
		elif speedType == 6:
			speedMillisDivider = 100
		animationSpeed = autoVJAnimationState.millisDelta / speedMillisDivider
		# the background should move slower to give a parallax effect
		animationSpeed /= 50

		animationType = (int(
				autoVJAnimationState.state[autoVJAnimationState.midground][autoVJAnimationState.geometry][autoVJAnimationState.animationType]
				)) % 6 # spinZ, spinX, spinY, spinZSpinX, spinXSpinYSpinZ, noise
		if animationType == 0:
			geometry.rotateIncZ(animationSpeed)
		#elif animationType == 1:
			#geometry.rotateIncX(animationSpeed)
		#elif animationType == 2:
			#geometry.rotateIncY(animationSpeed)
		elif animationType == 3:
			geometry.rotateIncZ(animationSpeed)
			#geometry.rotateIncX(animationSpeed)
		elif animationType == 4:
			#geometry.rotateIncX(animationSpeed)
			#geometry.rotateIncY(animationSpeed)
			geometry.rotateIncZ(animationSpeed)
		elif animationType == 5:
			#geometry.rotateIncX(animationSpeed * uniform(-1,1))
			#geometry.rotateIncY(animationSpeed * uniform(-1,1))
			geometry.rotateIncZ(animationSpeed * uniform(-1,1))

		geometry.position(0.0, 0.0, 900.1)

		#scale = autoVJAnimationState.state[autoVJAnimationState.midground][autoVJAnimationState.geometry][autoVJAnimationState.scale]
		#scale = 1 + int(scale%5) # from 0,10 to 1,5
		geometry.scale(20,20,20)

		# the shader type is independent from the midground
		shaderType = (int(
				autoVJAnimationState.state[autoVJAnimationState.background][autoVJAnimationState.shader][autoVJAnimationState.theType]
				))% len(AutoVJShaderTypes.shadersTable)
		shader = AutoVJShaderTypes.shadersTable[shaderType]
		geometry.set_shader(shader)


		# use the palette scale to invert the colors
		paletteInvert = (int(
				autoVJAnimationState.state[autoVJAnimationState.midground][autoVJAnimationState.palette][autoVJAnimationState.scale]
				))% 2
		paletteEntry = AutoVJPaletteTypes.paletteTable[
			(int(
				autoVJAnimationState.state
					[autoVJAnimationState.midground]
					[autoVJAnimationState.palette]
					[autoVJAnimationState.theType]
				))% len(AutoVJPaletteTypes.paletteTable)]
		col1 = paletteEntry[0]
		col2 = paletteEntry[1]
		if paletteInvert:
			col1,col2 = col2,col1

		# goes from 0 to 15, only the first few do something
		# swap, shades, random, flash
		paletteAnimationType = (int(
				1.5 * autoVJAnimationState.state[autoVJAnimationState.midground][autoVJAnimationState.palette][autoVJAnimationState.animationType]
				))
		if paletteAnimationType == 0:
			if autoVJAnimationState.frameCount % 8 == 0:
				col1,col2 = col2,col1
		elif paletteAnimationType == 1:
			if autoVJAnimationState.frameCount % 8 == 0:
				col1[0] = col1[0]/2
				col1[1] = col1[1]/2
				col1[2] = col1[2]/2
				col2[0] = col2[0]/2
				col2[1] = col2[1]/2
				col2[2] = col2[2]/2
			elif autoVJAnimationState.frameCount % 8 == 4:
				col1[0] = col1[0]*2
				col1[1] = col1[1]*2
				col1[2] = col1[2]*2
				col2[0] = col2[0]*2
				col2[1] = col2[1]*2
				col2[2] = col2[2]*2
		elif paletteAnimationType == 2:
			if autoVJAnimationState.frameCount % 8 == 0:
				col1[0] = uniform(0,1)
				col1[1] = uniform(0,1)
				col1[2] = uniform(0,1)
				col2[0] = uniform(0,1)
				col2[1] = uniform(0,1)
				col2[2] = uniform(0,1)
		elif paletteAnimationType == 3:
			if autoVJAnimationState.frameCount % 8 == 0:
				col1=  [1.0,1.0,1.0]
				col2=  [1.0,1.0,1.0]


		geometry.set_custom_data(48, col1)
		geometry.set_custom_data(51, col2)

		shaderScale = int(
				autoVJAnimationState.state[autoVJAnimationState.midground][autoVJAnimationState.shader][autoVJAnimationState.scale]
				)
		# with the dots shader, too few dots don't look super-cool, so adjust
		if shaderType == AutoVJShaderTypes.dots:
			shaderScale = 2*(10+shaderScale)

		geometry.set_custom_data(54, [shaderScale]) # number of stripes

		geometry.draw(camera=self.cameraToUse)

