import os

import pytest
from shikimori.client import Shikimori
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def user_agent():
    return os.getenv("USER_AGENT")

@pytest.fixture
def client(user_agent):
    return Shikimori(user_agent=user_agent)


