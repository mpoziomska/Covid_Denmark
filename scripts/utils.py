# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 20:35:45 2021

@author: mpozi
"""
import pandas as pd
import numpy as np
from matplotlib.animation import PillowWriter
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import matplotlib
from bokeh.models.tools import HoverTool, BoxZoomTool, ResetTool, UndoTool, RedoTool, ZoomOutTool
from bokeh.plotting import figure, show, save
from bokeh.io import output_file
import datetime
import os

def gif_line_plot(x=[], y=[], title='', xlim=None, ylim=None, slow=None, ylabel='', xlabel='', yticks=[[], []], xticks=[[], []], write_path=None, sc=2):
    fig, ax = plt.subplots(figsize=(8 * sc, 5 * sc))
    matplotlib.rcParams.update({'font.size': 10 * sc})
    matplotlib.rcParams.update({'font.weight': 'normal'})
    matplotlib.rcParams['xtick.major.pad']='5'
    matplotlib.rcParams['ytick.major.pad']='8'
    
    IM = [plt.plot(x[0], y[0], linewidth=2 * sc, c='k')[0]]
    def init():
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        plt.title(title)
        plt.yticks(yticks[0], yticks[1])
        plt.xticks(xticks[0], xticks[1], rotation=45)
        plt.xlim(xlim)
        plt.ylim(ylim)
        plt.grid()
        
        return IM
        
    def animate(i):
        print(len(x[:i]))
        IM[0].set_data(x[:i], y[:i])
        return IM
    
    ani = animation.FuncAnimation(fig, animate, frames=len(x), init_func=init, interval=0.0000000001, blit=True, repeat=False)
    
    writer = PillowWriter(fps=50000000000)
    ani.save(write_path, writer=writer)
            
def line_plot_interactive(col = 'total_cases_per_million', countries = ['Denmark', 'United Kingdom', 'South Korea', 'China', 'Switzerland'], title = '', ylabel='', th = False, file='a', legloc='top_right'):
    
    with open('../data/BIG_CSV.csv') as f:
        p = pd.read_csv(f)
    
    if th:
        s = 1000
    else:
        s = 1
    p = p[p.date.notna() & p[col].notna()]
    
    y = []
    x = []
    for i in countries:
        A = p[p.location.isin([i])]
        y.append(np.array(A[col], dtype='float') / s)
        xx = []
        for i in A.index:
            a = A.date[i].split('-')
            xx.append(pd.to_datetime(datetime.date(int(a[0]), int(a[1]), int(a[2]))))
        x.append(xx)
    
    sc = 2
    p = figure(
        title=title,
        
        x_axis_type="datetime",
        #y_range=(0, 50),
       
        x_range=(pd.to_datetime(datetime.date(2020, 2, 1)), pd.to_datetime(datetime.date(2021, 4, 20))),
        sizing_mode="stretch_width",
        max_width=sc*500,
        plot_height=sc*250,
        toolbar_location="below"
    )
    p.title.align = "center"
    p.title.text_font_size = "25px"
    p.xaxis.axis_label = 'Date'
    p.yaxis.axis_label = ylabel
    # add renderers
    l = ['yellow', 'dimgray', 'darkkhaki', 'cadetblue', 'maroon']
    for i in range(len(x)):
        p.line(x[i], y[i], line_width=2, line_color = l[i], legend_label=countries[i], name=countries[i], muted_color=l[i], muted_alpha=0.2)
        
    p.legend.location = legloc
    p.legend.click_policy="mute"
    p.tools=[HoverTool(tooltips=[('Country', '$name'), ('Date', '@x{%F}'), (ylabel.replace(' in thousands', ''), '@y' + th * ' k')],
              formatters={'@x': 'datetime'}), ResetTool(), BoxZoomTool(), UndoTool(), RedoTool(), ZoomOutTool()]
    
    output_file("./../images/" + file + ".html")
    save(p)

def update_html():
    rep = ''
    
    
    l = os.listdir('./../images/')
    
    for i in l:
        if 'html' in i:
            with open('./../images/' + i) as f:
                rep += f.read()

    with open('./../report.html', 'w') as f:
        f.write(rep)
        
        #uk, szwecja, chiny, korea pd