import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Function to draw heatmap given a DataFrame input
def draw_heatmap(df):
    fig,ax = plt.subplots(figsize=(12,10))
    mask = np.triu(np.ones_like(df.corr()))
    ax = sns.heatmap(df.corr(),
                     vmin=-1,
                     vmax=1,
                     annot = True,
                     annot_kws={"size": 10},
                     linewidths=.25,
                     mask = mask,
                     square = True,
                     cmap = 'viridis',
                     cbar_kws = {'shrink' : .75})
    plt.title(f'Correlations between columns', fontsize = 20);

# Function to return percent change between two year lists
def pct_changer(scores_2017, scores_2018):
    return [(new - old)/old for new, old in zip(scores_2018, scores_2017)]

# Function to return standardized list
def standardizer(scores):
    mean = np.mean(scores)
    std = np.std(scores)
    return [((x-mean)/std) for x in scores]

# Removing commas and returning as ints
def remove_commas(x):
    return int(x.replace(',',''))

# Rounding to 2 decimal places after dividing by 1 million
def divide_million(x):
    return round(x/1000000.0,2)

# Some entries had a `.` to start the string, working around those
def remove_periods(x):
    return x[1:]

# Some entries had a '%' at the end of the string, working around those
def remove_pct(x):
    return int(x[:-1])

# Creating a function to 'manually' calculate the standard deviation
def stan_dev(col):
    return (sum([(np.mean(col) - x)**2 for x in col])/len(col))**0.5
