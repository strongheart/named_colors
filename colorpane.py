import wx
from colorTool import *
import colorTool as ct
from cdb import CDB, Color


def colorize(w,c, inv=1):
	r = invert(c) if inv else contrast(c)
	w.SetBackgroundColour(c)
	w.SetForegroundColour(r)

def lab(P,t,c,z=None):
	w=wx.StaticText(P,-1,t)
	colorize(w,c)
	w.SetFont(P.GetFont())
	if z: z.Add(w, 1, wx.EXPAND | wx.ALL, 2)
	w.SetFont(P.GetFont())
	return w

def butt(P,t,c,z=None):
	w=wx.Button(P,-1,t)
	colorize(w,c,0)
	w.SetFont(P.GetFont())
	w.Bind(wx.EVT_BUTTON, P.pressed)
	if z: z.Add(w, 1, wx.EXPAND | wx.ALL, 1)
	return w

def tfin(P,t,c,z=None):
	w=wx.TextCtrl(P,-1,t,style=wx.TEXT_ALIGNMENT_RIGHT)
	colorize(w,c)
	w.SetFont(P.GetFont())
	if z: z.Add(w, 1, wx.EXPAND | wx.ALL, 1)
	return w

class CPane(wx.ScrolledWindow):
	def __init__(self, P):
		super().__init__(P)
		self.SetScrollRate(10,10)
		self.SetMinSize((500,300))
		self.SetScrollPos(wx.HORIZONTAL,0)
		self.SetSize((911, 600))
		F=self.GetFont()
		F.SetPixelSize((0,18))
		self.SetFont(F)
		self.cdb=CDB()
		self.color_rep=HEX
		self.sort_method=DARKNESS
		self.initData()
		self.Bind(wx.EVT_SIZE, self.resize)
		self.sort()
		self.Scroll(1,1)
		self.SetTargetRect(wx.Rect ((0,0),self.Size))

		self.SetScrollPos(wx.HORIZONTAL,0)
		pos = self.GetScrollPos(wx.HORIZONTAL)
		print(f"SCROLL al {pos}")
		self.Refresh()

	def initData(self):
		gz=wx.GridSizer(3,5,5)
		cm=self.cdb.colors
		for n,C in cm.items():
			p =wx.Panel(self)
			z=wx.BoxSizer()
			tag=lab(p,n,C,z)
			p.SetSizer(z)
			colorize(p,C)
			gz.Add(p, 1,wx.EXPAND,10)
			tf=tfin(self, crep(C,self.color_rep) ,invert(C), gz)
			b=butt(self,f"{n} info",C,gz)
		self.SetSizer(gz)
		self.Scroll(0,-1)
		self.SetTargetRect(wx.Rect ((0,0),self.Size))


	def resize(self,e):
		w,h=self.Size
		print(f"{self.GetName()} Size = {(w,h)}")
		pos=self.GetScrollPos(wx.HORIZONTAL)
		print(f"SCROLL al {pos}")


	def pressed(self, e):
		b=e.GetEventObject()
		C=b.GetBackgroundColour()
		n=self.cdb.FindName(C)
		print(f"{n} button pressed ")

	def sort(self, method=None, rev=0):
		if not method:
			method=self.sort_method
		cm=self.cdb.colors
		cm=ct.sort(cm,method,rev)
		gz=self.GetSizer()
		kids=[c.GetWindow() for c in gz.GetChildren()]
		z=len(kids)
		z3=z//3
		Z=z if len(cm)==z3 else min(z,len(cm))
		nn=[n for n in cm.keys()]
		F = self.GetFont()
		for k in kids:
			k.SetFont(F)

		for k in range(0,Z,3):
			pan=kids[k]
			tag=pan.GetSizer().GetChildren()[0].GetWindow()
			val=kids[k+1]
			b = kids[k + 2]
			name=nn[k//3]
			C=cm[name]
			v=ct.crep(C, self.color_rep)
			tag.SetLabelText(name)
			val.SetValue(v)
			b.SetLabelText(f'{name} info')
			colorize(tag,C)
			colorize(pan,C)
			colorize(val,invert(C))
			colorize(b,C,0)
			colorize(tag, C)

			tag.Refresh()
		self.Refresh()
		self.Update()







class App(wx.App):
	def __init__(self):
		super(App, self).__init__()
		frame = wx.Frame(None, -1,"Test ColorPane")#, style=wx.CENTER|wx.RESIZE_BORDER|wx.DEFAULT_FRAME_STYLE)
		pane=CPane(frame)
		z = wx.BoxSizer()
		z.Add(pane,1, wx.EXPAND|wx.ALL, 1)
		frame.SetSizer(z)
		frame.Show(True)
		pane.Scroll(0,0)
		frame.Fit()



if __name__ == '__main__':
	app = App()
	app.MainLoop()
