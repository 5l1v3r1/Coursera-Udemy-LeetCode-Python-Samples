'''
Applied Plotting, Charting & Data Representation in Python
University of Michigan
Week3-Assigment3
Building a Custom Visualization

In this assignment you must choose one of the options presented below and submit a visual as well as your source code for peer grading. The details of how you solve the assignment are up to you, although your assignment must use matplotlib so that your peers can evaluate your work. The options differ in challenge level, but there are no grades associated with the challenge level you chose. However, your peers will be asked to ensure you at least met a minimum quality for a given technique in order to pass. Implement the technique fully (or exceed it!) and you should be able to earn full grades for the assignment.
Ferreira, N., Fisher, D., & Konig, A. C. (2014, April). Sample-oriented task-driven visualizations: allowing users to make better, more confident decisions.       In Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 571-580). ACM. (video)
In this paper the authors describe the challenges users face when trying to make judgements about probabilistic data generated through samples. As an example, they look at a bar chart of four years of data (replicated below in Figure 1). Each year has a y-axis value, which is derived from a sample of a larger dataset. For instance, the first value might be the number votes in a given district or riding for 1992, with the average being around 33,000. On top of this is plotted the 95% confidence interval for the mean (see the boxplot lectures for more information, and the yerr parameter of barcharts).
A challenge that users face is that, for a given y-axis value (e.g. 42,000), it is difficult to know which x-axis values are most likely to be representative, because the confidence levels overlap and their distributions are different (the lengths of the confidence interval bars are unequal). One of the solutions the authors propose for this problem (Figure 2c) is to allow users to indicate the y-axis value of interest (e.g. 42,000) and then draw a horizontal line and color bars based on this value. So bars might be colored red if they are definitely above this value (given the confidence interval), blue if they are definitely below this value, or white if they contain this value.


'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as col
import matplotlib.cm as cm

%matplotlib notebook

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])

### Preparing Data
df_mean = np.mean(df,axis=1) #calculate the means of df
df_std = np.std(df,axis=1) #calculate the standard deviations (std) of df
n = df.shape[1] #number of column size=total count of values for rows
z=1.96 # z value is equel to 1.96 because of n>30
df_yerr = 1.96 * (df_std/np.sqrt(n)) # compute the 95% confidence intervals
                                # for adding error bars (CI) with yerr parameter    
r=range(df.shape[0]) # The x position of bars in plot

### Setup The Plot
plt.figure(figsize=(8,7))
bars = plt.bar(r, df_mean, yerr = df_yerr, capsize=7, color = 'grey')

### Add Title, Label, xticks
plt.xticks(r, df.index)
plt.title('Random Data Between 1992 - 1995')

### Dejunkifying Plot
[plt.gca().spines[loc].set_visible(False) for loc in ['top', 'right']] #Remove top and right frame

### OPTIONS ###
borderline = 42000 #defined in the instruction

# Add The borderline as a ytick
plt.axhline(y = borderline, zorder=1, linewidth=2, color='black',ls='--')
ytick = plt.gca().get_yticks()
ytick = np.append(ytick,borderline)
plt.gca().set_yticks(ytick)

#Setup Colormap
colormap = col.LinearSegmentedColormap.from_list("colormap",["blue", "white","red"])
cpick = cm.ScalarMappable(cmap=colormap)
cpick.set_array([])

#Add the colorbar
plt.colorbar(cpick, orientation='horizontal', boundaries=np.linspace(0,1,100))

#Arrange the Bar Color From the borderline
color_loc = []
for mean,yerr in zip(df_mean,df_yerr):
    ci_up=mean+yerr
    ci_down=mean-yerr
    if borderline<ci_down:
        temp=1
    elif borderline>ci_up:
        temp=0
    else:
        temp=(borderline-ci_down)/(ci_up-ci_down)
    color_loc.append(temp)
color_loc

##
import ipywidgets as widgets
widget=widgets.IntSlider(value=borderline,
    min=30000,
    max=60000,
    step=500,
    description='borderline',
    disabled=False,
    continuous_update=False,
    orientation='vertical',
    readout=True)
widget

#Updating the plot 
bars = plt.bar(r, df_mean, yerr = df_yerr, capsize=7, color = cpick.to_rgba(color_loc))

plt.show()