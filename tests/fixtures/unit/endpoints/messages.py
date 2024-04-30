import pytest

from shikimori.endpoints.message import MessageEndpoint
from shikimori.types.message import MessageInfo
from shikimori.types.photo import Photo, PhotoExtended
from shikimori.types.topics import Linked
from shikimori.types.user import User


@pytest.fixture
def message_client():
    return MessageEndpoint("", "", "")


@pytest.fixture
def messages_byid_json():
    return {
        "id": 16,
        "kind": "Private",
        "read": False,
        "body": "test",
        "html_body": "test",
        "created_at": "2022-11-26T17:19:32.889+03:00",
        "linked_id": 0,
        "linked_type": None,
        "linked": None,
        "from": {
            "id": 23456828,
            "nickname": "zxc",
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
            "last_online_at": "2022-11-26T17:19:32.889+03:00",
            "url": "http://test.host/zxc",
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
    }


@pytest.fixture
def messages_byid_resp(messages_byid_json):
    response = messages_byid_json
    return MessageInfo(
        id=response["id"],
        body=response["body"],
        created_at=response["created_at"],
        html_body=response["html_body"],
        kind=response["kind"],
        linked=(
            Linked(
                name=response["linked"]["name"],
                id=response["linked"]["id"],
                russian=response["linked"]["russian"],
                url=response["linked"]["url"],
                kind=response["linked"]["kind"],
                score=response["linked"]["score"],
                status=response["linked"]["status"],
                episodes=response["linked"].get("episodes"),
                episodes_aired=response["linked"].get("episodes_aired"),
                volumes=response["linked"].get("volumes"),
                chapters=response["linked"].get("chapters"),
                aired_on=response["linked"]["aired_on"],
                released_on=response["linked"]["released_on"],
                image=Photo(**response["linked"]["image"]),
            )
            if response["linked"]
            else None
        ),
        linked_id=response["linked_id"],
        linked_type=response["linked_type"],
        read=response["read"],
        to=User(
            id=response["to"]["id"],
            nickname=response["to"]["nickname"],
            avatar=response["to"]["avatar"],
            last_online_at=response["to"]["last_online_at"],
            url=response["to"]["url"],
            image=PhotoExtended(**response["to"]["image"]),
        ),
        sender=User(
            id=response["from"]["id"],
            nickname=response["from"]["nickname"],
            avatar=response["from"]["avatar"],
            last_online_at=response["from"]["last_online_at"],
            url=response["from"]["url"],
            image=PhotoExtended(**response["from"]["image"]),
        ),
    )


@pytest.fixture
def messages_create_json():
    return {
        "id": 9,
        "kind": "Private",
        "read": False,
        "body": "xx",
        "html_body": "xx",
        "created_at": "2022-11-26T17:19:32.718+03:00",
        "linked_id": 0,
        "linked_type": None,
        "linked": None,
        "from": {
            "id": 23456824,
            "nickname": "zxc",
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
            "last_online_at": "2022-11-26T17:19:32.718+03:00",
            "url": "http://test.host/zxc",
        },
        "to": {
            "id": 23456824,
            "nickname": "zxc",
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
            "last_online_at": "2022-11-26T17:19:32.718+03:00",
            "url": "http://test.host/zxc",
        },
    }


@pytest.fixture
def messages_create_resp(messages_create_json):
    response = messages_create_json
    return MessageInfo(
        id=response["id"],
        body=response["body"],
        created_at=response["created_at"],
        html_body=response["html_body"],
        kind=response["kind"],
        linked=(
            Linked(
                name=response["linked"]["name"],
                id=response["linked"]["id"],
                russian=response["linked"]["russian"],
                url=response["linked"]["url"],
                kind=response["linked"]["kind"],
                score=response["linked"]["score"],
                status=response["linked"]["status"],
                episodes=response["linked"].get("episodes"),
                episodes_aired=response["linked"].get("episodes_aired"),
                volumes=response["linked"].get("volumes"),
                chapters=response["linked"].get("chapters"),
                aired_on=response["linked"]["aired_on"],
                released_on=response["linked"]["released_on"],
                image=Photo(**response["linked"]["image"]),
            )
            if response["linked"]
            else None
        ),
        linked_id=response["linked_id"],
        linked_type=response["linked_type"],
        read=response["read"],
        to=User(
            id=response["to"]["id"],
            nickname=response["to"]["nickname"],
            avatar=response["to"]["avatar"],
            last_online_at=response["to"]["last_online_at"],
            url=response["to"]["url"],
            image=PhotoExtended(**response["to"]["image"]),
        ),
        sender=User(
            id=response["from"]["id"],
            nickname=response["from"]["nickname"],
            avatar=response["from"]["avatar"],
            last_online_at=response["from"]["last_online_at"],
            url=response["from"]["url"],
            image=PhotoExtended(**response["from"]["image"]),
        ),
    )


@pytest.fixture
def messages_update_json():
    return {
        "id": 5,
        "kind": "Private",
        "read": False,
        "body": "blablabla",
        "html_body": "blablabla",
        "created_at": "2022-11-26T17:19:32.615+03:00",
        "linked_id": 0,
        "linked_type": None,
        "linked": None,
        "from": {
            "id": 23456822,
            "nickname": "zxc",
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
            "last_online_at": "2022-11-26T17:19:32.615+03:00",
            "url": "http://test.host/zxc",
        },
        "to": {
            "id": 23456822,
            "nickname": "zxc",
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
            "last_online_at": "2022-11-26T17:19:32.615+03:00",
            "url": "http://test.host/zxc",
        },
    }


@pytest.fixture
def messages_update_resp(messages_update_json):
    response = messages_update_json
    return MessageInfo(
        id=response["id"],
        body=response["body"],
        created_at=response["created_at"],
        html_body=response["html_body"],
        kind=response["kind"],
        linked=(
            Linked(
                name=response["linked"]["name"],
                id=response["linked"]["id"],
                russian=response["linked"]["russian"],
                url=response["linked"]["url"],
                kind=response["linked"]["kind"],
                score=response["linked"]["score"],
                status=response["linked"]["status"],
                episodes=response["linked"].get("episodes"),
                episodes_aired=response["linked"].get("episodes_aired"),
                volumes=response["linked"].get("volumes"),
                chapters=response["linked"].get("chapters"),
                aired_on=response["linked"]["aired_on"],
                released_on=response["linked"]["released_on"],
                image=Photo(**response["linked"]["image"]),
            )
            if response["linked"]
            else None
        ),
        linked_id=response["linked_id"],
        linked_type=response["linked_type"],
        read=response["read"],
        to=User(
            id=response["to"]["id"],
            nickname=response["to"]["nickname"],
            avatar=response["to"]["avatar"],
            last_online_at=response["to"]["last_online_at"],
            url=response["to"]["url"],
            image=PhotoExtended(**response["to"]["image"]),
        ),
        sender=User(
            id=response["from"]["id"],
            nickname=response["from"]["nickname"],
            avatar=response["from"]["avatar"],
            last_online_at=response["from"]["last_online_at"],
            url=response["from"]["url"],
            image=PhotoExtended(**response["from"]["image"]),
        ),
    )
