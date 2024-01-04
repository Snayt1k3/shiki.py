from pydantic import BaseModel


class AuthOptions(BaseModel):
    client_id: str
    redirect_uri: str
    client_secret: str


class Auth:
    def __init__(
        self, request, user_agent: str = None, options: AuthOptions | None = None
    ):
        self.headers = {"User-Agent": user_agent}
        self.request = request
        self.options = options

    async def get_access_token(self, auth_code: str) -> dict:
        body = {
            "grant_type": "authorization_code",
            "client_id": self.options.client_id,
            "client_secret": self.options.client_secret,
            "code": auth_code,
            "redirect_uri": self.options.redirect_uri,
        }
        return await self.request.make_request(
            "POST", url="/oauth/token", body=body, headers=self.headers
        )

    async def get_new_access_token(self, refresh_token: str) -> dict:
        body = {
            "grant_type": "refresh_token",
            "client_id": self.options.client_id,
            "client_secret": self.options.client_secret,
            "refresh_token": refresh_token,
        }
        return await self.request.make_request(
            "POST", url="/oauth/token", body=body, headers=self.headers
        )
