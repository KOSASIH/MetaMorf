import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

def plot_histogram(data, column, title=None):
    """
    Plot a histogram for a specific column of the input data.

    Args:
        data (pandas.DataFrame): The input data.
        column (str): The column to plot.
        title (str, optional): The title of the plot.

    Returns:
        None
    """
    data[column].plot(kind='hist', title=title)
    plt.show()

def plot_boxplot(data, column, title=None):
    """
    Plot a boxplot for a specific column of the input data.

    Args:
        data (pandas.DataFrame): The input data.
        column (str): The column to plot.
        title (str, optional): The title of the plot.

    Returns:
        None
    """
    data[column].plot(kind='box', title=title)
    plt.show()

def plot_scatterplot(data, x, y, title=None):
    """
    Plot a scatterplot for two specific columns of the input data.

    Args:
        data (pandas.DataFrame): The input data.
        x (str): The x-axis column.
        y (str): The y-axis column.
        title (str, optional): The title of the plot.

    Returns:
        None
    """
    data.plot(kind='scatter', x=x, y=y, title=title)
    plt.show()

def plot_heatmap(data, title=None):
    """
    Plot a heatmap for the correlation matrix of the input data.

    Args:
        data (pandas.DataFrame): The input data.
        title (str, optional): The title of the plot.

    Returns:
        None
    """
    corr = data.corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm', title=title)
    plt.show()

def plot_map(data, lat_column, lon_column, title=None):
    """
    Plot a map for the input data based on latitude and longitude columns.

    Args:
        data (pandas.DataFrame): The input data.
        lat_column (str): The latitude column.
        lon_column (str): The longitude column.
        title (str, optional): The title of the map.

    Returns:
        None
    """
    m = folium.Map(location=[data[lat_column].mean(), data[lon_column].mean()], zoom_start=5)
    for index, row in data.iterrows():
        folium.CircleMarker(location=(row[lat_column], row[lon_column]), radius=5, color='blue', fill=True, fill_color='blue', fill_opacity=0.6, popup=row['name']).add_to(m)
    m.save(title + '.html')
