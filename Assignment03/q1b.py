import re
f = open("emails.txt","rt")
lines = f.read()
p = r'[a-zA-Z0-9._]+@[a-zA-Z]+[a-zA-Z.-]+'
lst = re.findall(p,lines)
for i in lst:
	print(i)
