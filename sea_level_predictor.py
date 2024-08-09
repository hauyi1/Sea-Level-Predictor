import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(x, y, label='data')
    
    # Create first line of best fit
    regression = linregress(x, y)
    x_prediction = pd.Series([i for i in range(1880, 2051)])
    y_prediction = regression.intercept + regression.slope*x_prediction
    plt.plot(x_prediction, y_prediction, label='Line of best fit')
    
    # Create second line of best fit
    df_recent = df[df['Year']>=2000]
    y_2 = df_recent['CSIRO Adjusted Sea Level']
    x_2 = df_recent['Year']
    regression_2 = linregress(x_2, y_2)
    x_prediction_2 = pd.Series([i for i in range(2000, 2051)])
    y_prediction_2 = regression_2.intercept + regression_2.slope * x_prediction_2
    plt.plot(x_prediction_2, y_prediction_2, label='Line of best fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
