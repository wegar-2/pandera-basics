from src.fts_types import FtsType
from src.stooq_data_adapter import StooqDataAdapter
import pandas as pd


if __name__ == "__main__":

    data_configs: list[tuple[str, FtsType]] = [
        ("eurpln_d", FtsType.FX),
        ("tsla_us_d", FtsType.STOCK),
        ("fw20_d", FtsType.EXCHANGE_FUTURES)
    ]

    datas: dict[str, pd.DataFrame] = {}

    for fname, fts_type in data_configs:
        datas[fname] = StooqDataAdapter.load_file(fname=fname, fts_type=fts_type)

    print(datas["eurpln_d"])
    print(datas["tsla_us_d"])
    print(datas["fw20_d"])
