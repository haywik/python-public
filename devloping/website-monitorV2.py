import requests as r
import time
import json

web_url=["https://haywik.com/status-b","https://dev.haywik.com/status-b","https://central.haywik.com/status-b"]

def primary():
	web_raw=[]
	web_format=[]
	web_temp=""
	final=""
	final2=""
	for url in web_url:
		try:
			web_raw.append(r.get(url).json())
		except Exception as e: print("prinary() web error",e)
	for raw in web_raw:
		web_temp=""
		for exact in raw:
			web_temp = web_temp + f"""{f'{exact.upper()}':<8.8} |  {raw[exact]}\n"""
		web_format.append(web_temp)

	if len(web_format) == 1: final=merge_line[0]
	if len(web_format) == 2:
		final=merge_line(web_format[0],web_format[1],50,1)
		for i in final:
			final2 = final2 + i + "\n"
		final=merge_line(final2,web_format[2],50,2)
	if len(web_format) > 2:
		final=merge_line(web_format[0],web_format[1],50,1)
		pointer=2
		for e in range(len(web_format)-2):
			for i in final:
				final2 = final2 + i + "\n"									#12.may.2026 21:29 gmt, seems to bug out when above 3 cols, could be as data is not unuiqe but probs a logica issue
			final=merge_line(final2,web_format[pointer],50,pointer)
			pointer=pointer+1

	return final

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


out=primary()
while True:
	for i in out:
		print(i)
	out=primary()
	time.sleep(3)
	print("\033[H\033[J", end="")
