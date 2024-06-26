import sys
import os

root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.insert(0, root_path)

from tests.fixtures.unit.api_client import *
from tests.fixtures.unit.limiter import *
from tests.fixtures.unit.endpoints.abuse_request import *
from tests.fixtures.unit.endpoints.topic_ignore import *
from tests.fixtures.unit.endpoints.user_ignore import *
from tests.fixtures.unit.endpoints.episode_notification import *
from tests.fixtures.unit.endpoints.user_rates import *
from tests.fixtures.unit.endpoints.achievements import *
from tests.fixtures.unit.endpoints.animes import *
from tests.fixtures.unit.endpoints.appears import *
from tests.fixtures.unit.endpoints.bans import *
from tests.fixtures.unit.endpoints.calendar import *
from tests.fixtures.unit.endpoints.characters import *
from tests.fixtures.unit.endpoints.club import *
from tests.fixtures.unit.endpoints.comments import *
from tests.fixtures.unit.endpoints.constants import *
from tests.fixtures.unit.endpoints.dialogs import *
from tests.fixtures.unit.endpoints.favorites import *
from tests.fixtures.unit.endpoints.forums import *
from tests.fixtures.unit.endpoints.friends import *
from tests.fixtures.unit.endpoints.genres import *
from tests.fixtures.unit.endpoints.mangas import *
from tests.fixtures.unit.endpoints.messages import *
from tests.fixtures.unit.endpoints.people import *
from tests.fixtures.unit.endpoints.publisher import *
from tests.fixtures.unit.endpoints.ranobes import *
from tests.fixtures.unit.endpoints.reviews import *
from tests.fixtures.unit.endpoints.stats import *
from tests.fixtures.unit.endpoints.studios import *
from tests.fixtures.unit.endpoints.topic import *
from tests.fixtures.unit.endpoints.users import *
from tests.fixtures.unit.endpoints.videos import *
from tests.fixtures.unit.endpoints.graphql import *
from tests.fixtures.integration.client import *
