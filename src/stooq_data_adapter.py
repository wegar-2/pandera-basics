from src.fts_types import FtsType
from src.exceptions import NonExistentDataFileException
from src.fts_validator import FtsValidator
from pathlib import Path
import numpy as np
import pandas as pd


class StooqDataAdapter:

    @staticmethod
    def _get_data_path() -> Path:
        return Path(__file__).parent.parent / "data"

    @classmethod
    def _get_data_files(cls) -> list[str]:
        return [x.name for x in cls._get_data_path().iterdir() if x.is_file()]

    @staticmethod
    def _parse_raw_file(data: pd.DataFrame) -> pd.DataFrame:
        data.columns = [x.lower() for x in data.columns]
        data = data.set_index("date").sort_index(axis=0, ascending=True)
        for c in data.columns:
            data[c] = data[c].astype(np.float64)
        data = data.loc[~data.isna().any(axis=1), :]
        return data

    @classmethod
    def load_file(cls, fname: str, fts_type: FtsType) -> pd.DataFrame:
        if f"{fname}.csv" not in cls._get_data_files():
            raise NonExistentDataFileException(fname=fname)
        data = cls._parse_raw_file(
            data=pd.read_csv(cls._get_data_path() / f"{fname}.csv", parse_dates=["Date"], date_format="%Y-%m-%d"))
        FtsValidator.validate(data=data, fts_type=fts_type)
        return data
