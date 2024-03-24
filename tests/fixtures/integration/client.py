import logging
import os

import pytest
from shikimori.client import Shikimori
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture
def user_agent():
    return os.getenv("USER_AGENT")


@pytest.fixture
def auth_code():
    return os.getenv("AUTH_CODE")


@pytest.fixture
def client_id():
    return os.getenv("CLIENT_ID")


@pytest.fixture
def client_secret():
    return os.getenv("CLIENT_SECRET")


@pytest.fixture
def client(user_agent, client_secret, client_id):
    return Shikimori(
        user_agent=user_agent,
        logging=logging.DEBUG,
        client_id=client_id,
        client_secret=client_secret,
    )
