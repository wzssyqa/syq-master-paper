#! /usr/bin/env python
# -*- coding: utf-8 -*-
import mdp
from genreport import *
from genplot import *
from genpaper import *
from sys import *
import numpy
#两个末煤仓的沉降
#使用全局变量，有点脏
#定义在 genplot.py 文件中
#mo1_cj=[]
#mo2_cj=[]
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

#gen_report('11','7','./dd.html',False)

gen_all_report()
#生成图形和newreport,给 mo1_cj 和 mo2_cj 赋值
plot_all_mc(argv[1],argv[2])
gen_paper(argv[1],argv[2])
do_fast_ica(True)
do_fast_ica(False)

