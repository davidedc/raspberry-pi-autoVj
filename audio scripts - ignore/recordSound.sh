#!/bin/bash
arecord -D plughw:0,0 -q -c 1 -r 16000 --duration=5 -f S16_LE -t raw foo.raw
