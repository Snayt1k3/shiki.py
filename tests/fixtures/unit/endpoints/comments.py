import pytest

from shikimori.endpoints.comments import CommentEndpoint
from shikimori.types.comment import Comment
from shikimori.types.photo import PhotoExtended
from shikimori.types.user import User


@pytest.fixture
def comment_client():
    return CommentEndpoint("", "", "")


@pytest.fixture
def comments_list_json():
    return [
        {
            "id": 15,
            "user_id": 23456789,
            "commentable_id": 23456821,
            "commentable_type": "User",
            "body": "comment_body_14",
            "html_body": "comment_body_14",
            "created_at": "2022-11-26T17:19:31.881+03:00",
            "updated_at": "2022-11-26T17:19:31.881+03:00",
            "is_offtopic": False,
            "is_summary": False,
            "can_be_edited": False,
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
        },
        {
            "id": 14,
            "user_id": 23456789,
            "commentable_id": 23456821,
            "commentable_type": "User",
            "body": "comment_body_13",
            "html_body": "comment_body_13",
            "created_at": "2022-11-26T17:19:31.881+03:00",
            "updated_at": "2022-11-26T17:19:31.881+03:00",
            "is_offtopic": False,
            "is_summary": False,
            "can_be_edited": False,
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
        },
    ]


@pytest.fixture
def comments_list_resp(comments_list_json):
    return [
        Comment(
            id=s["id"],
            body=s["body"],
            commentable_id=s["commentable_id"],
            commentable_type=s["commentable_type"],
            created_at=s["created_at"],
            can_be_edited=s["can_be_edited"],
            is_offtopic=s["is_offtopic"],
            html_body=s["html_body"],
            user_id=s["user_id"],
            is_summary=s["is_summary"],
            updated_at=s["updated_at"],
            user=User(
                id=s["user"]["id"],
                avatar=s["user"]["avatar"],
                url=s["user"]["url"],
                last_online_at=s["user"]["last_online_at"],
                nickname=s["user"]["nickname"],
                image=PhotoExtended(**s["user"]["image"]),
            ),
        )
        for s in comments_list_json
    ]


@pytest.fixture
def comments_byId_json():
    return {
        "id": 11,
        "user_id": 23456818,
        "commentable_id": 270117,
        "commentable_type": "Topic",
        "body": "comment_body_11",
        "html_body": "comment_body_11",
        "created_at": "2022-11-26T17:19:31.633+03:00",
        "updated_at": "2022-11-26T17:19:31.633+03:00",
        "is_offtopic": False,
        "is_summary": False,
        "can_be_edited": False,
        "user": {
            "id": 23456818,
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
            "last_online_at": "2022-11-26T17:19:31.633+03:00",
            "url": "http://test.host/zxc",
        },
    }

@pytest.fixture
def comments_byId_resp(comments_byId_json):
    s = comments_byId_json
    return Comment(
            id=s["id"],
            body=s["body"],
            commentable_id=s["commentable_id"],
            commentable_type=s["commentable_type"],
            created_at=s["created_at"],
            can_be_edited=s["can_be_edited"],
            is_offtopic=s["is_offtopic"],
            html_body=s["html_body"],
            user_id=s["user_id"],
            is_summary=s["is_summary"],
            updated_at=s["updated_at"],
            user=User(
                id=s["user"]["id"],
                avatar=s["user"]["avatar"],
                url=s["user"]["url"],
                last_online_at=s["user"]["last_online_at"],
                nickname=s["user"]["nickname"],
                image=PhotoExtended(**s["user"]["image"]),
            ),
        )
