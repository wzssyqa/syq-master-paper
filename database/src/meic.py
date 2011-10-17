#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import string

meic={"11":"一号原煤仓","12":"二号原煤仓","21":"一号矸石仓","22":"二号矸石仓","31":"一号块精煤仓","32":"二号块精煤仓","33":"三号块精煤仓","34":"四号块精煤仓","41":"一号末煤仓","42":"二号末煤仓"}

dmc={'1':"原煤仓","2":"矸石仓","3":"块精煤仓","4":"末煤仓"}

xmc={'1':"一号仓","2":"二号仓","3":"三号仓","4":"四号仓"}

starttime={'1':'2009年11月21日','2':'2009年12月22日','3':'2010年1月7日','4':'2009年12月19日'}

mcg={'1':43.15,'2':21.5,'3':22.5,'4':50.2}

mczj={'1':22.0,'2':12.0,'3':15.0,'4':30.0}

def get_month_string(day):
	return day[0:4]+'年'+day[5:7]+'月'
	

#is day1 later than or equle day2 ?
def compare_day(day1,day2):
	sday1=string.split(day1,'.')
	sday2=string.split(day2,'.')

	if int(sday1[0])>int(sday2[0]):
		return True
	elif int(sday1[0])<int(sday2[0]):
		return False
	elif int(sday1[1])>int(sday2[1]):
		return True
	elif int(sday1[1])<int(sday2[1]):
		return False
	elif int(sday1[2])>=int(sday2[2]):
		return True
	elif int(sday1[2])<int(sday2[2]):
		return False


def date_diff(day1,day2):
	y1=int(day1[0:4])
	m1=int(day1[5:7])
	d1=int(day1[8:10])

	y2=int(day2[0:4])
	m2=int(day2[5:7])
	d2=int(day2[8:10])
	date1=datetime.date(y1,m1,d1)
	date2=datetime.date(y2,m2,d2)

	return (date2-date1).days
