"""
"""

import webbrowser
import urllib.request
print("Enter starting prompt")
prompt=input()
route=[]
route.append(prompt)
url="https://en.wikipedia.org/wiki/"+prompt
webbrowser.open(url)
page=urllib.request.urlopen(url)
for x in range(1,65):
	line=page.readline()
	if(b'<p>' in line and b'<a href' in line):
		print(line)
print(route)