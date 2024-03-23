from .requestLimiter import RequestLimiter
from .constants import MAX_REQUESTS_PER_SECOND, SHIKIMORI_URL, MAX_REQUESTS_PER_MINUTE
from .request import Request
from .auth import Auth, AuthOptions
from shikimori import endpoints
from logging import basicConfig, DEBUG

__all__ = ["Shikimori"]


class Shikimori:
    """
    main class fow work with shikimori api
    """

    def __init__(
        self,
        *,
        user_agent: str = None,
        client_id: str = None,
        client_secret: str = None,
        redirect_uri: str = "urn:ietf:wg:oauth:2.0:oob",
        base_url: str = None,
        logging: int | bool = None,
    ):
        """
        Initialize client for work with shikimori api

        """
        if not user_agent:
            raise ValueError(
                "You need to specify user-agent otherwise you may be banned"
            )

        if logging is not None:
            if logging is True:
                basicConfig(level=DEBUG)
            else:
                basicConfig(level=logging)

        # dependencies
        self._base_url = SHIKIMORI_URL if not base_url else base_url
        self._request = Request()
        self._limiter = RequestLimiter(
            MAX_REQUESTS_PER_SECOND,
            MAX_REQUESTS_PER_MINUTE,
            self._request,
        )

        # Auth dependencies
        self._options = AuthOptions(
            client_id=client_id, redirect_uri=redirect_uri, client_secret=client_secret
        )
        self._user_agent = user_agent
        self._token = None

        # init auth
        self.Auth = Auth(self._limiter, self._user_agent, self._options)

        # dependencies
        self._deps = {
            "base_url": self._base_url,
            "request": self._limiter,
            "user_agent": self._user_agent,
        }

        # init endpoints adapters
        self.abuseRequest = endpoints.AbuseRequestEndpoint(**self._deps)
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

    def set_token(self, token: str) -> None:
        self._request.set_token(token)
