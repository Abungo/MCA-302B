import re

date1 = '''2022-04-14 2022-05-06
2023-6-7
'''
q = r'\d{4}-\d{1,2}-\d{1,2}'
lst = re.findall(q,date1)
print("The dates in the file are: ",lst)
print("The dates in DD-MM-YYYY Format are: ")
for i in lst:
	ndate = re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', i)
	print(ndate)