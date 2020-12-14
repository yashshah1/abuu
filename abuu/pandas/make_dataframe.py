import os
import pandas as pd

def make_dataframe(path: str, **kwargs) -> pd.DataFrame:
    ext = os.path.splitext(path)[1][1::]
    kw = {}
    if ext == "csv":
        fn = pd.read_csv
        kw = {**kw, "low_memory": False}
    elif ext in ("xls", "xlsx"):
        fn = pd.read_excel
    elif ext in ("pkl", "pickle"):
        fn = pd.read_parquet
    else:
        raise ValueError("Currently only csv, xls, xlsx, pkl and pickle files are supported")
    kwargs = {**kw, **kwargs}
    return fn(path, **kwargs)    
