import pandas as pd
import typing as t


def collapse_levels(df: pd.DataFrame) -> pd.DataFrame:
    """
    This will collapse all of the levels in a multi-index dataframe
    and join them with an underscore.


    Arguments
    ---------

    - df: pd.DataFrame:
        The data frame to collapse.

    Returns
    --------

    - out: pd.DataFrame:
        The collapsed dataframe.


    """
    df_copy = df.copy()
    df_copy.columns = ["_".join(col).rstrip("_") for col in df_copy.columns.values]
    return df_copy


def lowercase_colnames(df: pd.DataFrame) -> pd.DataFrame:
    """
    This will turn all of the column names in a dataframe
    to lowercase and replace spaces with underscores.


    Arguments
    ---------

    - df: pd.DataFrame:
        The dataframe to format.


    Returns
    --------

    - out: pd.DataFrame:
        The formatted dataframe.


    """
    df_copy = df.copy()
    df_copy.columns = [col.lower().replace(" ", "_") for col in df_copy.columns.values]
    return df_copy
