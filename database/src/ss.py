#! /usr/bin/env python
from genreport import *
from genplot import *
from genpaper import *
from sys import *

#gen_report('11','7','./dd.html',False)
gen_all_report()
plot_all_mc(argv[1],argv[2])
gen_paper(argv[1],argv[2])
