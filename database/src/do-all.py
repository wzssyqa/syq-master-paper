#! /usr/bin/env python
# -*- coding: utf-8 -*-
import mdp
import mutinfo
from genreport import *
from genplot import *
from genpaper import *
from sys import *
import os
import numpy
import scipy.stats
#两个末煤仓的沉降
#使用全局变量，有点脏
#定义在 genplot.py 文件中
###沉降  #mo1_cj=[]  #mo2_cj=[]
###装煤量 #mo1_load=[] #mo2_load=[]
### 温度  #mo_tmp[]
### 时间  #mo_day[]
def do_fast_ica(pca_first):
	mo1_cj_inverse = numpy.array(mo1_cj).T
	mo2_cj_inverse = numpy.array(mo2_cj).T
	if pca_first:
		mo1_cj_array = mdp.pca(mo1_cj_inverse, input_dim=4, output_dim=3)
		mo2_cj_array = mdp.pca(mo2_cj_inverse, input_dim=4, output_dim=3)
	else:
		mo1_cj_array = mo1_cj_inverse
		mo2_cj_array = mo2_cj_inverse
	a = mdp.fastica(mo1_cj_array)
	b = mdp.fastica(mo2_cj_array)
	return a,b

def compute_pearsonr(raw, icaed):
## raw 和 icaed 都是一列为一个组数据的矩阵
	i=0; j=0
	raw_here=raw.T
	icaed_here=icaed.T
	pearson_value=[]
	mutinfo_value=[]
	icaed_len,xxxx=icaed_here.shape
	while j<icaed_len:
		tmp,tmp_tmp=scipy.stats.pearsonr(raw_here, icaed_here[j])
		pearson_value.append(tmp)
		tmp=mutinfo.nmi(raw_here,icaed_here[j])
		mutinfo_value.append(tmp)
		j=j+1
	return pearson_value, mutinfo_value
	
#gen_report('11','7','./dd.html',False)

def plot_icaed(day, load, tmp, icaed, name):
	f=open('tmpf.tmp','w')
	icaed_here=icaed.T
	icaed_len,xxxx=icaed_here.shape
	for i in range(0, len(day)):
		f.write(str(day[i])+' '+str(load[i])+' '+str(tmp[i]))
		for j in range(0, icaed_len):
			f.write(' '+str(icaed_here[j][i]))
		f.write('\n')
	f.close()
	
	f=open('cmd.plot','w')
	f.write('set term png font \'/usr/share/adobe/simsun.ttc,10\' size 1280,800\n')
	f.write('set output "./plot/'+name+'.png"\n')
	f.write('set output "./plot/'+name+'.png"\n')
	f.write('set size 1,1\n')
	f.write('set grid\n')
	f.write('set xlabel "从第一次测量开始的天数"\n')
	f.write('set ylabel "装载量"\n')
	f.write('set y2label "温度"\n')
#	f.write('set y3label "独立成分"\n')

	f.write('plot "tmpf.tmp" using 1:2 title "装载量" w lines axes x1y1, ')
	f.write('"tmpf.tmp" using 1:3 title "温度" w lines axes x1y1, ')
	for j in range(0, icaed_len):
		f.write('"tmpf.tmp" using 1:'+str(4+j)+' title "独立成分'+str(j+1)+'" w lines axes x1y2')
		if j!=icaed_len-1:
			f.write(', ')
	f.write(';\n')
	f.close()
	os.system('gnuplot cmd.plot')

gen_all_report()
#生成图形和newreport,给 mo1_cj 和 mo2_cj 赋值
plot_all_mc(argv[1],argv[2])
gen_paper(argv[1],argv[2])
mo1_pca,mo2_pca=do_fast_ica(True)
plot_icaed(mo_day, mo1_load, mo_tmp, mo1_pca, '41-pca')
plot_icaed(mo_day, mo2_load, mo_tmp, mo2_pca, '42-pca')

mo1_ica,mo2_ica=do_fast_ica(False)
plot_icaed(mo_day, mo1_load, mo_tmp, mo1_ica, '41-ica')
plot_icaed(mo_day, mo2_load, mo_tmp, mo2_ica, '42-ica')

mo1_tmp_vs_pca=compute_pearsonr(numpy.array(mo_tmp).T, mo1_pca)
mo2_tmp_vs_pca=compute_pearsonr(numpy.array(mo_tmp).T, mo2_pca)
mo1_tmp_vs_ica=compute_pearsonr(numpy.array(mo_tmp).T, mo1_ica)
mo2_tmp_vs_ica=compute_pearsonr(numpy.array(mo_tmp).T, mo2_ica)

mo1_day_vs_pca=compute_pearsonr(numpy.array(mo_day).T, mo1_pca)
mo2_day_vs_pca=compute_pearsonr(numpy.array(mo_day).T, mo2_pca)
mo1_day_vs_ica=compute_pearsonr(numpy.array(mo_day).T, mo1_ica)
mo2_day_vs_ica=compute_pearsonr(numpy.array(mo_day).T, mo2_ica)

mo1_load_vs_pca=compute_pearsonr(numpy.array(mo1_load).T, mo1_pca)
mo2_load_vs_pca=compute_pearsonr(numpy.array(mo2_load).T, mo2_pca)
mo1_load_vs_ica=compute_pearsonr(numpy.array(mo1_load).T, mo1_ica)
mo2_load_vs_ica=compute_pearsonr(numpy.array(mo2_load).T, mo2_ica)

print 'tmp VS PCA'
print mo1_tmp_vs_pca, mo2_tmp_vs_pca
print 'tmp VS ICA'
print mo1_tmp_vs_ica, mo2_tmp_vs_ica

print 'day VS PCA'
print mo1_day_vs_pca, mo2_day_vs_pca
print 'day VS ICA'
print mo1_day_vs_ica, mo2_day_vs_ica

print 'load VS PCA'
print mo1_load_vs_pca, mo2_load_vs_pca
print 'load VS ICA'
print mo1_load_vs_ica, mo2_load_vs_ica


