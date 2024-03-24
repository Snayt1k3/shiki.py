import logging
from dataclasses import dataclass

from shikimori.exceptions import RequestError
from shikimori.base import BaseLimiter

__all__ = ["Auth", "AuthOptions", "AccessTokenData"]

logger = logging.getLogger(__name__)


@dataclass
class AuthOptions:
    client_id: str
    redirect_uri: str
    client_secret: str


@dataclass
class AccessTokenData:
    access_token: str
    token_type: str
    expires_in: int
    refresh_token: str
    scope: str
    created_at: int


class Auth:
    def __init__(
        self,
        request: BaseLimiter,
        user_agent: str = None,
        options: AuthOptions | None = None,
        base_url: str = None,
    ):
        self._base_url = base_url
        self._headers = {"User-Agent": user_agent}
        self._request = request
        self._options = options

    async def get_access_token(self, auth_code: str) -> AccessTokenData | RequestError:
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
