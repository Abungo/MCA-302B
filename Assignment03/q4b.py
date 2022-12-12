import re

f = open("date.txt","rt")
date1 = f.read()
q = r'\d{4}-\d{1,2}-\d{1,2}'
lst = re.findall(q,date1)
print("The dates in the file are: ",lst)
print("The dates in DD-MM-YYYY Format are: ")
for i in lst:
	ndate = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', i)
	print(ndate)