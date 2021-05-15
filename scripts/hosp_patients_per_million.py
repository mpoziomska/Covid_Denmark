from utils import *

line_plot_interactive(col = 'owid-covid-data_hosp_patients_per_million', 
                      countries = ['Denmark', 'United Kingdom'], 
                      title = "hosp_patients_per_million", 
                      ylabel='Total deaths', 
                      th = False, 
                      file='hosp_patients_per_million', 
                      legloc='top_left')

update_html()