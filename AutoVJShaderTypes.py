#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pi3d

class AutoVJShaderTypes:
	
	# the palette names are just indexes into a table
	dots =  0
	stripes =  1
	gradient =  2
	flat =  3
	shadersTable = []

	def __init__(self):
		AutoVJShaderTypes.shadersTable = [
			pi3d.Shader('./autoVJ/shaders/mat_dots_color'),
			pi3d.Shader('./autoVJ/shaders/mat_grad_color'),
			pi3d.Shader('./autoVJ/shaders/mat_stripe_color'),
		]

	
