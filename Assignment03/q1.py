import re
s = """abungo@Gmail.co.nz,abungothokchom@gmail.com
abungococ@gmail.com
"""
p = r'[a-zA-Z0-9._]+@[a-zA-Z]+[a-zA-Z.-]+'
lst = re.findall(p,s)
for i in lst:
	print(i)
