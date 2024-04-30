import pytest

from shikimori.endpoints.bans import BanEndpoint
from shikimori.types.bans import Comment, Ban
from shikimori.types.photo import PhotoExtended
from shikimori.types.user import User


@pytest.fixture
def ban_client():
    return BanEndpoint("", "", "")


@pytest.fixture
def bans_list_json():
    return [
        {
            "id": 2,
            "user_id": 23456789,
            "comment": {
                "id": 6,
                "commentable_id": 82468,
                "commentable_type": "Topic",
                "body": "comment_body_6\n\n[ban=2]",
                "user_id": 23456789,
                "created_at": "2022-11-26T17:19:27.200+03:00",
                "updated_at": "2022-11-26T17:19:27.200+03:00",
                "is_offtopic": False,
            },
            "moderator_id": 23456789,
            "reason": "moderator comment",
            "created_at": "2022-11-26T17:19:27.200+03:00",
            "duration_minutes": 180,
            "user": {
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
            "moderator": {
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
            "id": 1,
            "user_id": 23456789,
            "comment": {
                "id": 5,
                "commentable_id": 82468,
                "commentable_type": "Topic",
                "body": "comment_body_5\n\n[ban=1]",
                "user_id": 23456789,
                "created_at": "2022-11-26T17:19:27.200+03:00",
                "updated_at": "2022-11-26T17:19:27.200+03:00",
                "is_offtopic": False,
            },
            "moderator_id": 23456789,
            "reason": "moderator comment",
            "created_at": "2022-11-26T17:19:27.200+03:00",
            "duration_minutes": 180,
            "user": {
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
            "moderator": {
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
    ]


@pytest.fixture
def bans_list_resp(bans_list_json):
    return [
        Ban(
            id=b["id"],
            created_at=b["created_at"],
            duration_minutes=b["duration_minutes"],
            moderator_id=b["moderator_id"],
            reason=b["reason"],
            user_id=b["user_id"],
            comment=Comment(**b["comment"]),
            user=User(
                id=b["user"]["id"],
                avatar=b["user"]["avatar"],
                image=PhotoExtended(**b["user"]["image"]),
                last_online_at=b["user"]["last_online_at"],
                nickname=b["user"]["nickname"],
                url=b["user"]["url"],
            ),
            moderator=User(
                id=b["moderator"]["id"],
                avatar=b["moderator"]["avatar"],
                image=PhotoExtended(**b["moderator"]["image"]),
                last_online_at=b["moderator"]["last_online_at"],
                nickname=b["moderator"]["nickname"],
                url=b["moderator"]["url"],
            ),
        )
        for b in bans_list_json
    ]
