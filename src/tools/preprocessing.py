import pandas as pd
import numpy as np

def clean_data(data):
    """
    Clean the data by removing missing values and duplicates.

    Args:
        data (pandas.DataFrame): The input data.

    Returns:
        pandas.DataFrame: The cleaned data.
    """
    # Remove missing values
    data.dropna(inplace=True)

    # Remove duplicates
    data.drop_duplicates(inplace=True)

    return data

def transform_data(data, columns):
    """
    Transform the data by applying functions to specific columns.

    Args:
        data (pandas.DataFrame): The input data.
        columns (dict): The columns to transform and the corresponding functions.

    Returns:
        pandas.DataFrame: The transformed data.
    """
    for column, func in columns.items():
        data[column] = func(data[column])

    return data

def normalize_data(data, columns):
    """
    Normalize the data by scaling the values to a specific range.

    Args:
        data (pandas.DataFrame): The input data.
        columns (list): The columns to normalize.

    Returns:
        pandas.DataFrame: The normalized data.
    """
    for column in columns:
        data[column] = (data[column] - np.min(data[column])) / (np.max(data[column]) - np.min(data[column]))

    return data

def encode_categorical_data(data, columns):
    """
    Encode categorical data by mapping the categories to integers.

    Args:
        data (pandas.DataFrame): The input data.
        columns (list): The columns to encode.

    Returns:
        pandas.DataFrame: The encoded data.
    """
    for column in columns:
        data[column] = data[column].astype('category').cat.codes

    return data

def aggregate_data(data, columns, aggregation_functions):
    """
    Aggregate the data by applying functions to specific columns.

    Args:
        data (pandas.DataFrame): The input data.
        columns (list): The columns to aggregate.
        aggregation_functions (dict): The aggregation functions for each column.

    Returns:
        pandas.DataFrame: The aggregated data.
    """
    data_aggregated = data.groupby(columns).agg(aggregation_functions)

    return data_aggregated

def merge_data(data1, data2, on):
    """
    Merge two data frames based on a common column.

    Args:
        data1 (pandas.DataFrame): The first data frame.
        data2 (pandas.DataFrame): The second data frame.
        on (str): The common column.

    Returns:
        pandas.DataFrame: The merged data.
    """
    data_merged = pd.merge(data1, data2, on=on)

    return data_merged

def split_data(data, ratio):
    """
    Split the data into training and testing sets.

    Args:
        data (pandas.DataFrame): The input data.
        ratio (float): The ratio of the training set.

    Returns:
        tuple: The training and testing sets.
    """
    train_size = int(len(data) * ratio)
    train_data, test_data = data.iloc[:train_size], data.iloc[train_size:]

    return train_data, test_data
