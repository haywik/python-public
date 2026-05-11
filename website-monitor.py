import requests as r
import time
import json

web1 = r.get("http://127.0.25.6:9005/status").json()
web2 = r.get("http://127.0.25.6:9005/status").json()

web1_com=""
web2_com=""
for i in web1:
	web1_com = web1_com + f"""{f'{i.upper()}':<8.8} |  {web1[i]}\n""" 

for i in web2:
	web2_com = web2_com + f"""{f'{i.upper()}':<8.8} |  {web2[i]}\n"""

def merge_line(var1,var2):
	line=[]
	var1_part=[]
	var2_part=[]
	var1_temp=""
	var2_temp=""
	for i in var1: var1_part.append(i)
	for i in var2: var2_part.append(i)

	if len(var1_part) >= len(var1_part):
		for i in var1_part:
			if i=="\n":
				var1_temp = f"""{f'{var1_temp}':<40.40}"""
				line.append(var1_temp)
				var1_temp=""
			else:
				var1_temp=var1_temp+i
		c=-1
		for i in var2_part:
			if i=="\n":
				c=c+1
				line[c] = line[c] + var2_temp
				var2_temp=""
			else:
				var2_temp=var2_temp+i

	if len(var2_part) > len(var1_part):
		for i in var2_part:
			if i=="\n":
				var2_temp = f"""{f'{var2_temp}':<30.30}"""
				line.append(var2_temp)
				var2_temp=""
			else:
				var2_temp=var2_temp+i
		c=-1
		for i in var1_part:
			if i=="\n":
				c=c+1
				line[c] = line[c] + var1_temp
				var1_temp=""
			else:
				var1_temp=var1_temp+i


	return line

print(web1_com)
print(web2_com)
print(merge_line(web1_com,web2_com))


