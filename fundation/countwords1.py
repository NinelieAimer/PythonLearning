#countwords hamlet
def gett():
	txt=open("hamlet.txt","r").read()
	txt=txt.lower()
	for ch in '!"#$%()*+,-./:;<>=?@[\\]^_{|}~':
		txt=txt.replace(ch," ")
	return txt

hamlettxt=gett()
words=hamlettxt.split()
counts={}
for i in words:
	counts[i]=counts.get(i,0)+1
item=list(counts.items())
item.sort(key=lambda x:x[1],reverse=True)
for n in range(10):
	i,number=item[n]
	print("{0:<10}{1:>5}".format(i,number))
