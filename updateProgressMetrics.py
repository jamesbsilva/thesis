#!/usr/bin/env python
"""
	updateProgressMetric.py

	updates the plots and data for pagecount, wordcount etc

----------

	-jbsilva
"""

import sys;
import datetime;
import pandas as pd;
import matplotlib as mpl;
import numpy as np;
import pandas as pd;
import pylab as plt;
import seaborn as sns;
import os;

# presets for plots
fontTitle = {'fontname':'Lucid','fontsize':30, 'fontweight':'bold'}; fontAxis = {'fontname':'Lucid','fontsize':24, 'fontweight':'bold'};
sns.set_style("whitegrid"); sns.set_palette("deep", desat=.6); sns.set_context(rc={"figure.figsize": (14, 12)})
mpl.rcParams['figure.facecolor'] = "white"

outFolder = "ProgressMetrics/";
pageFile = outFolder+"pageData.csv"; wrdsTFile = outFolder+"wrdsTData.csv"; wrdsHFile = outFolder+"wrdsHData.csv";

def seabornScatterPlot(data,xName,yName,titleIn):
    '''
        seabornScatterPlot plots a scatter plot using seaborn.

    :param X: x axis data
    :param Y: y axis data
    :param xName: name of x axis
    :param yName: name of y axis
    :param titleIn: plot title
    '''
    sns.lmplot(xName, yName, data, palette="Set1", fit_reg=False);
    plt.title(titleIn);

def regScatterPlot(data,xName,yName,titleIn,xaxis='',yaxis=''):
    '''
        seabornScatterPlot plots a scatter plot using seaborn.

    :param X: x axis data
    :param Y: y axis data
    :param xName: name of x axis
    :param yName: name of y axis
    :param titleIn: plot title
    '''
    plt.plot(data[xName], data[yName],'o-');
    plt.xlabel(xaxis); plt.ylabel(yaxis);
    plt.title(titleIn);
    plt.xlim([np.min(data[xName])-5,np.max(data[xName])+5]);

def updatePageData(day,pages):
    if not os.path.exists(pageFile):
        f = open(pageFile,'w');
        f.write("dayOfYear,PagesCompleted\n");
        f.close();

    data = pd.read_csv(pageFile);
    dataArr = data.as_matrix();
    data.index.names = ['Id'];
        
    updating = True;
    for u in range(dataArr.shape[0]):
        dayOfYear = dataArr[u][0]; pagesCurr = dataArr[u][1]; 
        if dayOfYear == day:
            dataArr[u][1] = pages; updating = False;

    if updating:
        dataArr = np.vstack([ dataArr, [day,pages] ])
 
    data = pd.DataFrame(dataArr,columns=data.columns.tolist());
    data.to_csv(pageFile,index=None);
    data = data.astype(np.float);

    return data;

def updateWordsData(day,words,headerWords=False):
    if not headerWords:
        wFile = wrdsTFile;
    else:
        wFile = wrdsHFile;
    if not os.path.exists(wFile):
        f = open(wFile,'w');
        f.write("dayOfYear,Words\n");
        f.close();
    data = pd.read_csv(wFile);
    data.index.names = ['Id'];
    updating = True;
    for datRow in data.iterrows():
        dat = datRow[1]
        if dat["dayOfYear"] == day:
            dat["Words"] = words; updating = False;
    if updating:
        data.loc[len(data.index)] = [day,words];
    data.to_csv(wFile,index=None);
    data = data.astype(np.float);
    return data;

for i in range(1,len(sys.argv)):
    numIn = sys.argv[i].split()
    if i == 1:
        pages = numIn[len(numIn)-1]
    elif i == 2:
        wrdsH = numIn[len(numIn)-1]
    elif i == 3:
        wrdsT = numIn[len(numIn)-1]

day = datetime.datetime.now().timetuple().tm_yday
curryear = datetime.datetime.now().year
day = day + 365*(int(curryear)-2015)

pgData = updatePageData(day,pages)
fitStart = pgData['dayOfYear'][pgData.shape[0]-7]

pgDataSub = pgData[pgData['dayOfYear'] > fitStart]
p = np.polyfit(pgDataSub['dayOfYear'], pgDataSub['PagesCompleted'],1);
endDate = (120-p[1])/p[0]
maxDate = pgData['dayOfYear'].max()
print "Projected End 120 pgs : ",endDate

wrdsHData = updateWordsData(day,wrdsH,headerWords=True)
wrdsTData = updateWordsData(day,wrdsT,headerWords=False)

seabornScatterPlot(pgData,"dayOfYear","PagesCompleted","Thesis Pages Completed")
plt.savefig(outFolder+"PagesCompleted.png")
plt.clf()
regScatterPlot(pgData,"dayOfYear","PagesCompleted","Thesis Pages Completed",xaxis="dayOfYear",yaxis="PagesCompleted")
plt.savefig(outFolder+"PagesCompleted_alt.png")
plt.clf()
plt.xlim([fitStart,maxDate+20])
plt.plot([fitStart,maxDate+20],[fitStart*p[0]+p[1],(maxDate+20)*p[0]+p[1]],'-')
plt.savefig(outFolder+"PagesCompleted_short.png")
seabornScatterPlot(wrdsHData,"dayOfYear","Words","Thesis Words In Headers Completed")
plt.savefig(outFolder+"WordsHeaderCompleted.png")
seabornScatterPlot(wrdsTData,"dayOfYear","Words","Thesis Words Completed")
plt.savefig(outFolder+"WordsCompleted.png")
regScatterPlot(wrdsTData,"dayOfYear","Words","Thesis Words Completed",xaxis="dayOfYear",yaxis="WordsCompleted")
plt.savefig(outFolder+"WordsCompleted_alt.png")


