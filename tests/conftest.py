import sys
import os

# Получите путь к корневому каталогу проекта
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Добавьте корневой путь проекта в PYTHONPATH
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
