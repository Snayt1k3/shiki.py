def filter_none_parameters(params: dict) -> dict:
    return {key: value for key, value in params.items() if value is not None}
