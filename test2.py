import requests as r

#rec = r.get("https://dev.haywik.com/status-b")

#print(rec.text)

#formatted = {rec.text}
#print(formatted)


example = """{"name":"dev.haywik.com","alive":true,"uptime":"day 1, 18:14:44"}"""

get_name=True
capture=False
get_info=False
info_capture=False
info_first=True
info_end="$RN#ADOM"
temp=""
temp2=""
proc = {}

def convert_json(data):
	global get_name,capture,get_info,info_capture,info_first,info_end,temp,temp2,proc
	for char in data:
		if char == '"' and get_name == True:
			if capture==False:capture=True
			elif capture==True: capture=False

		if capture==True:
			temp=temp+char
			temp.replace('"',"")

		if capture==False and temp != "":
			proc[temp]=""
			temp=""
			get_info=True
			get_name=False

		if get_info == True and char == ":":
			capture_info=True	

		if info_capture==True:
			if info_first==True and char=='"':
				info_end='"'
				info_first=False
			elif info_first==True and char!='"':
				info_end=","
				info_first=False

			if char!=info_end:
				temp2=temp2+char
				temp2=temp2.replace('"',"")
			elif char==info_end:
				proc[temp]=temp2
				get_name=True
				info_capture=False


	print(proc)
final = convert_json(example)

print(final)






