#! /usr/bin/env python
# -*- coding: utf-8 -*-
import string
import os
from meic import *

def write_table_header(f):
	#header of table
	f.write('<tr>')
	f.write('<th align="center">序号</th> \n <th align="center">时间</th> \n')
	f.write('<th align="center">本次下沉</th> \n <th align="center">累积下沉</th> \n <th align="center">高程</th>\n')
	f.write('<th align="center">载荷</th> \n <th align="center">观测者</th> \n <th align="center">计算者</th>\n')
	f.write('<th align="center">备注</th> \n')
	f.write('</tr>')


#i is from 0
def write_a_row(i,f,days,level,heavy,obver,caluter,note):
	f.write('<tr>\n')
	f.write('<td align="right">'+str(i+1)+'</td>\n')#序号
	f.write('<td align="right">'+days[i]+'</td>\n')#时间
	
	if i>0:
		f.write('<td align="right">'+str(round(float(level[i-1])-float(level[i]),4))+'</td>\n')#本次下沉
		f.write('<td align="right">'+str(round(float(level[0])-float(level[i]),4))+'</td>\n')#累积下沉
	elif i==0:
		f.write('<td align="right">'+'0'+'</td>\n')#本次下沉
		f.write('<td align="right">'+'0'+'</td>\n')#累积下沉
	
	f.write('<td align="right">'+level[i]+'</td>\n')#高程
	f.write('<td align="right">'+heavy[i]+'</td>\n')#载荷
	f.write('<td align="right">'+obver[i]+'</td>\n')#观测者
	f.write('<td align="right">'+caluter[i]+'</td>\n')#计算者
	
	if level[i]==note[i]:
		nt=' '
	else:
		nt=note[i]
	f.write('<td align="right">'+nt+'</td>\n')#备注
	f.write('</tr>\n')


def part_data(days,level,heavy,obver,caluter,note):
	if len(days)<3:
		return
	while compare_day('2010.04.14',days[2]):
		days.pop(1)
		level.pop(1)
		heavy.pop(1)
		obver.pop(1)
		caluter.pop(1)
		note.pop(1)


def point_belong_meicang(meicang,point):
	f=open('../static/point.csv','r')
	while 1:
		mc=f.readline()
		if mc=='\n':
			return False
		pt=string.split(mc,',')
		if pt[0]==meicang:
			if point==pt[1] or point==pt[2] or point==pt[3] or point==pt[4]:
				return True
			else:
				return False
	print('something error?')
	return False


## "meicang:煤仓号;point:点号;days;level:list 高程;obver：观测者;caluter：计算者；comment：备注 ;heavy"
def gen_report(meicang,point,htmlfile,part):	

	if not point_belong_meicang(meicang,point):
		print('point '+ point+' is not belong to '+ 'meicang '+meicang)
		return False
	
	f=open(htmlfile,"w")
	f.write('<html>\n<body>\n')
	f.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
	f.write('<h4 align="center">')
	f.write(meic[meicang]+' ')
	f.write(point+" ")
	f.write("号点沉降观测数据表")
	f.write('</h4>\n')


	f.write("<center>\n")
	#table
	f.write('<table border="1" align="center" style="border-collapse:collapse;">\n')
	
	write_table_header(f)
		
	hf=open('../heavy/'+meicang[0]+'.csv','r')
	lf=open('../level/'+meicang[0]+'.csv','r')
	nf=open('../note/'+meicang[0]+'.csv','r')
	
	days=string.split(hf.readline(),',')
	obver=string.split(hf.readline(),',')
	caluter=string.split(hf.readline(),',')

	hhh=0
	while hhh<int(meicang[1]):
		heavytmp=hf.readline()
		hhh=hhh+1
	heavy=string.split(heavytmp,',')
				

	i=1
	while i<int(point)+1:
		lf.readline()
		nf.readline()
		i=i+1
	level=string.split(lf.readline(),',')
	note=string.split(nf.readline(),',')
	
	if part==True:
		part_data(days,level,heavy,obver,caluter,note)
		
	lel=len(level)

	i=0
	while i<lel:
		write_a_row(i,f,days,level,heavy,obver,caluter,note)
		i=i+1
		
	
	f.write('</table>\n')
	f.write("</center>\n")
	
	#end of html
	f.write('</body>\n</html>\n')

	f.close()
	hf.close()
	lf.close()
	return True
	


def gen_all_report():
	if not os.path.exists('part'):	
		os.mkdir('part')
	if not os.path.exists('all'):
		os.mkdir('all')

	p=open('../static/point.csv','r')
	while 1:
		mc=p.readline()
		if not mc:
			return False
		pt=string.split(mc,',')
		for i in 1,2,3,4:
			phf='./part/'+pt[0]
			ahf='./all/'+pt[0]
			if int(pt[i])<10:
				phf=phf+'0'+pt[i][0]+'.html'
				ahf=ahf+'0'+pt[i][0]+'.html'
			else:
				phf=phf+pt[i][0:2]+'.html'
				ahf=ahf+pt[i][0:2]+'.html'
			gen_report(pt[0],pt[i],phf,True)
			gen_report(pt[0],pt[i],ahf,False)


	
