import requests as r

#rec = r.get("https://dev.haywik.com/status-b")

#print(rec.text)

#formatted = {rec.text}
#print(formatted)


example = """{"name":"dev.haywik.com","alive":true,"uptime":"18:14:44"}"""




def convert_json(data):
	proc = {}
	temp=""
	for char in data:
		if char == ",":
			part=temp.replace("{","").replace("}","").replace("'","")
			temp=""
			point = part.index(":")
			part=part.replace(":","")
			proc[part[:point].replace('"','')]=part[point:].replace('"','')
		else:
			temp=temp+char
	return proc

final = convert_json(example)


main = {"random":"random"}

main.update(final)

print(main)




