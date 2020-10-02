import os
import pandas as pd

def make_dataframe(path: str, **kwargs) -> pd.DataFrame:
    ext = os.path.splitext(path)[1][1::]
    if ext == "csv":
        fn = pd.read_csv
    elif ext in ("xls", "xlsx"):
        fn = pd.read_excel
    elif ext in ("pkl", "pickle"):
        fn = pd.read_parquet
    else:
        raise ValueError("Currently only csv, xls, xlsx, pkl and pickle files are supported")
    return fn(path, **kwargs)    
