import wx
from data.wxColorNames import colorMap as wxColorMap
from colorIO import *


class CDB(wx.ColourDatabase):
	def __init__(self):
		super().__init__()
		self.wxColors=wxColorMap
		self.webColors=loadWebColors()
		self.colors={**self.wxColors, **self.webColors}

		for n,c in self.colors.items():
			self.AddColour(n,c)

		print(f"{len(wxColorMap)} wxColors and  {len(self.webColors)} totaling  {len(self.colors)}")


