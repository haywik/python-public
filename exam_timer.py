import time
from os import system

total_q = 0	#total questions on paper
total_time = 0 #Mins

sec = 0
min = 0
hour = 0

min_d = 0
hour_d =0
sec_c = 0
q_num = 1  #starting question number



if total_q <  1:
	while True:
		total_q = input("Total questions on paper [Num]:")
		if total_q.isnumeric():
			total_q = int(total_q)
			break
if total_time < 1:
	while True:
		total_time = input("Total time of paper [Mins]:")
		if total_time.isnumeric():
			total_time=int(total_time)
			break

tt = total_time * 60
hour_d = int(tt / 60 / 60)
min_d = int(tt/60 - (hour_d*60))
sec_d = tt - min_d*60 - hour_d*60*60

split_time = total_time*60 / total_q		# how much timer per question


def format_time(hour,min,sec):
	if min < 10:min_o = "0"+str(min)  #min_o is minute output
	else: min_o = min

	if hour < 10:hour_o = "0"+str(hour)
	else: hour_o = hour

	if sec < 10:sec_o = "0"+str(sec)
	else: sec_o = sec

	formatted = f"{hour_o}:{min_o}:{sec_o}"

	return formatted

def convert_time(sec):
	hour = int( sec /60 /60)
	min = int(sec/60 - (hour*60))
	sec = int(sec - min*60 - hour *60*60)
	
	return format_time(hour,min,sec)
	

while True:
	time.sleep(1)
	sec = sec + 1
	sec_c = sec_c + 1			#a constant second second timer
	sec_d = sec_d - 1
	
	if sec > 59:
		min = min +1
		sec = 0
	if sec_d < 0:
		min_d = min_d - 1
		sec_d = 59
	if min_d < 0:
		min_d = 59
		hour_d = hour_d - 1
		if hour_d < 0:
			hour_d = 0
	if min > 60:
		hour = hour + 1
		min = 0
	if sec_c > split_time:
		q_num = q_num + 1		#current question number
		sec_c = 0

	min_q_en = sec_c / 60

	print("\033[H\033[J", end="")

	format = f"""
{'-'*90}
{f'Time enlasped: {format_time(hour,min,sec)}':<35.35} Question enlasped: {convert_time(sec_c)}\n
{f'Time left: {format_time(hour_d,min_d,sec_d)}':<35.35} Question left: {convert_time(split_time-sec_c)}\n
{f' ' :<35.35} Question num: {q_num}\n
{'-'*90}
	"""


	print(format)
