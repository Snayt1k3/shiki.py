import pytest

from shikimori.endpoints.dialogs import DialogsEndpoint
from shikimori.types.photo import PhotoExtended, Photo
from shikimori.types.dialog import Dialog
from shikimori.types.message import Message, MessageInfo
from shikimori.types.user import User
from shikimori.types.topics import Linked


@pytest.fixture
def dialog_client():
    return DialogsEndpoint("", "", "")


@pytest.fixture
def dialogs_list_json():
    return [
        {
            "target_user": {
                "id": 23456830,
                "nickname": "user_12",
                "avatar": "/assets/globals/missing_avatar/x48.png",
                "image": {
                    "x160": "/assets/globals/missing_avatar/x160.png",
                    "x148": "/assets/globals/missing_avatar/x148.png",
                    "x80": "/assets/globals/missing_avatar/x80.png",
                    "x64": "/assets/globals/missing_avatar/x64.png",
                    "x48": "/assets/globals/missing_avatar/x48.png",
                    "x32": "/assets/globals/missing_avatar/x32.png",
                    "x16": "/assets/globals/missing_avatar/x16.png",
                },
                "last_online_at": "2022-11-26T17:19:33.176+03:00",
                "url": "http://test.host/user_12",
            },
            "message": {
                "id": 20,
                "kind": "Private",
                "read": False,
                "body": "test",
                "html_body": "test",
                "created_at": "2022-11-26T17:19:33.176+03:00",
                "linked_id": 0,
                "linked_type": None,
                "linked": None,
            },
        }
    ]


@pytest.fixture
def dialogs_list_resp(dialogs_list_json):
    return [
        Dialog(
            target_user=User(
                id=s["target_user"]["id"],
                nickname=s["target_user"]["nickname"],
                avatar=s["target_user"]["avatar"],
                last_online_at=s["target_user"]["last_online_at"],
                url=s["target_user"]["url"],
                image=PhotoExtended(**s["target_user"]["image"]),
            ),
            message=Message(
                id=s["message"]["id"],
                body=s["message"]["body"],
                html_body=s["message"]["html_body"],
                created_at=s["message"]["created_at"],
                read=s["message"]["read"],
                kind=s["message"]["kind"],
                linked_id=s["message"]["linked_id"],
                linked_type=s["message"]["linked_type"],
                linked=(
                    Linked(
                        name=s["message"]["linked"]["name"],
                        id=s["message"]["linked"]["id"],
                        russian=s["message"]["linked"]["russian"],
                        url=s["message"]["linked"]["url"],
                        kind=s["message"]["linked"]["kind"],
                        score=s["message"]["linked"]["score"],
                        status=s["message"]["linked"]["status"],
                        episodes=s["message"]["linked"]["episodes"],
                        episodes_aired=s["message"]["linked"]["episodes_aired"],
                        aired_on=s["message"]["linked"]["aired_on"],
                        released_on=s["message"]["linked"]["released_on"],
                        image=Photo(**s["message"]["linked"]["image"]),
                    )
                    if s["message"]["linked"]
                    else None
                ),
            ),
        )
        for s in dialogs_list_json
    ]


@pytest.fixture
def dialogs_ById_json():
    return [
        {
            "id": 19,
            "kind": "Private",
            "read": None,
            "body": "test",
            "html_body": "test",
            "created_at": "2022-11-26T17:19:33.124+03:00",
            "linked_id": 0,
            "linked_type": None,
            "linked": None,
            "from": {
                "id": 23456829,
                "nickname": "user_11",
                "avatar": "/assets/globals/missing_avatar/x48.png",
                "image": {
                    "x160": "/assets/globals/missing_avatar/x160.png",
                    "x148": "/assets/globals/missing_avatar/x148.png",
                    "x80": "/assets/globals/missing_avatar/x80.png",
                    "x64": "/assets/globals/missing_avatar/x64.png",
                    "x48": "/assets/globals/missing_avatar/x48.png",
                    "x32": "/assets/globals/missing_avatar/x32.png",
                    "x16": "/assets/globals/missing_avatar/x16.png",
                },
                "last_online_at": "2022-11-26T17:19:33.124+03:00",
                "url": "http://test.host/user_11",
            },
            "to": {
                "id": 23456789,
                "nickname": "user_user",
                "avatar": "/assets/globals/missing_avatar/x48.png",
                "image": {
                    "x160": "/assets/globals/missing_avatar/x160.png",
                    "x148": "/assets/globals/missing_avatar/x148.png",
                    "x80": "/assets/globals/missing_avatar/x80.png",
                    "x64": "/assets/globals/missing_avatar/x64.png",
                    "x48": "/assets/globals/missing_avatar/x48.png",
                    "x32": "/assets/globals/missing_avatar/x32.png",
                    "x16": "/assets/globals/missing_avatar/x16.png",
                },
                "last_online_at": "2022-11-26T17:19:26.755+03:00",
                "url": "http://test.host/user_user",
            },
        },
        {
            "id": 18,
            "kind": "Private",
            "read": False,
            "body": "test",
            "html_body": "test",
            "created_at": "2022-11-26T17:19:33.124+03:00",
            "linked_id": 0,
            "linked_type": None,
            "linked": None,
            "from": {
                "id": 23456789,
                "nickname": "user_user",
                "avatar": "/assets/globals/missing_avatar/x48.png",
                "image": {
                    "x160": "/assets/globals/missing_avatar/x160.png",
                    "x148": "/assets/globals/missing_avatar/x148.png",
                    "x80": "/assets/globals/missing_avatar/x80.png",
                    "x64": "/assets/globals/missing_avatar/x64.png",
                    "x48": "/assets/globals/missing_avatar/x48.png",
                    "x32": "/assets/globals/missing_avatar/x32.png",
                    "x16": "/assets/globals/missing_avatar/x16.png",
                },
                "last_online_at": "2022-11-26T17:19:26.755+03:00",
                "url": "http://test.host/user_user",
            },
            "to": {
                "id": 23456829,
                "nickname": "user_11",
                "avatar": "/assets/globals/missing_avatar/x48.png",
                "image": {
                    "x160": "/assets/globals/missing_avatar/x160.png",
                    "x148": "/assets/globals/missing_avatar/x148.png",
                    "x80": "/assets/globals/missing_avatar/x80.png",
                    "x64": "/assets/globals/missing_avatar/x64.png",
                    "x48": "/assets/globals/missing_avatar/x48.png",
                    "x32": "/assets/globals/missing_avatar/x32.png",
                    "x16": "/assets/globals/missing_avatar/x16.png",
                },
                "last_online_at": "2022-11-26T17:19:33.124+03:00",
                "url": "http://test.host/user_11",
            },
        },
    ]


@pytest.fixture
def dialogs_ById_resp(dialogs_ById_json):
    return [
        MessageInfo(
            id=s["id"],
            kind=s["kind"],
            body=s["body"],
            html_body=s["html_body"],
            created_at=s["created_at"],
            linked_id=s["linked_id"],
            linked_type=s["linked_type"],
            read=s["read"],
            linked=(
                Linked(
                    name=s["linked"]["name"],
                    id=s["linked"]["id"],
                    russian=s["linked"]["russian"],
                    url=s["linked"]["url"],
                    kind=s["linked"]["kind"],
                    score=s["linked"]["score"],
                    status=s["linked"]["status"],
                    episodes=s["linked"]["episodes"],
                    episodes_aired=s["linked"]["episodes_aired"],
                    aired_on=s["linked"]["aired_on"],
                    released_on=s["linked"]["released_on"],
                    image=Photo(**s["linked"]["image"]),
                )
                if s["linked"]
                else None
            ),
            to=User(
                id=s["to"]["id"],
                avatar=s["to"]["avatar"],
                image=PhotoExtended(**s["to"]["image"]),
                last_online_at=s["to"]["last_online_at"],
                nickname=s["to"]["nickname"],
                url=s["to"]["url"],
            ),
            sender=User(
                id=s["from"]["id"],
                avatar=s["from"]["avatar"],
                image=PhotoExtended(**s["from"]["image"]),
                last_online_at=s["from"]["last_online_at"],
                nickname=s["from"]["nickname"],
                url=s["from"]["url"],
            ),
        )
        for s in dialogs_ById_json
    ]
