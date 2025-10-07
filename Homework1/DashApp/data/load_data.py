import pandas


def load_data_csv(path: str) -> pandas.DataFrame:
    data = pandas.read_csv(
        filepath_or_buffer=path
    )
    return data
