#!/usr/bin/python

from __future__ import print_function
import sys
import re
from PIL import Image

"""
Used to display an image generated with bmp_logo tool
in U-Boot source tree.
"""

if len(sys.argv) < 3:
    print('Usage: ./bmpshow.py bmp_logo.h bmp_logo_data.h')
    sys.exit(1)

fname_info = sys.argv[1]
fname_data = sys.argv[2]

lines = open(fname_info, 'r').read()
params = re.findall('(BMP_LOGO_\w*)\s*(\d+)', lines)
params = dict(params)

for key in params:
    params[key] = int(params[key])
    print(key, params[key])

# process palette data
lines = open(fname_data, 'r').read()
data = re.search('bmp_logo_palette.*?{(.*?)};', lines, re.DOTALL)
data = re.sub('\s', '', data.group(1))
palette = [int(v,16) for v in data.split(',') if v]

# process bitmap data
data = re.search('bmp_logo_bitmap.*?{(.*?)};', lines, re.DOTALL)
data = re.sub('\s', '', data.group(1))
bitmap = [int(v,16) for v in data.split(',') if v]

print('palette len', len(palette))
print('bitmap len', len(bitmap))

width = params['BMP_LOGO_WIDTH']
height = params['BMP_LOGO_HEIGHT']
size = (width, height)

#img888 = Image.new('RGB', size)

data = bytearray()
for i,p in enumerate(bitmap):
    color = palette[p-16]
    pixel = ((color&0xf00)>>8, (color&0x0f0)>>4, (color&0x00f))
    # scale 4b depth to 8b
    # just to test the difference in RGB888
    #scaled = tuple(v*16 for v in pixel)
    #img888.putpixel((i%width, i//width), scaled)
    # covert to RGB565
    ored = (pixel[2]<<1 | pixel[1]<<7 | pixel[0]<<12)
    # little endian order
    data.append(ored&0x00ff)
    data.append(ored>>8)

print('bitmap size', len(data))
img = Image.frombytes('RGB', size, buffer(data), 'raw', 'BGR;16')
img.show()
#img888.show()

