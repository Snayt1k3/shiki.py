def filter_none_parameters(params: dict) -> dict:
    return {key: value for key, value in params.values() if value is not None}
