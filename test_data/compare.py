# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 23:17:06 2018

@author: Fei
"""
import numpy as np
import matplotlib.pyplot as plt
from uncertainties import ufloat, unumpy, test_uncertainties

def String_to_float(string):
    try:
        aa =  string.split('(')
        a,b = float(aa[0]),float(aa[1][:-1])
    except:
        aa =  string.split('(')
        a,b = float(aa[0]),0
    return a,b

myK = ['124.6(0)','137.6(1.0)','176(8)','54.8(0.9)','117.9(1.6)']
PaperK = ['124.6(0)','136.3(2)','176(7)','60(0)','117.9(1.2)']



myG = ['86.4(0)','51.62(0.25)','103(5)','35.63(0.20)','70.13(0.33)']
PaperG = ['86.4(0)','51.2(0.2)','103(2.7)','36(0)','70.1(0.5)']

fig, ax = plt.subplots()
x    = [String_to_float(i)[0] for i in myK]
xerr = [10*String_to_float(i)[1] for i in myK]
y    = [String_to_float(i)[0] for i in PaperK]
yerr = [10*String_to_float(i)[1] for i in PaperK]

x1    = [String_to_float(i)[0] for i in myG]
x1err = [10*String_to_float(i)[1] for i in myG]
y1    = [String_to_float(i)[0] for i in PaperG]
y1err = [10*String_to_float(i)[1] for i in PaperG]

ax.errorbar(x, y, xerr=xerr, yerr=yerr,fmt='.', markersize='10', ecolor='red',)
ax.errorbar(x1, y1, xerr=x1err, yerr=y1err,fmt='.', markersize='10', ecolor='red',)

ax.set_title('for clarity all errors times 10')
ax.set_xlabel('my calc (GPa)')
ax.set_ylabel('Paper report (GPa)')
ax.set_xlim(30,250)
ax.set_ylim(30,250)
ax.plot([0,1000],[0,1000],'k')
fig.savefig('compare',dpi=200)


