#! /usr/bin/env python
# -*- coding: utf-8 -*-
import string
import os
from meic import *
import linecache

def write_header(f,i):
	f.write('<html>\n<body>\n')
	f.write('<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n')
	f.write('<h2 align="center">')
	f.write(dmc[i]+'沉降观测阶段总结')
	f.write('</h2>\n')
	
	f.write('<p>自'+starttime[i]+'起，对'+dmc[i]+'沉降情况进行了观测,对观测结果进行分析，结果如下：</p>')
	
	f.write('<h3 align="left">1．下沉数据统计</h3>\n')
	
	
def write_table(f,i,j):
	f.write('<h4 align="left">1.'+j+' '+xmc[j]+'</h4>\n')
	f.write('<h4 align="center">最大下沉及累计下沉统计表</h4>\n')
	f.write("<center>\n")
	f.write('<table border="1" align="center" style="border-collapse:collapse;">\n')
	f.write('<tr>')
	f.write('<th align="center">观测点号</th> \n <th align="center">最大下沉(mm)</th> \n')
	f.write('<th align="center">载荷(%)</th> \n <th align="center">观测时间</th> \n <th align="center">累计下沉(mm)</th>\n')
	f.write('<th align="center">载荷(%)</th> \n <th align="center">观测时间</th> \n')
	f.write('</tr>')
	
	point=get_point(i,j)
	pmax,plst=get_data(i,j,point)
	
	x=0
	while(x<4):
		f.write('<tr>\n')
		f.write('<td align="right">'+point[x]+'</td>\n')
		f.write('<td align="right">'+str((-1)*round(pmax[x]['xc']*1000,1))+'</td>\n')
		f.write('<td align="right">'+pmax[x]['zh']+'</td>\n')
		f.write('<td align="right">'+pmax[x]['day']+'</td>\n')
	
		f.write('<td align="right">'+str((-1)*round(plst[x]['xc']*1000,1))+'</td>\n')
		f.write('<td align="right">'+plst[x]['zh']+'</td>\n')
		f.write('<td align="right">'+plst[x]['day']+'</td>\n')
		f.write('</tr>\n')
		x=x+1
	
	f.write('</table>\n</center>\n')
		
	f.write('<p>最大下沉差为对称点 ')
	k=0
	if(abs(plst[2]['xc']-plst[0]['xc'])>abs(plst[3]['xc']-plst[1]['xc'])):
		delt=abs(plst[2]['xc']-plst[0]['xc'])
	else:
		delt=abs(plst[3]['xc']-plst[1]['xc'])
		k=1
		
	f.write(point[k]+'——'+point[k+2]+'，')
	f.write('差值为 Δ='+str(round(delt*1000,1))+'mm，<br/>')
	k=1.0/delt*mczj[i]
	f.write('相对倾斜为 k=Δ/2R=1/'+str(int(k))+'<br/>')
	f.write('顶部偏差值为 Δ<sub>顶</sub>='+str(round(mcg[i]*delt/mczj[i]*1000,1))+'mm</p>')
	f.write('<img src = "../plot/'+i+j+'.png" width="100%">')
	
def write_analysis(f,i):
	af=open('../analysis/'+i,'r')
	while(1):
		ana=af.readline()
		if(not ana):
			return
		f.write(ana)

def write_tail(f):
	f.write('</body>\n</html>\n')
	
def get_point(i,j):
	tmpf=open('../static/point.csv','r')
	while(1):
		pn=tmpf.readline()
		if(not pn):
			return None
		tmpp=string.split(pn,',')
		if(tmpp[0][0]==i and tmpp[0][1]==j):
			point=tmpp[1:]
			point[3]=str(int(tmpp[4]))
			return point
	return None
	
def get_data(i,j,point):
	lvf='../level/'+i+'.csv'
	day=string.split(linecache.getline(lvf,1),',')
	hvf='../heavy/'+i+'.csv'

	p0=string.split(linecache.getline(lvf,int(point[0])+1),',')
	p1=string.split(linecache.getline(lvf,int(point[1])+1),',')
	p2=string.split(linecache.getline(lvf,int(point[2])+1),',')
	p3=string.split(linecache.getline(lvf,int(point[3])+1),',')
	
	heavy=string.split(linecache.getline(hvf,3+int(j)),',')
	
	plt=[{'xc':float(p0[-1])-float(p0[0]),'zh':heavy[-1],'day':day[-1]},
		{'xc':float(p1[-1])-float(p1[0]),'zh':heavy[-1],'day':day[-1]},
		{'xc':float(p2[-1])-float(p2[0]),'zh':heavy[-1],'day':day[-1]},
		{'xc':float(p3[-1])-float(p3[0]),'zh':heavy[-1],'day':day[-1]}]

	mindex=[0,0,0,0];
	x=0
	while(x<len(p0)):
		if(float(p0[x])<float(p0[mindex[0]])):
			mindex[0]=x
		if(float(p1[x])<float(p1[mindex[1]])):
			mindex[1]=x
		if(float(p2[x])<float(p2[mindex[2]])):
			mindex[2]=x
		if(float(p3[x])<float(p3[mindex[3]])):
			mindex[3]=x
		x=x+1
	
	pmx=[{'xc':float(p0[mindex[0]])-float(p0[0]),'zh':heavy[mindex[0]],'day':day[mindex[0]]},
		{'xc':float(p1[mindex[1]])-float(p1[0]),'zh':heavy[mindex[1]],'day':day[mindex[1]]},
		{'xc':float(p2[mindex[2]])-float(p2[0]),'zh':heavy[mindex[2]],'day':day[mindex[2]]},
		{'xc':float(p3[mindex[3]])-float(p3[0]),'zh':heavy[mindex[3]],'day':day[mindex[3]]}
		]
	return pmx,plt

def gen_paper():
	f=open('./paper/1.html','w')
	write_header(f,'1')
	write_table(f,'1','1')
	write_table(f,'1','2')
	write_analysis(f,'1')

	f=open('./paper/2.html','w')
	write_header(f,'2')
	write_table(f,'2','1')
	write_table(f,'2','2')
	write_analysis(f,'2')

	f=open('./paper/3.html','w')
	write_header(f,'3')
	write_table(f,'3','1')
	write_table(f,'3','2')
	write_table(f,'3','3')
	write_table(f,'3','4')
	write_analysis(f,'3')

	f=open('./paper/4.html','w')
	write_header(f,'4')
	write_table(f,'4','1')
	write_table(f,'4','2')
	write_analysis(f,'4')
