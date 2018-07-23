#!/bin/bash

screenfetch -N -n > ~/.dominae/screenfetch.txt
convert -size 2000x2000 -channel RGBA -background none -trim -bordercolor none -border 3 -fill grey -font San-Francisco-Display-Bold caption:@.dominae/screenfetch.txt ~/.dominae/screenfetch.png