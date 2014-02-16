#!/usr/bin/python
from __future__ import absolute_import, division, print_function, unicode_literals
""" A very simple gradient-colored cube and a simple solid colored box """
import demo
import pi3d
import threading
import time
import sys
import re
import math

from AutoVJBackground import AutoVJBackground

from pi3d.shape.Canvas import Canvas
from pi3d.util.String import String
from pi3d.util.Ttffont import Ttffont
from AutoVJAnimationState import AutoVJAnimationState
from AutoVJGeometryTypeSimpleCube import AutoVJGeometryTypeSimpleCube
from AutoVJMidground import AutoVJMidground
from AutoVJShaderTypes import AutoVJShaderTypes

counter = [None]*5
artist = [""] * 1
title = [""] * 1
counter[0] = 0




def checkLastRecResult(counter, artist, title):
	while True:
		counter[0] = counter[0] + 1
		sys.stderr.write("hello from thread" + str(counter[0]))

		#txt='{"matches":[{"key":"Xz5UTjcmsakF4B+eJjAHdew/zwlpxKxCKn6XkYo9KqHuPvQ8gRTPk49dR86iIg==","metadata":{"title":"Punching In A Dream","artist":"The Naked And Famous"},"type":"music"}]}'
		#txt = open('./autoVJ/lastRecognitionResponse.txt','r').read()
		txt = ''

		re1='("title")' # Double Quote String 1
		re2=':' # Any Single Character 1
		re3='"(.*?)"' # Double Quote String 2

		re4='("artist")' # Double Quote String 1
		re5=':' # Any Single Character 1
		re6='"(.*?)"' # Double Quote String 2

		rg = re.compile(re1+re2+re3,re.IGNORECASE|re.DOTALL)
		m = rg.search(txt)
		if m:
			#string1=m.group(1)
			string2=m.group(2)
			#sys.stderr.write(string1)
			sys.stderr.write(string2)
			title[0] = string2

		rg = re.compile(re4+re5+re6,re.IGNORECASE|re.DOTALL)
		m = rg.search(txt)
		if m:
			#string1 = m.group(1)
			string2 = m.group(2)
			#sys.stderr.write(string1)
			sys.stderr.write(string2)
			artist[0] = string2

		time.sleep(5)


thr = threading.Thread(target=checkLastRecResult, args = (counter,artist, title))
thr.daemon = True #allows the program to exit even if a Thread is still running
thr.start()


#DISPLAY = pi3d.Display.create(x=100, y=100)
DISPLAY = pi3d.Display.create()
#shader = pi3d.Shader("shaders/star")
tex = pi3d.Texture("./autoVJ/textures/emptyPNG8bit.png")
#shaderFlat = pi3d.Shader('shaders/mat_grad_color')
#shaderFlat = pi3d.Shader('shaders/mat_stripe_color')

# initiliase the shadrs and put them in a table
# note that the shaders have to be initialised after
# the display has been created.
AutoVJShaderTypes()
shaderFlat = AutoVJShaderTypes.shadersTable[0]
#canvShader = pi3d.Shader('shaders/2d_grad')

#box = pi3d.Cuboid(x=0, y=0, z=2.2)
#box = pi3d.Cuboid(w=100, h=100, d=100, x=0, y=0, z=100.0)
#box.set_draw_details(shaderFlat,[tex],1.0,0.1)
# unfortunately alpha doesn't seem to work
#box.set_material((1.0,0,0,0.1))


mykeys = pi3d.Keyboard()

ASPECT = DISPLAY.width / DISPLAY.height

perspectiveCamera = pi3d.Camera((0,0,0), (0,0,-0.1), (1, 1000, 45, ASPECT), is_3d=True)

box = AutoVJGeometryTypeSimpleCube(perspectiveCamera, tex)
background = AutoVJBackground(perspectiveCamera, shaderFlat, tex)

artistBackgroudShapeHeight = 100
artistOffsetFromTop = 200
titleBackgroudShapeHeight = 100
titleOffsetFromTop = 80

artistYPosition = (DISPLAY.height/2 - artistBackgroudShapeHeight/2) - titleOffsetFromTop
artistBackgroudShape = pi3d.Cuboid( w = 1, h=artistBackgroudShapeHeight, d=100, y=artistYPosition, z=100.0)
artistBackgroudShape.set_draw_details(shaderFlat,[tex],1.0,0.1)
artistBackgroudShape.set_material((1.0,0,0,0.1))

titleYPosition = (DISPLAY.height/2 - titleBackgroudShapeHeight/2) - artistOffsetFromTop
titleBackgroudShape = pi3d.Cuboid( w = 1, h=titleBackgroudShapeHeight, d=100, y=titleYPosition, z=100.0)
titleBackgroudShape.set_draw_details(shaderFlat,[tex],1.0,0.1)
titleBackgroudShape.set_material((1.0,0,0,0.1))

rad = 100.0/math.sqrt(3.0/4.0)

artistBackgroudEdgeShape = pi3d.Cone(radius= rad/2.0, height=100, sides=24, name="Cone",
        y=artistYPosition, z=100.0)
artistBackgroudEdgeShape.set_draw_details(shaderFlat,[tex],1.0,0.1)
artistBackgroudEdgeShape.set_material((1.0,0,0,0.1))

titleBackgroudEdgeShape = pi3d.Cone(radius= rad/2.0, height=100, sides=24, name="Cone",
        y=titleYPosition, z=100.0)
titleBackgroudEdgeShape.set_draw_details(shaderFlat,[tex],1.0,0.1)
titleBackgroudEdgeShape.set_material((1.0,0,0,0.1))


ortographicCamera = pi3d.Camera(is_3d=False)

#load ttf font and set the font colour to 'raspberry'
flatsh = pi3d.Shader("./autoVJ/shaders/uv_flat")
arialFont = Ttffont("./autoVJ/fonts/Roboto-BoldItalic.ttf", "#dd00aa")

autoVJAnimationState = AutoVJAnimationState()
autoVJMidground = AutoVJMidground()

writeState = 0 # waiting / sliding in / blink-in / showing / blinkout / sliding out


startSlideInMs = 0
startBlinkInMS = 0
startShowInMS = 0
startBlinkOutMS = 0
startSlideOutMS = 0

previousArtist = ""
previousTitle = ""

while DISPLAY.loop_running():

  autoVJAnimationState.updateTimeAndFrameCount()
  autoVJAnimationState.randomiseOne()
  background.draw(autoVJAnimationState)
  autoVJMidground.draw(autoVJAnimationState)

  theArtist = artist[0].upper()
  theTitle = title[0].upper()
  if (previousArtist != theArtist or previousTitle != theTitle)and writeState == 0:
	  artistBackgroudWidth = 40*(len(theArtist)+2)
	  artistXPosition = -(DISPLAY.width/2 - artistBackgroudWidth/2)
	  artistBackgroudShape.scale(artistBackgroudWidth,1,1)
	  artistString = String(font=arialFont, string=theArtist.upper(),
					  camera=ortographicCamera, z=1.0, is_3d=False) # orthographic view					  
	  artistString.set_shader(flatsh)
	  artistString.position(artistXPosition, artistYPosition, 49)

	  titleBackgroudWidth = 40*(len(theTitle)+2)
	  titleXPosition = -(DISPLAY.width/2 - titleBackgroudWidth/2)
	  titleBackgroudShape.scale(titleBackgroudWidth,1,1)
	  titleString = String(font=arialFont, string=theTitle.upper(),
					  camera=ortographicCamera, z=1.0, is_3d=False) # orthographic view					  
	  titleString.set_shader(flatsh)
	  titleString.position(titleXPosition, titleYPosition, 49)

	  previousArtist = theArtist
	  previousTitle = theTitle
	  writeState = 1


  if writeState == 1:
	  if startSlideInMs == 0:
		  startSlideInMs = autoVJAnimationState.millis
	  slideTime = autoVJAnimationState.millis - startSlideInMs
	  slideTimeRemaining = 250 - slideTime
	  if slideTimeRemaining <= 0:
		  slideTimeRemaining = 0
		  writeState = 2
		  startBlinkInMS = 0
	  artistBackgroudShape.positionX(artistXPosition - slideTimeRemaining * 2)
	  artistBackgroudEdgeShape.positionX((artistXPosition + artistBackgroudWidth/2) - slideTimeRemaining * 2)
	  titleBackgroudShape.positionX(titleXPosition - slideTimeRemaining * 2)
	  titleBackgroudEdgeShape.positionX((titleXPosition + titleBackgroudWidth/2) - slideTimeRemaining * 2)

  if writeState == 2:
	  if startBlinkInMS == 0:
		  startBlinkInMS = autoVJAnimationState.millis
	  blinkInTime = autoVJAnimationState.millis - startBlinkInMS
	  blinkInTimeRemaining = 250 - blinkInTime
	  if blinkInTimeRemaining <= 0:
		  startBlinkInMS = 0
		  writeState = 3
	  if autoVJAnimationState.frameCount % 3 == 0:
		artistString.draw(camera=ortographicCamera)
		titleString.draw(camera=ortographicCamera)

  if writeState == 3:
	  if startShowInMS == 0:
		  startShowInMS = autoVJAnimationState.millis
	  showTime = autoVJAnimationState.millis - startShowInMS
	  showTimeRemaining = 3000 - showTime
	  if showTimeRemaining <= 0:
		  startShowInMS = 0
		  writeState = 4
		  startBlinkOutMS = 0
	  artistString.draw(camera=ortographicCamera)
	  titleString.draw(camera=ortographicCamera)

  if writeState == 4:
	  if startBlinkOutMS == 0:
		  startBlinkOutMS = autoVJAnimationState.millis
	  blinkOutTime = autoVJAnimationState.millis - startBlinkOutMS
	  blinkOutTimeRemaining = 250 - blinkOutTime
	  if blinkOutTimeRemaining <= 0:
		  startBlinkOutMS = 0
		  writeState = 0
		  startSlideInMs = 0
	  if autoVJAnimationState.frameCount % 3 == 0:
		artistString.draw(camera=ortographicCamera)
		titleString.draw(camera=ortographicCamera)

  if writeState == 1 or writeState == 2 or writeState == 3 or writeState == 4:
	  artistBackgroudShape.draw(camera=ortographicCamera)
	  artistBackgroudEdgeShape.rotateToZ(180)
	  artistBackgroudEdgeShape.draw(camera=ortographicCamera)
	  titleBackgroudShape.draw(camera=ortographicCamera)
	  titleBackgroudEdgeShape.rotateToZ(180)
	  titleBackgroudEdgeShape.draw(camera=ortographicCamera)
	  

  theKey = mykeys.read()
  if theKey == 27: # esc
    mykeys.close()
    DISPLAY.destroy()
    break
  elif theKey == 32: # space
    pi3d.screenshot("./autoVJ/screenshots/" + str(autoVJAnimationState.frameCount)+".png")
