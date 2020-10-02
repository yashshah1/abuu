import os.path as path
from typing import Callable, Dict, Any

import pandas as pd

from .make_dataframe import make_dataframe

def get_dataloader(prefix: str) -> Callable[[str, Dict[str, Any]], pd.DataFrame]:
    def dataloader(name: str, **kwargs) -> pd.DataFrame:
        file_path = path.join(prefix, name)
        return make_dataframe(file_path, **kwargs)
    return dataloader