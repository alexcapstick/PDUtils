import pandas as pd
import typing as t


def groupby_freq(
    df: pd.DataFrame,
    groupby_cols: t.List[str],
    count_col: str,
    result_col: str = "freq",
) -> pd.DataFrame:
    """
    This function groups a dataframe by a list of columns and counts
    the number of occurrences of each group.


    Arguments
    ---------

    - df: pd.DataFrame:
        The dataframe to be grouped.

    - groupby_cols: _type_:
        The columns to group by.

    - count_col: _type_:
        The column to count.

    - result_col: str, optional:
        The name for the outputted column to have.
        Defaults to :code:`"freq"`.



    Returns
    --------

    - out: pd.DataFrame:
        The dataframe with the new column.


    """
    groupby_cols = list(groupby_cols)
    groupby_cols.append(count_col)

    return df.groupby(by=groupby_cols).size().to_frame(name=result_col)
