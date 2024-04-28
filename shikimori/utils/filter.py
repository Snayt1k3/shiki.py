def filter_none_parameters(params: dict) -> dict:
    return {key: value for key, value in params.items() if value is not None}


def handle_none_data(func):
    def wrapper(*args, **kwargs):
        data = args[1]

        if data is None:
            return None

        return func(*args, **kwargs)

    return wrapper
