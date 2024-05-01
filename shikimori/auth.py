import logging
from dataclasses import dataclass

from shikimori.base import BaseLimiter
from shikimori.exceptions import RequestError

__all__ = ["Auth", "AuthOptions", "AccessTokenData"]

logger = logging.getLogger(__name__)


@dataclass
class AuthOptions:
    client_id: str
    redirect_uri: str
    client_secret: str
    scopes: list[str] | None = None


@dataclass
class AccessTokenData:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str
    created_at: int


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

        Args:
            request (BaseLimiter): An instance of the BaseLimiter class for making requests.
            user_agent (str, optional): User-agent string to be used in API requests. Defaults to None.
            options (AuthOptions, optional): An instance of the AuthOptions class containing authentication options. Defaults to None.
            base_url (str, optional): Base URL for the Shikimori API. Defaults to None.
        """
        self._base_url = base_url
        self._headers = {"User-Agent": user_agent}
        self._request = request
        self._options = options

    async def get_access_token(self, auth_code: str) -> AccessTokenData | RequestError:
        """
        Obtain an access token using an authorization code.

        Args:
            auth_code (str): Authorization code obtained during the OAuth authorization process.

        Returns:
            Union[AccessTokenData, RequestError]: An instance of AccessTokenData if successful, or a RequestError if an error occurs during the request.

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

        Args:
            refresh_token (str): Refresh token obtained during the OAuth authorization process.

        Returns:
            Union[AccessTokenData, RequestError]: An instance of AccessTokenData if successful, or a RequestError if an error occurs during the request.

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
    def auth_uri(self) -> str:
        return f"https://shikimori.one/oauth/authorize?client_id={self._options.client_id}&redirect_uri={self._options.redirect_uri}&response_type=code&scope={"+".join(self._options.scopes)}"  # NOQA