from utils import *

line_plot_interactive(col = 'owid-covid-data_positive_rate', 
                      countries = ['Denmark', 'United Kingdom', 'South Korea', 'Switzerland'], 
                      title = "Positive rate", 
                      ylabel='Positive rate', 
                      th = False, 
                      file='positive_rate_interactive', 
                      legloc='top_right')


update_html()