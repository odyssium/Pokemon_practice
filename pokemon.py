# -*- coding: utf-8 -*-
"""
Created on Wed Jun 06 22:38:46 2018

@author: odyssium
"""

import os
import sys
import time
import re
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly as py
import seaborn as sns

#%%

parser = argparse.ArgumentParser(usage ="pokemon.py" ,description="a practice program for interactive data analysis")
parser.add_argument("directory", help="file directory")
parser.add_argument("filename", help="file name.xlxs")
parser.add_argument("-t", help="type of pokemon (), Grass, Fire, Water, Bug, Normal, Poison, Eletric, Ground, Psychic...", dest="type", default="[a-zA-Z]+")
parser.add_argument("-p", help="type of plot =  “scatter” | “reg” | “resid” | “kde” | “hex”", dest="plot", default="scatter")
parser.add_argument("-vx", help="value1 for plotting= total | HP | Attack | Defense | SpAtk | SpDef | Speed | Stage", dest="vx", default="Attack")
parser.add_argument("-vy", help="value2 for plotting= total | HP | Attack | Defense | SpAtk | SpDef | Speed | Stage", dest="vy", default="Defense")

args = parser.parse_args()
#print(args.directory)
#print(args.filename)
#print(args.type)
#print(args.plot)

#%%

def log(file):
    f = open(file +'_log.txt', 'w')
    f.write('analysis start at' +time.strftime("%Y%m%d_%H%M%S", time.localtime()) + '\r\n\r\n')
    f.write('input file =' +file)
    f.close

dir = sys.argv
os.chdir(dir[1])
filename = dir[2]
log(filename)
file = pd.read_excel(dir[2])

gStat1 = file.Type1.value_counts()
#gStat2 = file.Type2.value_counts()

print(gStat1)

# plot style setting
sns.set_style('whitegrid')
sns.despine()

ptp = args.plot
patt = args.type
vv1 = args.vx
vv2 = args.vy
#%%
fig, axs = plt.subplots(2, 1, figsize = (6,12))
ax1 = plt.subplot2grid((2, 1), (0, 0))
ax2 = plt.subplot2grid((2, 1), (1, 0))
#plot1 = sns.regplot(x="Attack", y="Defense", data=file[file.Type1.str.contains("Grass")], ax=ax1)
#plot1 = sns.stripplot(x="Type1", y="Attack", data=file, ax=ax2)

#%%
plot1 = sns.regplot(x=vv1, y=vv2, data=file[file.Type1.str.contains(patt)], ax=ax1)
plot1.set_title("type of Pokemon : {}".format(patt))
plot1 = sns.boxplot(x="Type1", y=vv1, data=file, ax=ax2)

#%%
plot2 = sns.jointplot(x=vv1, y=vv2, data=file[file.Type1.str.contains(patt)], kind=ptp)

#%%

fig1 = plot1.get_figure()
fig1.savefig('result1.png')

plot2.fig.savefig('result2.png')


