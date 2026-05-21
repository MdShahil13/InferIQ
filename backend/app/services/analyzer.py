import pandas as pd

def analyze_dataset(df):

    rows = df.shape[0]
    cols = df.shape[1]

    numeric_cols = len(
        df.select_dtypes(
            include="number"
        ).columns
    )

    categorical_cols = len(
        df.select_dtypes(
            include="object"
        ).columns
    )

    missing_values = (
        df.isnull().sum().sum()
    )

    analysis = {

        "rows": rows,
        "columns": cols,
        "numeric_columns": numeric_cols,
        "categorical_columns": categorical_cols,
        "missing_values": int(
            missing_values
        )
    }

    return analysis