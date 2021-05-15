from utils import *

line_plot_interactive(col = 'total_cases_per_million', countries = ['Denmark', 'United Kingdom', 'South Korea', 'Switzerland', 'China'], title = "Total cases of covid-19 per million", ylabel='Total cases per million in thousands', th = True, file='total_cases_interactive', legloc='top_left')

update_html()