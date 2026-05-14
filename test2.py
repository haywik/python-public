import requests as r

#rec = r.get("https://dev.haywik.com/status-b")

#print(rec.text)

#formatted = {rec.text}
#print(formatted)


example = """{"name":"dev.haywik.com","alive":true,"uptime":"18:14:44"}"""

temp=""
temp2=""

proc = {}

for char in example:
	if char == ",":
		part=temp
		temp=""
		point = part.index(":")
		proc[example[:point]]=example[point:]
	else:
		temp=temp+char


print(proc)
