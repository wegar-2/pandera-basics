import pandas as pd
import pandera as pa
from src.fts_types import FtsType
from src.fts_pa_schemas import SCHEMA_DICT


class FtsValidator:

    @staticmethod
    def validate(data: pd.DataFrame, fts_type: FtsType):
        schema = SCHEMA_DICT[fts_type]
        schema.validate(data)
