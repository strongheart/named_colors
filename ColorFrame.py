from random import randint

import wx
from colorTool import *
from colorpane import CPane, colorize



def butt(p,t,c):
	b=wx.Button(p,-1,t)
	b.SetBackgroundColour(c)
	b.SetForegroundColour(Color(0xFFFFFF-c.GetRGB() ))
	b.SetForegroundColour(Color(contrast(c)))
	P=p.GetParent()
	b.Bind(wx.EVT_BUTTON, P.sortColor)
	b.Bind(wx.EVT_ENTER_WINDOW, P.tellSort)
	b.Bind(wx.EVT_LEAVE_WINDOW, P.unTell)

	# print(f"{b.GetLabelText()} id={b.GetId()}")
	return b

class CF(wx.Frame):
	def __init__(self, P=None, title="Named Color by steve"):
		super().__init__(P, -1,title)
		self.cbrev=None
		self.idRed=None
		self.idGreen=None
		self.idBlue=None
		self.idGray=None
		self.idDark=None
		self.idAlphabet=None
		self.myTBar()
		self.cpan=CPane(self)
		Z=wx.BoxSizer(wx.VERTICAL)
		Z.Add(self.cpan, 1,wx.EXPAND|wx.ALL, 5)
		self.SetSizer(Z)


	def myTBar(self):
		tbar=self.CreateToolBar()
		self.cbrev=wx.CheckBox(tbar,-1,"Sort Reversed", style=wx.CB_SORT)
		tbar.AddControl(self.cbrev, "Reverse Sort")
		# cb.Bind(wx.EVT_CHECKBOX, self.check)
		b = butt(tbar, "Red", wx.RED)
		tbar.AddControl(b, "red")
		self.idRed=b.GetId()
		b=butt(tbar,"Green",wx.GREEN)
		tbar.AddControl(b,"green")
		self.idGreen = b.GetId()
		b = butt(tbar, "Blue", wx.BLUE)
		self.idBlue = b.GetId()
		tbar.AddControl(b, "Blue")
		b=butt(tbar,"Dark",wx.BLACK)
		self.idDark = b.GetId()
		tbar.AddControl(b,"Dark")
		# b=butt(tbar,"Gray",invert(wx.LIGHT_GREY))
		b = butt(tbar, "Gray", invert(Color(127, 127, 127)))
		self.idGray = b.GetId()
		tbar.AddControl(b, "Grey")

		b = butt(tbar, "By Name", Color(randint(0,255),randint(0,255),randint(0,255)))
		self.idAlphabet = b.GetId()
		tbar.AddControl(b, "Name")

		sbar=self.CreateStatusBar(6)
		self.statbar=sbar
		self.tell("Color Tool Not ready")



	def sortColor(self,e):
		b=e.GetEventObject()
		print(f"Sort Color {b.GetLabelText()} id={e.GetId()} {b.GetId()}")
		k=b.GetId()
		M=None
		if k == self.idRed :
			M=REDNESS
		elif k == self.idGreen:
			M=GREENNESS
			# print("GREENIE")
		elif k == self.idBlue:
			M=BLUENESS
		elif k == self.idDark:
			M=DARKNESS
		elif k == self.idGray:
			M=GRAYNESS
		else :
			M=ALPHABETICAL
			colorize(e.GetEventObject(), Color(randint(0,255),randint(0,255),randint(0,255)))
		cb=self.cbrev
		# cb=wx.CheckBox(self)
		rev= -1 if cb.GetValue() else 1

		self.cpan.sort_method=M
		self.cpan.sort(M, cb.GetValue())
		self.Refresh()

	def tellSort(self, e):
		b=e.GetEventObject()
		t= b.GetLabelText()
		self.tell(f"Sort By {t}ness",0)

	def unTell(self, e):
		self.statbar.PopStatusText( 0)

	def tell(self,text, i=0):
		self.statbar.PushStatusText(text,i)




class App(wx.App):
	def __init__(self):
		super(App, self).__init__()
		frame = CF(None)
		frame.Show(True)


if __name__ == '__main__':
	app = App()
	app.MainLoop()



