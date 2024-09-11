import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col= 'date')
df.index = pd.to_datetime(df.index)
# Clean data
upper_percent = df['value'].quantile(0.975)
lower_percent = df['value'].quantile(0.025)
df = df[
    (df['value'] > lower_percent) &
    (df['value'] < upper_percent)
    ]

def draw_line_plot():
#       Setting up the figure
    lineplot_df = df.copy()
    fig = plt.figure(figsize=(14, 4))
    ax = plt.gca()
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
#       Generating the figure
    dates = lineplot_df.index
    values = lineplot_df['value']
    ax.plot(dates, values, color= 'red')

#       Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    fig, ax = plt.subplots(figsize=(8, 8))
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    monthly_avg = df_bar.groupby(['year', 'month'])['value'].transform('mean')
    df_bar['monthly_avg'] = monthly_avg

    # Draw bar plot
    sns.barplot(data= df_bar, x= df_bar['year'], y= 'monthly_avg', hue= df_bar['month'], palette= 'tab10')

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    
    handles, labels = ax.get_legend_handles_labels()  # Get current legend labels
    ax.legend(handles=handles, labels=month_names, title='Months', loc='upper left')

    ax.set_xlabel('Years')
    plt.xticks(rotation= 90)
    ax.set_ylabel('Average Page Views')
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)





    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
