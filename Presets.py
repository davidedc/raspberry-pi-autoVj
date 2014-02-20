#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
[][0][1] scale is 1 + this value % 5, background alway 20.0
[][0][2] spinZ, spinX, spinY, spinZSpinX, spinXSpinYSpinZ, noise
[][0][3] backfast, backmid, backslow, halt, slow, mid, fast

[][1][0] index of ShaderTypes.shadersTable: dot, rings, gradient, stripe
[][1][1] scale multiplier for dots, rings, stripes
[][1][4] petals for dot, smoothing for ring 0-7 increases both
[][1][5] formula exponent for dot shader. 0-3 petals grow from middle
          4-5 circular dots 6-10 shard pattern. For ring shader this
          controls the number of rings

[1][2][0] index PaletteTypes.paletteTable 45 entries NB on midgound used
[][2][1] inverts palletteEntry colours if odd value
[][2][2] colour change every 8 frames just for one frame
          0 -> swap
          1 -> 8th frame halve, 4th frame double rgb values
          2 -> randomise rgb values
          3 -> flash, col1 and col2 to white
"""

############### geometery       ### shader          ### palette
# 1=>preset[0] 2=>preset[1] etc
preset = [
          [[ [0, 1, 2, 0, 0, 0], [1, 6, 0, 0, 2, 2], [0, 0, 0, 0, 0, 0]],
          [ [0, 2, 4, 4, 0, 0], [0, 1, 0, 0, 4, 4], [6, 0, 2, 0, 0, 0]]],
          
          [[ [0, 1, 5, 0, 0, 0], [2, 6, 0, 0, 0, 4], [0, 0, 3, 0, 0, 0]],
          [ [0, 2, 4, 4, 0, 0], [2, 1, 0, 0, 4, 4], [25, 0, 3, 0, 0, 0]]],
          
          [[ [0, 1, 5, 0, 0, 0], [3, 6, 0, 0, 0, 4], [0, 0, 1, 0, 0, 0]],
          [ [0, 2, 4, 4, 0, 0], [3, 1, 0, 0, 4, 4], [32, 0, 1, 0, 0, 0]]]
        ]
