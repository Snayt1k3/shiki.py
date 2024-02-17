import sys
import os

# Получите путь к корневому каталогу проекта
root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Добавьте корневой путь проекта в PYTHONPATH
sys.path.insert(0, root_path)

from tests.fixtures.unit.api_client import *
from tests.fixtures.unit.limiter import *
