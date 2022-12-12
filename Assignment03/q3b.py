import re

f = open("index.html","rt")
lines = f.read()
#print(lines)
p = r'</*.+?>'
str = re.sub(p,"",lines)
print(str)
