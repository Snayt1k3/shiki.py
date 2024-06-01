import logging
from shikimori.types.auth import AuthOptions, AccessTokenData

from shikimori.base import BaseLimiter
from shikimori.exceptions import RequestError

__all__ = ["Auth"]

logger = logging.getLogger(__name__)


class Auth:
    """
    Class for handling authentication with the Shikimori API.

    This class provides methods for obtaining access tokens and refreshing tokens.
    """

    def __init__(
        self,
        request: BaseLimiter,
        user_agent: str = None,
        options: AuthOptions | None = None,
        base_url: str = None,
    ):
        """
        Initialize the Auth class.

        :param request: An instance of the BaseLimiter class for making requests.
        :param user_agent:  User-agent string to be used in API requests. Defaults to None.
        :param options:  An instance of the AuthOptions class containing authentication options. Defaults to None.
        :param base_url:  Base URL for the Shikimori API. Defaults to None.
        """
        self._base_url = base_url
        self._headers = {"User-Agent": user_agent}
        self._request = request
        self._options = options

    async def get_access_token(self, auth_code: str) -> AccessTokenData | RequestError:
        """
        Obtain an access token using an authorization code.

        :param auth_code: Authorization code obtained during the OAuth authorization process.
        """
        body = {
            "grant_type": "authorization_code",
            "client_id": self._options.client_id,
            "client_secret": self._options.client_secret,
            "code": auth_code,
            "redirect_uri": self._options.redirect_uri,
        }

        resp = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/oauth/token",
            json=body,
            headers=self._headers,
        )

        if not isinstance(resp, RequestError):
            return AccessTokenData(**resp)

        logger.debug(
            f"Bad Request(refresh): status - {resp.status_code}: info - {str(resp)}"
        )

        return resp

    async def refresh(self, refresh_token: str) -> AccessTokenData | RequestError:
        """
        Refresh an access token using a refresh token.

        :param refresh_token: Refresh token obtained during the OAuth authorization process.
        """
        body = {
            "grant_type": "refresh_token",
            "client_id": self._options.client_id,
            "client_secret": self._options.client_secret,
            "refresh_token": refresh_token,
        }
        resp = await self._request.make_request(
            "POST",
            url=f"{self._base_url}/oauth/token",
            json=body,
            headers=self._headers,
        )

        if not isinstance(resp, RequestError):
            return AccessTokenData(**resp)

        logger.debug(
            f"Bad Request(refresh): status - {resp.status_code}: info - {str(resp)}"
        )

        return resp

    @property
    def auth_url(self) -> str:
        """
        Generates a URL for obtaining an authorization code to authenticate requests.
        """
        return f"https://shikimori.one/oauth/authorize?client_id={self._options.client_id}&redirect_uri={self._options.redirect_uri}&response_type=code&scope={'+'.join(self._options.scopes) if self._options.scopes else ''}"  # NOQA
