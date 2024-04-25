import pandas as pd
import numpy as np
import preprocessing as pp
import visualization as vis
import analysis as an
import modeling as md

def load_data(file):
    """
    Load the data from a file.

    Args:
        file (str): The file path.

    Returns:
        pandas.DataFrame: The loaded data.
    """
    data = pd.read_csv(file)

    return data

def preprocess_data(data):
    """
    Preprocess the data by cleaning, transforming, and normalizing.

    Args:
        data (pandas.DataFrame): The input data.

    Returns:
        pandas.DataFrame: The preprocessed data.
    """
    data_cleaned = pp.clean_data(data)
    data_transformed = pp.transform_data(data_cleaned, pp.transformations)
    data_normalized = pp.normalize_data(data_transformed, pp.columns)

    return data_normalized

def visualize_data(data, columns):
    """
    Visualize the data by plotting histograms, boxplots, scatterplots, heatmaps, and maps.

    Args:
        data (pandas.DataFrame): The input data.
        columns (list): The columns to visualize.

    Returns:
        None
    """
    vis.plot_histogram(data, columns[0])
    vis.plot_boxplot(data, columns[1])
    vis.plot_scatterplot(data, columns[2], columns[3])
    vis.plot_heatmap(data)
    vis.plot_map(data, 'latitude', 'longitude')

def analyze_data(data):
    """
    Analyze the data by computing statistics, correlations, and trends.

    Args:
        data (pandas.DataFrame): The input data.

    Returns:
        None
    """
    an.compute_statistics(data)
    an.compute_correlations(data)
    an.compute_trends(data)

def model_data(data):
    """
    Model the data by training and testing predictive models.

    Args:
        data (pandas.DataFrame): The input data.

    Returns:
        None
    """
    X_train, X_test, y_train, y_test = md.split_data(data, 0.7)
    model = md.train_model(X_train, y_train)
    predictions = md.test_model(model, X_test, y_test)
    md.evaluate_model(predictions, y_test)
