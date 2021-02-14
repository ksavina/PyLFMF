from PyLFMF import run
import numpy as np
from numpy.lib import recfunctions as rfn
import pandas as pd

arguments = ['h_tx', 'h_rx', 'freq',
             'power_tx', 'N', 'dist',
             'epsilon', 'sigma', 'polar']
# repr, str
err_msg = 'Incorrect input format. Run help(PyLFMF) for help.'

dt_in = np.dtype([
            ('h_tx', np.double), ('h_rx', np.double), ('freq', np.double),
            ('power_tx', np.double), ('N', np.double), ('dist', np.double),
            ('epsilon', np.double), ('sigma', np.double), ('polar', np.intc)
            ])

dt_out = np.dtype([('A', np.double), ('E', np.double), ('P', np.double),
                   ('method', np.intc), ('status', np.intc)])

def fromarray(data):
    if isinstance(data, list):
        data = np.array(data)
    try:
        data = data.reshape(-1, 9)
        data = rfn.unstructured_to_structured(data, dt_in)
    except:
        raise ValueError(err_msg)
    return data


def frompandas(df, mapper=None):
    if not isinstance(df, pd.DataFrame):
        raise ValueError(err_msg) 
    try:
        if mapper is not None:
            buf = []
            for arg in arguments:
                buf.append(mapper[arg])
            df = df[buf]
        else:
            df = df[arguments]
    except:
        raise ValueError("Mapping column names has failed.")
    df = fromarray(df.to_numpy())
    return df
            
def __fit(rec):
    return run([rec[arg].item() for arg in arguments])
  
def fit(data):
    buf = []
    for obs in data:
        obj = __fit(obs)
        buf.append((obj.A, obj.E, obj.P, obj.method, obj.status))
    return np.array(buf, dtype=dt_out)
