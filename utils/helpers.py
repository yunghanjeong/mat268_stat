import numpy as np
import pandas as pd
import os

def load_data(data_suffix: int,
              data_prefix: str='data_',
              data_dir='..//data',
              **kwargs) -> pd.DataFrame:
    """
    function to help load data easily.
    pass kwargs for pd.read_csv
    """
    filename = ''.join([data_prefix, str(data_suffix), '.csv'])
    filepath = os.path.join(data_dir, filename)
    df = pd.read_csv(filepath, **kwargs)
    return df

def find_mode(values: pd.Series):
    """
    finds the mode 
    returns mode as an array when found since there could
    be more than 1 mode.
    if no mode if found return none
    """
    if values[values.duplicated()].any():
        repeats = values.duplicated(keep=False)
        # get repeats as a dataframe
        repeated = values[repeats].reset_index()
        # group by values and count
        repeat_count = repeated.groupby(0).count()['index']
        repeat_max = repeat_count.max()
        mode = repeat_count[repeat_count == repeat_max].index
        return mode.values
    else:
        return None
    
def measure_ctv(values: pd.Series) -> tuple:
    """
    Given a pandas series of values return a tuple consisting of
    mean, median, mode, midrange
    """
    
    mean = values.mean()
    median = values.median()
    midrange = (values.max() + values.min()) / 2
    mode = find_mode(values)
    return mean, median, mode, midrange