import re
s = """<html>
<head>
	<title>Html Document</title>
</head>
<body>
	<div>
		<h1>Hello there</h1>
		<p>This is a paragraph inside a html document
And here is some gibberish text.
		</p>
	</div>
</body>

</html>
"""
p = r'</*.+?>'
str = re.sub(p,"",s)
print(str)
