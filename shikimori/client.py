from .requestLimiter import RequestLimiter
from .constants import MAX_REQUESTS_PER_SECOND, SHIKIMORI_URL, MAX_REQUESTS_PER_MINUTE
from .request import Request
from shikimori.auth import Auth
from shikimori.types.auth import AuthOptions
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

        :param user_agent: User-agent string to be used in API requests.
        :param client_id: Client ID for OAuth authentication.
        :param client_secret: Client secret for OAuth authentication.
        :param scopes: Scopes for OAuth authentication.
        :param redirect_uri: Redirect URI for OAuth authentication. Defaults to "urn:ietf:wg:oauth:2.0:oob".
        :param base_url: Base URL for the Shikimori API. Defaults to None.
        :param logging: Logging level for debug information. If True, debug logging is enabled. If False, logging is disabled. Defaults to None.

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
            client_id=client_id,
            redirect_uri=redirect_uri,
            client_secret=client_secret,
            scopes=scopes,
        )
        self._user_agent = user_agent

        # dependencies
        self._deps = {
            "base_url": self._base_url,
            "request": self._limiter,
            "user_agent": self._user_agent,
        }

        self.abuseRequest = endpoints.AbuseRequestEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/v2/abuse_requests/'"""
        self.achievement = endpoints.AchievementsEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/achievements'"""
        self.anime = endpoints.AnimeEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/animes'"""
        self.appear = endpoints.AppearsEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/appears'"""
        self.ban = endpoints.BanEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/bans'"""
        self.calendar = endpoints.CalendarEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/calendar'"""
        self.character = endpoints.CharacterEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/characters/'"""
        self.club = endpoints.ClubEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/clubs'"""
        self.comment = endpoints.CommentEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/comments'"""
        self.constant = endpoints.ConstantsEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/constants/anime'"""
        self.dialog = endpoints.DialogsEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/dialogs'"""
        self.episodeNotification = endpoints.EpisodeNotificationEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/v2/episode_notifications'"""
        self.favorite = endpoints.FavoritesEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/favorites/'"""
        self.forum = endpoints.ForumEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/forums'"""
        self.friend = endpoints.FriendEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/friends/:id'"""
        self.genre = endpoints.GenreEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/genres'"""
        self.manga = endpoints.MangaEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/mangas'"""
        self.message = endpoints.MessageEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/messages/'"""
        self.people = endpoints.PeopleEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/people/:id'"""
        self.publisher = endpoints.PublisherEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/publishers'"""
        self.ranobe = endpoints.RanobeEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/ranobe'"""
        self.review = endpoints.ReviewEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/reviews'"""
        self.stats = endpoints.StatsEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/stats/active_users'"""
        self.studio = endpoints.StudiosEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/studios'"""
        self.style = endpoints.StylesEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/styles/'"""
        self.topicIgnore = endpoints.TopicIgnoreEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/v2/topics/'"""
        self.topic = endpoints.TopicsEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/topics'"""
        self.userIgnore = endpoints.UserIgnoreEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/v2/users/:user_id/ignore'"""
        self.userImage = endpoints.UserImageEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/user_images'"""
        self.userRate = endpoints.UserRatesEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/v2/user_rates/'"""
        self.user = endpoints.UserEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/users'"""
        self.video = endpoints.VideosEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/animes/:anime_id/videos'"""
        self.auth = Auth(self._limiter, self._user_agent, self._options, self._base_url)
        """Endpoint for OAUTH"""
        self.graphql = endpoints.GraphQlEndpoint(**self._deps)
        """Endpoint for making requests to the URL 'https://shikimori.one/api/grapql with your fields'"""

    def set_token(self, token: str) -> None:
        """
        Set OAuth token for authentication.

        :param token: OAuth token to be set.
        """
        self._request.set_token(token)
