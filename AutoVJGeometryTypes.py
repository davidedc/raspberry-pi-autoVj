#!/usr/bin/env python
# -*- coding: utf-8 -*-


class AutoVJGeometryTypes:
	
	geometries =  []

	
	@staticmethod
	def add(geometry):
		AutoVJGeometryTypes.geometries.append(geometry)

	@staticmethod
	def get(index):
		index = index % len(AutoVJGeometryTypes.geometries)
		return AutoVJGeometryTypes.geometries[index]

	@staticmethod
	def length():
		return len(AutoVJGeometryTypes.geometries)
