from dataclasses import dataclass


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
