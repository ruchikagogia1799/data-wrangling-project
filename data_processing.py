# data_processing.py
"""
Data Processing Functions
Author: Your Name
Description: Functions for loading, cleaning, and transforming data.
"""

import pandas as pd

def load_data(filepath):
    """
    Load CSV data from the given filepath.

    Parameters:
    filepath (str): Path to the CSV file.

    Returns:
    DataFrame: Pandas DataFrame containing the loaded data.
    """
    return pd.read_csv(filepath)

def clean_data(df):
    """
    Clean the given DataFrame by removing unnecessary columns, 
    handling missing values, and stripping whitespace.

    Parameters:
    df (DataFrame): Input DataFrame.

    Returns:
    DataFrame: Cleaned DataFrame.
    """
    # Drop irrelevant columns if present
    columns_to_drop = ['Case Number.1', 'href', 'original order']
    df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True, errors='ignore')
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Strip column names
    df.columns = df.columns.str.strip()

    return df
