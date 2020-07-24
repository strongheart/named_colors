import wx
from wx import Colour as Color

REDNESS=0
GREENNESS=1
BLUENESS=2
DARKNESS=3
GRAYNESS=4
ALPHABETICAL=99

HEX=0
RGB=1
DEC=2


def crep(color, repmode=HEX):
	""":return str representation of color
	:param repmode determines if hexidecimal (HEX), compoite (RGB) ir devimal (DEC) representation is returned.
	"""
	if repmode==RGB:
		r,g,b,=color.Get(0)
		return(f"{r},{g},{b}")
	d=color.GetRGB()
	if repmode==DEC:
		return str(d)
	else:
		x="0x"+ ("000000"+hex(d)[2:] )[-6:]
		return x


def contrast(color):
	r,g,b=color.Get(0)
	r-=127
	b-=127
	g-=127
	return Color(r%256,g%256,b%256)


def invert(color):
	return Color(0xFFFFFF-color.GetRGB())


def xness(color, mode):
	r,g,b= cc =color.Get(0)
	csum=r+g+b+1
	if mode in range(3):
		x=cc[mode]
		return x*x/csum+x
	elif mode==DARKNESS:
		return csum
	elif mode==GRAYNESS:
		s=0
		for c in cc:
			s+=abs(127-c)
			return s
	else: return None

def alphabetical(cmap, rev):
	cm=dict(sorted(cmap.items(), key=lambda item: item[0].upper(), reverse=rev ))
	return cm

def sort(cmap, method, rev=0):
	if method<0 : rev=1
	method=abs(method)
	if method not in range(GRAYNESS+1):
		return alphabetical(cmap, rev)
	cm=dict(sorted(cmap.items(), key=lambda item: xness(item[1],method), reverse=rev ))
	return cm

