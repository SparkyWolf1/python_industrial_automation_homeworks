
def filter_data(
        data: list[dict],
        keys: list[str],
        search_col: str
        ) -> list[dict]:
    """Filter data based on search list"""
    filtered_data: list[dict] = list()
    for item in data:
        for key in keys:
            if (item[search_col] == key):
                filtered_data.append(item)
                print(
                    f"Searching: {item} "
                    + f"for {key} from {keys} in col "
                    + F"{item[search_col]}"
                    )

    return filtered_data
