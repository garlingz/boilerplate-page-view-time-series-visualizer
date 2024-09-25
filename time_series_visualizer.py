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
   def draw_bar_plot():
    fig, ax = plt.subplots(figsize=(8, 8))
    # Organizing information
    #   Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    #   Defining months/years
    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
                   'July', 'August', 'September', 'October', 'November', 'December']
    unique_years = df_bar['year'].unique()

    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()


    # Draw bar plot
    df_bar.plot(kind= 'bar', ax=ax)


    

    # Configure axis labels and ticks
    ax.legend(title= 'Months', labels= month_names, loc= 'upper left')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.set_xticks(range(len(df_bar.index)))
    ax.set_xticklabels(unique_years, rotation=90)


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig
def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Changing data type to float for value, and categorical for months
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['value'] = df_box['value'].astype(float)
    df_box['month'] = pd.Categorical(df_box['month'], categories= months, ordered= True)

    # Creating the Years/Months
    years = sorted(df_box['year'].unique())
    year_data = [df_box[df_box['year'] == year]['value'] for year in years]
    month_data = [df_box[df_box['month'] == month]['value'] for month in months]

    # Figure setup
    fig, axes = plt.subplots(1, 2, figsize= (14, 6))
    palette = sns.color_palette('husl', 12)
    # First boxplot
    sns.boxplot(df_box, x= 'year', y= 'value', palette= 'tab10', ax= axes[0], flierprops=dict(marker='.', markersize= 2))
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    # Second boxplot
    sns.boxplot(df_box, x= 'month', y= 'value', ax= axes[1], flierprops=dict(marker='.', markersize= 2), palette= palette, legend= False)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
