from .requestLimiter import RequestLimiter
from .constants import MAX_REQUESTS_PER_SECOND, SHIKIMORI_URL
from .request import Request
from .auth import Auth, AuthOptions
from .endpoints.topic_ignore import TopicIgnoreEndpoint

class Shikimori:
    """
    main class fow work with shikimori api
    """

    def __init__(
        self,
        user_agent: str = None,
        client_id: str = None,
        client_secret: str = None,
        redirect_uri: str = "urn:ietf:wg:oauth:2.0:oob",
    ):
        """Initialize client for work with shikimori api"""
        if not user_agent:
            raise ValueError(
                "You need to specify user-agent otherwise you may be banned"
            )
        self._limiter = RequestLimiter(MAX_REQUESTS_PER_SECOND, 1, Request())

        # Auth dependencies
        self._options = AuthOptions(
            client_id=client_id, redirect_uri=redirect_uri, client_secret=client_secret
        )
        self.Auth = Auth(limiter, user_agent, options)
        self.Topic = TopicIgnoreEndpoint(SHIKIMORI_URL, self._limiter, user_agent)
