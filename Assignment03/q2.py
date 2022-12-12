import re
s = """9205305486 +91 80762106306
+91862354690
+91
"""
q = r'\+?[1-9]?[0-9]? ?[0-9]{8,10}'
lst = re.findall(q,s)
print("Phone numbers in the String are: ")
for i in lst:
	print(i)
