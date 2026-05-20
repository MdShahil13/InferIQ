import pandas as pd
import numpy as np
import os

def clean_dataset(file_path):

    # Read CSV
    df = pd.read_csv(file_path)

    # Replace invalid values
    df.replace(
        ["N/A", "Unknown", "???"],
        np.nan,
        inplace=True
    )

    # Calculate noisy rows
    noisy_rows = (
        df.isnull()
        .any(axis=1)
        .sum()
    )

    total_rows = len(df)

    noise_percentage = (
        noisy_rows / total_rows
    ) * 100

    print(
        f"Noise %: {noise_percentage:.2f}"
    )

    # If noise is HIGH
    if noise_percentage > 10:

        print(
            "High noise detected → Filling values"
        )

        # Convert possible numeric columns
        for col in df.columns:

            try:
                df[col] = pd.to_numeric(
                    df[col]
                )

            except:
                pass

        # Numeric columns
        numeric_cols = (
            df.select_dtypes(
                include=np.number
            ).columns
        )

        for col in numeric_cols:

            mean_value = df[col].mean()

            df[col] = df[col].fillna(
                mean_value
            )

        # Categorical columns
        cat_cols = (
            df.select_dtypes(
                include="object"
            ).columns
        )

        for col in cat_cols:

            mode_value = (
                df[col]
                .mode()[0]
            )

            df[col] = df[col].fillna(
                mode_value
            )

    # LOW NOISE
    else:

        print(
            "Low noise detected → Removing rows"
        )

        df.dropna(inplace=True)

    # Output path
    output_path = os.path.join(
        "app",
        "uploads",
        "cleaned_data.csv"
    )

    # Save cleaned dataset
    df.to_csv(
        output_path,
        index=False
    )

    print(
        "Cleaned CSV generated!"
    )

    return output_path