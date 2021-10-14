import pandas as pd
import plotly.figure_factory
import csv

df=pd.read_csv('data1.csv')
fig = ff.create_distplot([df["Avg rating of the brand(No)"].tolist()], ["name of the bell-curve"], show_hist=False)
fig.show()

z_score=(mean_of_sample1-mean)/std_deviation