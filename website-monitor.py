import requests as r
import time
import json
from os import system

#urls=["http://127.0.25.6:9005/status","http://127.0.25.6:9005/status"]
#url_data=[]
#url_data_processed=[]
web_url=["http://127.0.25.6:9005/status-b","http://127.0.25.3:9005/status-b","http://127.0.25.2:9005/status-b"]

def primary():
	web_raw=[]
	web_format=[]
	web_temp=""
	final=""
	final2=""
	for url in web_url:
		try: web_raw.append(r.get(url).json())
		except: pass
	for raw in web_raw:
		web_temp=""
		for exact in raw:
			web_temp = web_temp + f"""{f'{exact.upper()}':<8.8} |  {raw[exact]}\n"""
		web_format.append(web_temp)


	final=merge_line(web_format[0],web_format[1],50,1)

	for i in final:
		final2 = final2 + i + "\n"

	final=merge_line(final2,web_format[2],50,2)


	
	for line in final:
		print(line)


def merge_line(var1,var2,width,col):
	width=width
	col=col
	line=[]
	var1_part=[]
	var2_part=[]
	var1_temp=""
	var2_temp=""
	var1_lines=0
	var2_lines=0
	for i in var1: var1_part.append(i)
	for i in var2: var2_part.append(i)
	for i in var1_part:
		if i == "\n": var1_lines=var1_lines+1
	for i in var2_part:
		if i == "\n": var2_lines=var2_lines+1
	
	if var1_lines >= var2_lines:
		for i in var1_part:
			if i=="\n":
				var1_temp = f"""{f'{var1_temp}':<{width*col}.{width*col}}"""
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

	if var2_lines > var1_lines:
		for i in var2_part:
			if i=="\n":
				var2_temp = f"""{f'{var2_temp}':<{width}.{width}}"""
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




primary()
