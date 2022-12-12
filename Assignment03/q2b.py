import re
f = open("phones.txt","rt")
s = f.read()
q = r'\+?[1-9]?[0-9]? ?[0-9]{8,10}'
lst = re.findall(q,s)
print("Phone numbers in the File are: ")
for i in lst:
	print(i)
