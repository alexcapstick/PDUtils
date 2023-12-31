import pandas as pd
import numpy as np
import typing as t


def fill_from_first_occurence(
    df: pd.DataFrame, subset: t.Union[t.List, str, None] = None, value: t.Any = 0
) -> pd.DataFrame:
    """
    This function fills each column in the subset
    in a dataframe with the value provided, from
    the first occurence

    This assumes that the dataframe is already
    sorted in the order in which you want to fill.


    Arguments
    ---------

    - df: pd.DataFrame:
        The dataframe to be filled.

    - subset: t.Union[t.List, str, None], optional:
        The subset of columns to fill.
        Defaults to :code:`None`.

    - value: t.Any, optional:
        The value to fill with.
        Defaults to :code:`0`.


    Raises
    ---------

        ValueError: If df is not a pandas dataframe.
        ValueError: If subset is not a list of strings.

    Returns
    --------

    - out: pd.DataFrame:
        The dataframe with the filled columns.


    """

    assert isinstance(df, pd.DataFrame), "df must be a pandas dataframe"

    df = df.copy()

    if subset is None:
        subset = df.columns
    elif type(subset) == str:
        subset = [subset]
    elif type(subset) != list:
        raise ValueError("subset must be a list of strings")

    for col in subset:
        first_index = df[col].first_valid_index()
        if first_index == None:
            continue
        df_temp = df.loc[first_index:, col]
        df_temp = df_temp.fillna(value)
        df.loc[first_index:, col] = df_temp

    return df


def explode_with_enumerate(
    df: pd.DataFrame, col: str, enumerate_name: str, start: int = 0
) -> pd.DataFrame:
    """
    Explodes a column in a dataframe and enumerates
    the values in the column. This allows you to
    keep track of the original order of the values.


    Arguments
    ---------

    - df: pd.DataFrame:
        The dataframe to be exploded.

    - col: str:
        The column to explode.

    - enumerate_name: str:
        The name of the column to contain
        the enumeration.

    - start: int, optional:
        The starting value of the enumeration.
        Defaults to :code:`0`.


    Returns
    --------

    - out: pd.DataFrame:
        The dataframe with the exploded column.

    """

    assert isinstance(df, pd.DataFrame), "df must be a pandas dataframe"
    assert isinstance(col, str), "col must be a string"
    assert isinstance(enumerate_name, str), "enumerate_name must be a string"

    df = df.copy()
    return df.assign(
        **{
            enumerate_name: lambda df: df[col].apply(lambda x: np.arange(len(x)))
            + start
        }
    ).explode([col, enumerate_name], ignore_index=False)
