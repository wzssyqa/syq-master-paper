#! /usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import string
import os
from meic import *

import linecache

#两个末煤仓的沉降
#使用全局变量，有点脏
mo1_cj=[]
mo2_cj=[]

def plot_a_mc(pt,fom,to):
	lfn='../level/'+pt[0][0]+'.csv'
	hfn='../heavy/'+pt[0][0]+'.csv'

	day=string.split(linecache.getline(lfn,1),',')
	
	lev1=string.split(linecache.getline(lfn,int(pt[1])+1),',')
	lev2=string.split(linecache.getline(lfn,int(pt[2])+1),',')
	lev3=string.split(linecache.getline(lfn,int(pt[3])+1),',')
	lev4=string.split(linecache.getline(lfn,int(pt[4])+1),',')
	
	hv=string.split(linecache.getline(hfn,int(pt[0][1])+3),',')
	
	while compare_day(day[-1],to):
		day.pop()
		hv.pop()
		lev1.pop()
		lev2.pop()
		lev3.pop()
		lev4.pop()
	
	while compare_day(fom,day[0]):
		day.pop(0)
		hv.pop(0)
		lev1.pop(0)
		lev2.pop(0)
		lev3.pop(0)
		lev4.pop(0)

	lth=len(day)
	i=1
	cj1=[0.0]
	cj2=[0.0]
	cj3=[0.0]
	cj4=[0.0]
	while i<lth:
		cj1.append(float(lev1[0])-float(lev1[i]))
		cj2.append(float(lev2[0])-float(lev2[i]))
		cj3.append(float(lev3[0])-float(lev3[i]))
		cj4.append(float(lev4[0])-float(lev4[i]))
		i=i+1
	
	if pt[0]=='41':
		mo1_cj.append(cj1)
		mo1_cj.append(cj2)
		mo1_cj.append(cj3)
		mo1_cj.append(cj4)
	if pt[0]=='42':
		mo2_cj.append(cj1)
		mo2_cj.append(cj2)
		mo2_cj.append(cj3)
		mo2_cj.append(cj4)
	
	tmpf=open('tmpf.tmp','w')
	i=0
	while i<lth:
		tmpf.write(str(date_diff(day[0],day[i]))+' '+str(float(hv[i]))+' '+'0 '+str(-cj1[i]*1000)+' '+str(-cj2[i]*1000)+' '+str(-cj3[i]*1000)+' '+str(-cj4[i]*1000)+'\n')
		i=i+1
	tmpf.close()

	pcf=open('cmd.plot','w')
	pcf.write('set term png font \'/usr/share/fonts/truetype/simsun.ttc,10\' size 1280,800\n')
	pcf.write('set output '+'"./plot/'+pt[0]+'.png"\n')
	pcf.write('set size 1,1\n')
	pcf.write('set grid\n')

	pcf.write('set xlabel "从第一次测量开始的天数"\n')
	pcf.write('set ylabel "』米毫『 量降沉的比相量测次一第与                                           百分比 量煤装" offset -5\n')
	pcf.write('plot ')
	pcf.write('"tmpf.tmp" using 1:4 title '+'"'+pt[1]+ '" w lines,')
	pcf.write(' "tmpf.tmp" using 1:5 title '+'"'+pt[2]+ '" w lines,')
	pcf.write(' "tmpf.tmp" using 1:6 title '+'"'+pt[3]+ '" w lines,')
	pcf.write(' "tmpf.tmp" using 1:7 title '+'"'+str(int(pt[4]))+ '" w lines,')
	pcf.write(' "tmpf.tmp" using 1:3 w lines lt rgb "black" title "",')
	pcf.write(' "tmpf.tmp" using 1:2 title '+'"'+'装煤量 %'+ '" w lines\n\n')

	pcf.close()

	os.system('gnuplot cmd.plot')
	
	phf=open('./newreport/'+pt[0]+'.html','w')
	phf.write('<html>\n<body>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
	phf.write('<h4 align="center">'+meic[pt[0]]+'高程表</h4>')
	phf.write('<center>\n<table border="1" align="center" style="border-collapse:collapse;">\n')
	phf.write('<tr>\n<th>时间</th><th colspan="4">各点高程</th>\n</tr>\n')
	phf.write('<tr><td>'+' '+'</td><td>'+pt[1]+'</td><td>'+pt[2]+'</td><td>'+pt[3]+'</td><td>'+pt[4]+'</td></tr>\n')
	i=0
	while i<lth:
		phf.write('<tr><td>'+day[i]+'</td><td>'+lev1[i]+'</td><td>'+lev2[i]+'</td><td>'+lev3[i]+'</td><td>'+lev4[i]+'</td></tr>\n')
		i=i+1
	phf.write('</table>\n</center>\n\n\n')
	phf.write('<h4 align="center">'+meic[pt[0]]+'沉降表</h4>')
	phf.write('<center>\n<table border="1" align="center" style="border-collapse:collapse;">\n')
	phf.write('<tr>\n<th>时间</th><th colspan="4">各点沉降量</th>\n</tr>\n')
	phf.write('<tr><td>'+' '+'</td><td>'+pt[1]+'</td><td>'+pt[2]+'</td><td>'+pt[3]+'</td><td>'+pt[4]+'</td></tr>\n')
	i=0
	while i<lth:
		phf.write('<tr><td>'+day[i]+'</td><td>'+str(round(cj1[i],4))+'</td><td>'+str(round(cj2[i],4))+'</td><td>'+str(round(cj3[i],4))+'</td><td>'+str(round(cj4[i],4))+'</td></tr>\n')
		i=i+1
	phf.write('</table>\n</center>\n\n\n')
	
	phf.write('<h4 align="center">'+meic[pt[0]]+'沉降图</h4>\n')
	phf.write('<img src = "../plot/'+pt[0]+'.png" width="100%"/>\n')
	phf.write('</body>\n</html>')
	phf.close()

def plot_all_mc(fom,to):
	pfn='../static/point.csv'
	pf=open(pfn,'r')
	while 1:
		pto=pf.readline()
		if not pto:
			return
		else:
			pt=string.split(pto,',')
			plot_a_mc(pt,fom,to)
