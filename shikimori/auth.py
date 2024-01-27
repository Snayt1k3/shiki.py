from dataclasses import dataclass

@dataclass
class AuthOptions:
    client_id: str
    redirect_uri: str
    client_secret: str


class Auth:
    def __init__(
        self, request, user_agent: str = None, options: AuthOptions | None = None
    ):
        self._headers = {"User-Agent": user_agent}
        self._request = request
        self._options = options

    async def get_access_token(self, auth_code: str) -> dict:
        body = {
            "grant_type": "authorization_code",
            "client_id": self._options.client_id,
            "client_secret": self._options.client_secret,
            "code": auth_code,
            "redirect_uri": self._options.redirect_uri,
        }
        return await self._request.make_request(
            "POST", url="/oauth/token", body=body, headers=self._headers
        )

    async def get_new_access_token(self, refresh_token: str) -> dict:
        body = {
            "grant_type": "refresh_token",
            "client_id": self._options.client_id,
            "client_secret": self._options.client_secret,
            "refresh_token": refresh_token,
        }
        return await self._request.make_request(
            "POST", url="/oauth/token", body=body, headers=self._headers
        )
