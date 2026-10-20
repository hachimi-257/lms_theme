"""Build square logo variants from the wide vidiSI logo.

Usage: python make_square_logo.py <wide_logo.png> <output_dir>
"""

import sys

from PIL import Image, ImageDraw

NAVY = (43, 52, 128)
GREEN = (108, 188, 160)

src, out_dir = sys.argv[1], sys.argv[2]
logo = Image.open(src).convert("RGBA")

# The network symbol sits on the right of the wordmark
symbol = logo.crop((1215, 0, logo.width, logo.height))
# Erase the "I" of "SI", which shares columns with the leftmost node
symbol.paste((0, 0, 0, 0), (25, 300, 95, logo.height))
symbol = symbol.crop(symbol.getbbox())


def is_green(r, g, b):
	return g > r + 40 and g > b


def recolor(img, navy_to):
	px = img.load()
	for y in range(img.height):
		for x in range(img.width):
			r, g, b, a = px[x, y]
			if a == 0:
				continue
			if min(r, g, b) > 200:
				# Ring interiors are opaque white in the source
				px[x, y] = (0, 0, 0, 0)
				continue
			px[x, y] = (*GREEN, a) if is_green(r, g, b) else (*navy_to, a)
	return img


def tile(size, symbol_img, background):
	"""Rounded square with the symbol centered."""
	canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
	if background:
		mask = Image.new("L", (size, size), 0)
		ImageDraw.Draw(mask).rounded_rectangle((0, 0, size - 1, size - 1), radius=size // 5, fill=255)
		canvas.paste(Image.new("RGBA", (size, size), (*background, 255)), (0, 0), mask)
	inner = int(size * 0.68)
	s = symbol_img.copy()
	s.thumbnail((inner, inner), Image.LANCZOS)
	canvas.alpha_composite(s, ((size - s.width) // 2, (size - s.height) // 2))
	return canvas


white_symbol = recolor(symbol.copy(), (255, 255, 255))
navy_symbol = recolor(symbol.copy(), NAVY)

tile(512, white_symbol, NAVY).save(f"{out_dir}/logo-square.png")
tile(512, navy_symbol, None).save(f"{out_dir}/logo-square-transparent.png")
tile(64, white_symbol, NAVY).save(f"{out_dir}/favicon.png")
