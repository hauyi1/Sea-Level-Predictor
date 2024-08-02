import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    regression = stats.linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='data')



    # Create first line of best fit
    plt.plot(df['Year'], regression.intercept + regression.slope*df['Year'], label='Line of best fit')

    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
