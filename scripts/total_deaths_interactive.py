from utils import *

line_plot_interactive(col = 'total_deaths_per_million', 
                      countries = ['Denmark', 'United Kingdom', 'South Korea', 'Switzerland', 'China'], 
                      title = "Total deaths per million", 
                      ylabel='Total deaths', 
                      th = False, 
                      file='total_deaths_interactive', 
                      legloc='top_left')

update_html()