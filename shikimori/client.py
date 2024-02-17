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
        self._limiter = RequestLimiter(MAX_REQUESTS_PER_SECOND, MAX_REQUESTS_PER_MINUTE, self._request,)

        # Auth dependencies
        self._options = AuthOptions(
            client_id=client_id, redirect_uri=redirect_uri, client_secret=client_secret
        )
        self._user_agent = user_agent
        self._token = None

        # init auth
        self.Auth = Auth(self._limiter, self._user_agent, self._options)

        # dependencies
        self.__deps = {
            "base_url": self._base_url,
            "request": self._limiter,
            "user_agent": self._user_agent,
        }

        # init endpoints adapters
        self.AbuseRequest = endpoints.AbuseRequestEndpoint(**self.__deps)
        self.Achievement = endpoints.AchievementsEndpoint(**self.__deps)
        self.Anime = endpoints.AnimeEndpoint(**self.__deps)
        self.Appear = endpoints.AppearsEndpoint(**self.__deps)
        self.Ban = endpoints.BanEndpoint(**self.__deps)
        self.Calendar = endpoints.CalendarEndpoint(**self.__deps)
        self.Character = endpoints.CharacterEndpoint(**self.__deps)
        self.Club = endpoints.ClubEndpoint(**self.__deps)
        self.Comment = endpoints.CommentEndpoint(**self.__deps)
        self.Constant = endpoints.ConstantsEndpoint(**self.__deps)
        self.Dialog = endpoints.DialogsEndpoint(**self.__deps)
        self.EpisodeNotification = endpoints.EpisodeNotificationEndpoint(**self.__deps)
        self.Favorite = endpoints.FavoritesEndpoint(**self.__deps)
        self.Forum = endpoints.ForumEndpoint(**self.__deps)
        self.Friend = endpoints.FriendEndpoint(**self.__deps)
        self.Genre = endpoints.GenreEndpoint(**self.__deps)
        self.Manga = endpoints.MangaEndpoint(**self.__deps)
        self.Message = endpoints.MessageEndpoint(**self.__deps)
        self.People = endpoints.PeopleEndpoint(**self.__deps)
        self.Publisher = endpoints.PublisherEndpoint(**self.__deps)
        self.Ranobe = endpoints.RanobeEndpoint(**self.__deps)
        self.Review = endpoints.ReviewEndpoint(**self.__deps)
        self.Stats = endpoints.StatsEndpoint(**self.__deps)
        self.Studio = endpoints.StudiosEndpoint(**self.__deps)
        self.Style = endpoints.StylesEndpoint(**self.__deps)
        self.TopicIgnore = endpoints.TopicIgnoreEndpoint(**self.__deps)
        self.Topic = endpoints.TopicsEndpoint(**self.__deps)
        self.UserIgnore = endpoints.UserIgnoreEndpoint(**self.__deps)
        self.UserRate = endpoints.UserRatesEndpoint(**self.__deps)
        self.User = endpoints.UserEndpoint(**self.__deps)
        self.Video = endpoints.VideosEndpoint(**self.__deps)

    def set_token(self, token: str) -> None:
        self._request.set_token(token)
