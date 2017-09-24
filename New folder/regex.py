import re


exp2 = "mon|tue|wed|thur|thurs|fri|sat|sun|monday|tuesday|wednesday|thursday|friday|saturday|sunday"
exp4 = "meet(?:ing)?|event|thing|appointment|appt|lunch|dinner"
exp5 = "\d\d? ?(?:am|pm)"
exp6 = "jan|feb|mar|apr|may|jun|jul|aug|sep|sept|oct|nov|dec|january|february|march|april|may|june|july|august|september|october|november|december"
exp8 = "\d\d? ?(?:th|nd|st|rd)*"
exp9 = "201."
exp1 = "office|home|school|at ?[A-Z][a-z]+"

nameReg = exp4
locationReg = exp1
monthReg = exp6
yearReg = exp9
dayReg = exp2
dateReg = exp8
timeReg = exp5

def checkInfo(row):
	if (row[0] == []):
		return "Could you please tell me what event you have scheduled?"
	elif (row[1] == []):
		return "Could you please tell me where this event will be?"
	elif (row[2] == []):
		return "Could you please tell me what time this event will be taking place?"
	else:
		return "I'll schedule an event called " + row[0] + " at " + row[1] + " for " + row[2] + "."

def createRow(phrase):
	row = [None, None, None]
	row[0] = re.findall(nameReg, phrase, re.IGNORECASE)[0];
	row[1] = re.findall(locationReg, phrase, re.IGNORECASE)[0];
	day = re.findall(dayReg, phrase, re.IGNORECASE)
	month = re.findall(monthReg, phrase, re.IGNORECASE)
	row[2] = day + ", " + month + " " + re.findall(dateReg, phrase, re.IGNORECASE) + " at " + re.findall(timeReg, phrase, re.IGNORECASE)
	print row[2]
	print row

	print checkInfo(row) 

createRow("I have a meeting at home on October 10th, 2017, Monday, at 10PM")
