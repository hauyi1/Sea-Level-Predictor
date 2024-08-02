import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='data')

    # Create first line of best fit
    regression = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], regression.intercept + regression.slope*df['Year'], label='Line of best fit')

    # Create second line of best fit
    df_recent = df[df['Year']>=2000]
    regress2 = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    plt.plot(df_recent['Year'], regress2.intercept + regress2.slope*df_recent['Year'], label='Line of best fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
