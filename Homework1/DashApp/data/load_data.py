import pandas


def load_data_csv(path: str, cols_range: list[int]) -> pandas.DataFrame:
    data = pandas.read_csv(
        filepath_or_buffer=path,
        sep=";",
        decimal=",",
        usecols=cols_range
    )
    return data
