#!/usr/bin/env python
# -*- coding: utf-8 -*-


class GeometryTypes(object):
  
  geometries =  []

  @staticmethod
  def add(geometry):
      GeometryTypes.geometries.append(geometry)

  @staticmethod
  def get(index):
    index = index % len(  GeometryTypes.geometries)
    return   GeometryTypes.geometries[index]

  @staticmethod
  def length():
    return len(  GeometryTypes.geometries)
