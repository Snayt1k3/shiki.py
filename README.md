# Shikimori API Wrapper


A Python library that provides a simple and easy-to-use wrapper for accessing the [Shikimori API](https://shikimori.one/api/doc). The library supports all endpoints and types of the Shikimori API and provides OAuth2 authorization functionality using an access token.

[![Build Status](https://img.shields.io/github/actions/workflow/status/Snayt1k3/shiki.py/build.yml)](https://github.com/Snayt1k3/shiki.py/actions/)
[![License](https://img.shields.io/github/license/snayt1k3/shiki.py)](https://github.com/Snayt1k3/shiki.py/LICENSE)
[![Coverage Status](https://coveralls.io/repos/github/Snayt1k3/shiki.py/badge.svg?branch=master)](https://coveralls.io/github/Snayt1k3/shiki.py?branch=master)
[![Documentation Status](https://readthedocs.org/projects/shikipy/badge/?version=latest)](https://shikipy.readthedocs.io/en/latest/?badge=latest)
  
## Features

- **Support for all Shikimori API endpoints**: This library supports all endpoints (both v1 and v2) of the Shikimori API, including anime, manga, characters, users, and more.
- **Authorization support**: The library provides support for authorization using an access token.
- **Strong typing**: The library has type hints for all methods, making it easy to integrate with other projects.
- **Easy-to-use API**: The API wrapper is designed to be simple and easy to use, with intuitive methods and parameters that make it easy to get started quickly.

## Documentation
See the shiki.py [API documentation](https://shikipy.readthedocs.io/en/latest/) .

See the [official documentation](https://shikimori.one/api/doc) for the Shikimori API.

## Installation
#### pip
```sh
$ pip install shiki.py
```
#### poetry
```sh
$ poetry add shiki.py
```

## Usage
To use the library, simply import it into your project and create an instance of a `Shikimori`. You can then use the various methods provided by the `Shikimori` to access the Shikimori API.

```python
import asyncio

from shikimori.client import Shikimori

client = Shikimori(user_agent="USER_AGENT")

async def main():
    return await client.anime.list()

if __name__ == "__main__":
    asyncio.run(main())
```

## Authorization
For more additional information see the [Official Shikimori OAuth2 Guide](https://shikimori.one/oauth).

1. **Register your [Shikimori Application](https://shikimori.one/oauth/applications):** This will provide you with a `client_id` and `client_secret` that you will need to use OAuth2.

2. **Redirect user to the Shikimori authorization endpoint:** This endpoint will prompt the user to grant your application access to their resources. After the user grants access, Shikimori will redirect them back to your application with an *authorization code*.
```
https://shikimori.one/oauth/authorize?client_id=CLIENT_ID&redirect_uri=REDIRECT_URI&response_type=code&scope=
```

3. **Get an access token:** Your application will need to exchange an *authorization code* for an `AccessToken`. Shikimori will respond with an access token that your application can use to access the restricted resources/endpoints.
```python
import asyncio

from shikimori.client import Shikimori

client = Shikimori(user_agent="USER_AGENT")

async def main():
    return await client.auth.get_access_token("CODE")

if __name__ == "__main__":
    asyncio.run(main())
```

4. **Use access token to access protected resources:** Finally, your application can use the access token to access the user's protected resources. Be sure to handle any errors or expired tokens gracefully.
```python
import asyncio

from shikimori.client import Shikimori

client = Shikimori(user_agent="USER_AGENT")


async def main():
    client.set_token("CODE")
    return await client.userRate.increment("USER_RATE_ID")


if __name__ == "__main__":
    asyncio.run(main())
```

5.**Refresh access token:** Access tokens have a limited lifespan of **1 day**, so your application will need to refresh them periodically to maintain access to the user's resources. To do this use a `get_access_token` function with the refresh token. Shikimori will respond with a new access token and refresh token that your application can use to continue accessing the user's resources.
```python
import asyncio

from shikimori.client import Shikimori

client = Shikimori(user_agent="USER_AGENT")


async def main():
    return await client.auth.refresh("REFRESH_TOKEN")


if __name__ == "__main__":
    asyncio.run(main())
```

## Contribution
Contributions to this library are always welcome and highly encouraged.

## License
This library is licensed under MIT. Please see [LICENSE](https://github.com/Snayt1k3/shiki.py/blob/master/LICENSE) for licensing details.