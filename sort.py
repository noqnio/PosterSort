#!/usr/bin/python

import os
import colorsys
import sys
from PIL import Image

meanHSV = []

for (path, dirs, files) in os.walk(sys.argv[1]):
    for fname in files:
        if fname.endswith(('.jpg', '.png')):
            im = Image.open(fname)
            meanRGB = [(float(sum(list(im.getdata(channel)))) / len(list(im.getdata(channel))))/255 for channel in range(3)]
            meanHSV.append([colorsys.rgb_to_hsv(meanRGB[0],meanRGB[1],meanRGB[2]),fname])

meanHSV.sort()
print '\n'.join([q[1] for q in meanHSV])
