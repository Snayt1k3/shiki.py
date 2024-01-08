from .requestLimiter import RequestLimiter
from .constants import MAX_REQUESTS_PER_SECOND, SHIKIMORI_URL
from .request import Request
from .auth import Auth, AuthOptions
from .endpoints.topic_ignore import TopicIgnoreEndpoint
from .endpoints.user_rates import UserRatesEndpoint
from .endpoints.abuse_requests import AbuseRequestEndpoint
from .endpoints.user_ignore import UserIgnoreEndpoint
from .endpoints.episode_notifications import EpisodeNotificationEndpoint


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
        base_url: str = None,
    ):
        """Initialize client for work with shikimori api"""
        if not user_agent:
            raise ValueError(
                "You need to specify user-agent otherwise you may be banned"
            )
        # dependencies
        self._base_url = SHIKIMORI_URL if not base_url else base_url
        self._limiter = RequestLimiter(
            MAX_REQUESTS_PER_SECOND, 1, Request()
        )  # Auth dependencies
        self._options = AuthOptions(
            client_id=client_id, redirect_uri=redirect_uri, client_secret=client_secret
        )
        self._user_agent = user_agent

        # init auth
        self.Auth = Auth(self._limiter, self._user_agent, self._options)

        # init endpoints adapters
        self.Topic = TopicIgnoreEndpoint(
            self._base_url, self._limiter, self._user_agent
        )
        self.UserRate = UserRatesEndpoint(
            self._base_url, self._limiter, self._user_agent
        )
        self.UserIgnore = UserIgnoreEndpoint(
            self._base_url, self._limiter, self._user_agent
        )
        self.AbuseRequest = AbuseRequestEndpoint(
            self._base_url, self._limiter, self._user_agent
        )
        self.EpisodeNotify = EpisodeNotificationEndpoint(
            self._base_url, self._limiter, self._user_agent
        )
