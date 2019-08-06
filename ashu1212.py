
# coding: utf-8

# In[5]:


import pandas
import matplotlib
import plotly
plotly.tools.set_credentials_file(username='tiwari.ashutosh12345678', api_key='ib7AwlSfFJWEmJSegt8U')
from IPython.display import Markdown, display
def printmd(string):
    display(Markdown(string))
import plotly.plotly as py
import plotly.figure_factory as ff
import pandas as pd
from plotly.graph_objs import *
import ipywidgets as w
from IPython.display import display
def printmd(string, color=None):
    colorstr = "<span style='color:{}'>{}</span>".format(color, string)
    display(Markdown(colorstr))
p=True;
df=[]
d=0
io=0
processno=0;

while(p==True):
    if io==0:
        d=d+1
        print("Welcome to this plotly based program .")
        print("Follow the steps to get a gantt chart for your data !!")
        print(">> For adding job process type 1 || Else type 2 to plot details :")
        a=input()
        print('')
    if io>0:
        d=d+1
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(">> To add another job proccess type 1 || To view graph type 2 :")
        a=input()
        print('')
    if a=='1':
        io=io+1
        print("Type down the task name :")
        print('')
        taskname=input()
        print('')
        print("Start Date of  : :")
        print(f" {taskname} e.g yyyy-mm-dd : ")
        print('')
        start_date=input()
        print('')
        print("End Date of  : :")
        print(f"{taskname} e.g yyyy-mm-dd :")
        print('')
        end_date=input()
        print('')
        print('')
        print(f"Type Status of {taskname} e.g  (  notstarted  ,  ongoing  ,  completed )")
        print("Warning: Text is case sensitive")
        dr=input()
        print('')
        print('')
        processno=processno+1
        print("Processing ....")
        print(f"Process No {processno} is added to gantt chart")
        print(" ")
        print(" ")
        df.append(dict(Task=taskname,Start=start_date,Finish=end_date,Resource=dr))
    if a=='2':
        io=io+1
        p=False
colors = {'notstarted': 'rgb(220, 0, 0)',
          'ongoing': (1, 0.9, 0.16),
          'completed': 'rgb(0, 255, 100)'}
fig=ff.create_gantt(df,colors=colors,index_col='Resource', show_colorbar=True,bar_width=0.1, showgrid_x=True, showgrid_y=True, group_tasks=True)
plotly.offline.plot(fig,filename="ashuproject",auto_open=True)

