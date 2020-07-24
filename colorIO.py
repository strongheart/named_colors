from wx import Colour as Color

wcFile="data/webColors.tsv"
	# "webColors.tsv"

def loadWebColors():
	F=open(wcFile)
	cm={}
	ff=[line.strip() for line in F.readlines()]
	for line in ff:
		S=line.split('\t')
		C=Color(int(S[1], 0x10))
		r,g,b = C.Get(0)
		cm[S[0]]=Color(b,g,r)
	return cm

