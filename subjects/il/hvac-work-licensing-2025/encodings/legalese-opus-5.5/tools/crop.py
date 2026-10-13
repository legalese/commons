"""Crop a region of an image and upscale it, for reading small text.

Usage: python3 -I crop.py SRC DST x0 y0 x1 y1 [scale]
Coordinates are in SRC pixels.
"""
import sys
from PIL import Image

src, dst = sys.argv[1], sys.argv[2]
x0, y0, x1, y1 = (int(v) for v in sys.argv[3:7])
scale = float(sys.argv[7]) if len(sys.argv) > 7 else 2.0
im = Image.open(src).convert("RGB")
c = im.crop((x0, y0, x1, y1))
c = c.resize((int(c.width * scale), int(c.height * scale)), Image.LANCZOS)
c.save(dst)
print(im.size, "->", c.size)
