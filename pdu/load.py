import typing as t
import pandas as pd
import numpy as np


def load_nested_dict_to_pandas(
    results_dict: t.Dict[t.Any, t.Any],
    level_names: t.List[t.Any] = None,
) -> pd.DataFrame:
    """
    This function loads a nested dictionary into a pandas DataFrame.

    Arguments
    ----------

    - results_dict : dict
        The nested dictionary to load.

    - level_names : list
        The names of the levels in the dictionary.
        This can be used to name the columns of the
        outputted :code:`DataFrame`.
        Defaults to :code:`None`.

    Returns
    --------

    - df : DataFrame
        The pandas DataFrame with the nested dictionary loaded.

    """

    # internal function to call recursively
    def internal_load_nested_dict_to_pandas(results_dict, level, level_names):
        df = pd.DataFrame()
        level = level + 1
        for key in results_dict.keys():
            if isinstance(results_dict[key], dict):
                df_output = internal_load_nested_dict_to_pandas(
                    results_dict[key], level, level_names
                )
                if level_names is None:
                    df_output = df_output.assign(**{f"level_{level}": key})
                else:
                    df_output = df_output.assign(**{level_names[level]: key})
                df = pd.concat([df, df_output])
            else:
                try:
                    df[key] = [results_dict[key]]
                except:
                    df[key] = np.nan
        return df

    return internal_load_nested_dict_to_pandas(
        results_dict=results_dict, level=-1, level_names=level_names
    )
