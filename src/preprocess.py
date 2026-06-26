import pandas as pd


def preprocess_input(
    data,
    make_encoder,
    feature_columns,
):
    """
    Preprocess user input before prediction.
    """

    df = pd.DataFrame([data])

    # Target Encoding
    df["make"] = df["make"].map(make_encoder)

    # Unknown brands
    df["make"] = df["make"].fillna(make_encoder.mean())

    # One Hot Encoding
    df = pd.get_dummies(df)

    # Match training columns
    df = df.reindex(columns=feature_columns, fill_value=0)

    return df