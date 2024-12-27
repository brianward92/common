import pandas as pd


def read(path):
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith(".parquet"):
        return pd.read_parquet(path)
    else:
        raise NotImplementedError(f"Unsupported file type: {path=}.")


def write(data, path):
    if path.endswith(".csv"):
        data.to_csv(path)
    elif path.endswith(".parquet"):
        data.to_parquet(path)
    else:
        raise NotImplementedError(f"Unsupported file type: {path=}.")
    return 0
