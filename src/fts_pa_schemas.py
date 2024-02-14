import pandas as pd
import pandera as pa
from src.fts_types import FtsType


DATE_INDEX = pa.Index(pa.Timestamp)
NONNEGATIVE_FLOAT_COL = pa.Column(pa.Float64, checks=pa.Check.ge(0))


SCHEMA_STOCK = pa.DataFrameSchema(
    index=DATE_INDEX,
    columns={
        "open": NONNEGATIVE_FLOAT_COL,
        "close": NONNEGATIVE_FLOAT_COL,
        "high": NONNEGATIVE_FLOAT_COL,
        "low": NONNEGATIVE_FLOAT_COL,
        "volume": NONNEGATIVE_FLOAT_COL
    }
)


SCHEMA_FX = pa.DataFrameSchema(
    index=DATE_INDEX,
    columns={
        "open": NONNEGATIVE_FLOAT_COL,
        "close": NONNEGATIVE_FLOAT_COL,
        "high": NONNEGATIVE_FLOAT_COL,
        "low": NONNEGATIVE_FLOAT_COL
    }
)

SCHEMA_EXCHANGE_FUTURES = pa.DataFrameSchema(
    index=DATE_INDEX,
    columns={
        "open": NONNEGATIVE_FLOAT_COL,
        "close": NONNEGATIVE_FLOAT_COL,
        "high": NONNEGATIVE_FLOAT_COL,
        "low": NONNEGATIVE_FLOAT_COL,
        "volume": NONNEGATIVE_FLOAT_COL,
        "openint": NONNEGATIVE_FLOAT_COL
    }
)


SCHEMA_DICT: dict[FtsType, pa.DataFrameSchema] = {
    FtsType.FX: SCHEMA_FX,
    FtsType.STOCK: SCHEMA_STOCK,
    FtsType.EXCHANGE_FUTURES: SCHEMA_EXCHANGE_FUTURES
}
