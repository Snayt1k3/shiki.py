from .requestLimiter import RequestLimiter
from .constants import MAX_REQUESTS_PER_SECOND, SHIKIMORI_URL, MAX_REQUESTS_PER_MINUTE
from .request import Request
from .auth import Auth, AuthOptions
from shikimori import endpoints
from logging import basicConfig, DEBUG

__all__ = ["Shikimori"]


class Shikimori:
    """
    Main class for interacting with the Shikimori API.

    This class provides methods and endpoints for working with various features of the Shikimori API,
    such as anime, manga, users, forums, etc.
    """

    def __init__(
            self,
            *,
            user_agent: str = None,
            client_id: str = None,
            client_secret: str = None,
            redirect_uri: str = "urn:ietf:wg:oauth:2.0:oob",
            scopes: list[str] = None,
            base_url: str = None,
            logging: int | bool = None,
    ):
        """
        Initialize client for working with the Shikimori API.

        Args:
            user_agent (str): User-agent string to be used in API requests.
            client_id (str): Client ID for OAuth authentication.
            client_secret (str): Client secret for OAuth authentication.
            scopes (list): Scopes for OAuth authentication.
            redirect_uri (str): Redirect URI for OAuth authentication. Defaults to "urn:ietf:wg:oauth:2.0:oob".
            base_url (str): Base URL for the Shikimori API. Defaults to None.
            logging (Union[int, bool]): Logging level for debug information. If True, debug logging is enabled. If False, logging is disabled. Defaults to None.
        Raises:
            ValueError: If user_agent is not specified.
        """
        if not user_agent:
            raise ValueError("You need to specify user-agent")

        if logging is not None:
            if logging is True:
                basicConfig(level=DEBUG)
            else:
                basicConfig(level=logging)

        # dependencies
        self._base_url = base_url or SHIKIMORI_URL
        self._request = Request()
        self._limiter = RequestLimiter(
            MAX_REQUESTS_PER_SECOND,
            MAX_REQUESTS_PER_MINUTE,
            self._request,
        )

        # Auth dependencies
        self._options = AuthOptions(
            client_id=client_id, redirect_uri=redirect_uri, client_secret=client_secret, scopes=scopes
        )
        self._user_agent = user_agent

        # dependencies
        self._deps = {
            "base_url": self._base_url,
            "request": self._limiter,
            "user_agent": self._user_agent,
        }

        self.abuseRequest = endpoints.AbuseRequestEndpoint(**self._deps)
        """Endpoint"""
        self.achievement = endpoints.AchievementsEndpoint(**self._deps)
        self.anime = endpoints.AnimeEndpoint(**self._deps)
        self.appear = endpoints.AppearsEndpoint(**self._deps)
        self.ban = endpoints.BanEndpoint(**self._deps)
        self.calendar = endpoints.CalendarEndpoint(**self._deps)
        self.character = endpoints.CharacterEndpoint(**self._deps)
        self.club = endpoints.ClubEndpoint(**self._deps)
        self.comment = endpoints.CommentEndpoint(**self._deps)
        self.constant = endpoints.ConstantsEndpoint(**self._deps)
        self.dialog = endpoints.DialogsEndpoint(**self._deps)
        self.episodeNotification = endpoints.EpisodeNotificationEndpoint(**self._deps)
        self.favorite = endpoints.FavoritesEndpoint(**self._deps)
        self.forum = endpoints.ForumEndpoint(**self._deps)
        self.friend = endpoints.FriendEndpoint(**self._deps)
        self.genre = endpoints.GenreEndpoint(**self._deps)
        self.manga = endpoints.MangaEndpoint(**self._deps)
        self.message = endpoints.MessageEndpoint(**self._deps)
        self.people = endpoints.PeopleEndpoint(**self._deps)
        self.publisher = endpoints.PublisherEndpoint(**self._deps)
        self.ranobe = endpoints.RanobeEndpoint(**self._deps)
        self.review = endpoints.ReviewEndpoint(**self._deps)
        self.stats = endpoints.StatsEndpoint(**self._deps)
        self.studio = endpoints.StudiosEndpoint(**self._deps)
        self.style = endpoints.StylesEndpoint(**self._deps)
        self.topicIgnore = endpoints.TopicIgnoreEndpoint(**self._deps)
        self.topic = endpoints.TopicsEndpoint(**self._deps)
        self.userIgnore = endpoints.UserIgnoreEndpoint(**self._deps)
        self.userRate = endpoints.UserRatesEndpoint(**self._deps)
        self.user = endpoints.UserEndpoint(**self._deps)
        self.video = endpoints.VideosEndpoint(**self._deps)
        self.auth = Auth(self._limiter, self._user_agent, self._options, self._base_url)

    def set_token(self, token: str) -> None:
        """
        Set OAuth token for authentication.

        :param token: OAuth token to be set.
        """
        self._request.set_token(token)
