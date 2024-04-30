import pytest

from shikimori.endpoints.characters import CharacterEndpoint
from shikimori.types.character import Character, AnimeRole, MangaRole
from shikimori.types.photo import Photo
from shikimori.types.roles import Character as MiniCharacter


@pytest.fixture
def character_client():
    return CharacterEndpoint("", "", "")


@pytest.fixture
def character_list_json():
    return {
        "id": 12,
        "name": "Alphonse Elric",
        "russian": "Альфонс Элрик",
        "image": {
            "original": "/system/characters/original/12.jpg?1701474667",
            "preview": "/system/characters/preview/12.jpg?1701474667",
            "x96": "/system/characters/x96/12.jpg?1701474667",
            "x48": "/system/characters/x48/12.jpg?1701474667",
        },
        "url": "/characters/12-alphonse-elric",
        "altname": "Al, Armored Alchemist",
        "japanese": "アルフォンス・エルリック",
        "description": "Младший брат [character=11]Эдварда Элрика[/character].\r\nВ детстве был очень похож на брата, но немного выше ростом, с более тёмными волосами и янтарными глазами. Из-за неудачной попытки человеческого преобразования Альфонс потерял своё тело, и его душа оказалась прикреплена к доспеху. Для большинства Альфонс предстаёт закованным в броню гигантом, из-за чего его постоянно принимают за старшего, что приводит [character=11]Эдварда[/character] в бешенство. Сам доспех представляет собой средневековые латы, с шипами на наплечниках и устрашающего вида шлемом. На левом наплечнике нарисован знак Фламеля. Кровавая печать, прикрепляющая душу к доспеху, нарисована на внутренней стороне в районе шеи.\r\nАльфонс спокойный и рассудительный, полная противоположность сумасбродному [character=11]Эдварду[/character]. В отличие от брата, Альфонс реже теряет контроль над собой и зачастую выступает своеобразным стоп-краном для удержания [character=11]Эдварда[/character]. Участвует во всех его авантюрах, при этом постоянно сокрушаясь, какой же у него испорченный брат. Готов пожертвовать своим благополучием и даже жизнью ради брата и близких людей. Чувствителен и весьма наивен, хотя дважды поймать его на одном и том же приёме непросто. Мечтает вернуть своё тело и даже составил список блюд, которые он после этого съест. Обожает кошек и животных вообще.\r\nКак и его брат, Альфонс — необычайно талантливый алхимик. По мастерству он мало уступает брату, а в алхимическом ремонте, вероятно, даже превосходит его. Также неплохо владеет холодным оружием. Альфонс — эксперт рукопашного боя, причём даже в детстве он превосходил [character=11]Эдварда[/character], а после превращения в доспех его навыки рукопашного боя только увеличились. Из-за отсутствия тела под доспехами Альфонс, вероятно, намного сильнее обычных людей, и его сила ограничена лишь прочностью доспехов.\r\n[spoiler=спойлер]Поначалу ему требуется круг для преобразования, но когда [character=5103]Кинг Бредли[/character] убивает забравшуюся в него химеру-союзника, открывается его способность к преобразованию без алхимического круга.\r\nВ отличие от [anime=121]аниме 2003 года[/anime], в [manga=25]манге[/manga] его характер с течением времени сильно изменился. После бегства из Бриггса и скитаний по Аместрису Альфонс становится более жёстким и решительным. Исчезает наивность. В результате понимания масштабов угрозы, возврат его тела отходит на задний план, и для победы он становится готов использовать любые методы. В частности он, в отличие от брата, готов использовать философский камень, но лишь чтобы защитить друзей от опасности. При этом он всё ещё верит в лучшее и готов протянуть руку помощи даже бывшему врагу.[/spoiler]",
        "description_html": '\u003cdiv class="b-text_with_paragraphs"\u003eМладший брат \u003ca href="https://shikimori.one/characters/11-edward-elric" title="Edward Elric" class="bubbled b-link" data-tooltip_url="https://shikimori.one/characters/11-edward-elric/tooltip" data-attrs="{\u0026quot;id\u0026quot;:11,\u0026quot;type\u0026quot;:\u0026quot;character\u0026quot;,\u0026quot;name\u0026quot;:\u0026quot;Edward Elric\u0026quot;,\u0026quot;russian\u0026quot;:\u0026quot;Эдвард Элрик\u0026quot;}"\u003eЭдварда Элрика\u003c/a\u003e.\u003cbr\u003eВ детстве был очень похож на брата, но немного выше ростом, с более тёмными волосами и янтарными глазами. Из-за неудачной попытки человеческого преобразования Альфонс потерял своё тело, и его душа оказалась прикреплена к доспеху. Для большинства Альфонс предстаёт закованным в броню гигантом, из-за чего его постоянно принимают за старшего, что приводит \u003ca href="https://shikimori.one/characters/11-edward-elric" title="Edward Elric" class="bubbled b-link" data-tooltip_url="https://shikimori.one/characters/11-edward-elric/tooltip" data-attrs="{\u0026quot;id\u0026quot;:11,\u0026quot;type\u0026quot;:\u0026quot;character\u0026quot;,\u0026quot;name\u0026quot;:\u0026quot;Edward Elric\u0026quot;,\u0026quot;russian\u0026quot;:\u0026quot;Эдвард Элрик\u0026quot;}"\u003eЭдварда\u003c/a\u003e в бешенство. Сам доспех представляет собой средневековые латы, с шипами на наплечниках и устрашающего вида шлемом. На левом наплечнике нарисован знак Фламеля. Кровавая печать, прикрепляющая душу к доспеху, нарисована на внутренней стороне в районе шеи.\u003cbr\u003eАльфонс спокойный и рассудительный, полная противоположность сумасбродному \u003ca href="https://shikimori.one/characters/11-edward-elric" title="Edward Elric" class="bubbled b-link" data-tooltip_url="https://shikimori.one/characters/11-edward-elric/tooltip" data-attrs="{\u0026quot;id\u0026quot;:11,\u0026quot;type\u0026quot;:\u0026quot;character\u0026quot;,\u0026quot;name\u0026quot;:\u0026quot;Edward Elric\u0026quot;,\u0026quot;russian\u0026quot;:\u0026quot;Эдвард Элрик\u0026quot;}"\u003eЭдварду\u003c/a\u003e. В отличие от брата, Альфонс реже теряет контроль над собой и зачастую выступает своеобразным стоп-краном для удержания \u003ca href="https://shikimori.one/characters/11-edward-elric" title="Edward Elric" class="bubbled b-link" data-tooltip_url="https://shikimori.one/characters/11-edward-elric/tooltip" data-attrs="{\u0026quot;id\u0026quot;:11,\u0026quot;type\u0026quot;:\u0026quot;character\u0026quot;,\u0026quot;name\u0026quot;:\u0026quot;Edward Elric\u0026quot;,\u0026quot;russian\u0026quot;:\u0026quot;Эдвард Элрик\u0026quot;}"\u003eЭдварда\u003c/a\u003e. Участвует во всех его авантюрах, при этом постоянно сокрушаясь, какой же у него испорченный брат. Готов пожертвовать своим благополучием и даже жизнью ради брата и близких людей. Чувствителен и весьма наивен, хотя дважды поймать его на одном и том же приёме непросто. Мечтает вернуть своё тело и даже составил список блюд, которые он после этого съест. Обожает кошек и животных вообще.\u003cbr\u003eКак и его брат, Альфонс — необычайно талантливый алхимик. По мастерству он мало уступает брату, а в алхимическом ремонте, вероятно, даже превосходит его. Также неплохо владеет холодным оружием. Альфонс — эксперт рукопашного боя, причём даже в детстве он превосходил \u003ca href="https://shikimori.one/characters/11-edward-elric" title="Edward Elric" class="bubbled b-link" data-tooltip_url="https://shikimori.one/characters/11-edward-elric/tooltip" data-attrs="{\u0026quot;id\u0026quot;:11,\u0026quot;type\u0026quot;:\u0026quot;character\u0026quot;,\u0026quot;name\u0026quot;:\u0026quot;Edward Elric\u0026quot;,\u0026quot;russian\u0026quot;:\u0026quot;Эдвард Элрик\u0026quot;}"\u003eЭдварда\u003c/a\u003e, а после превращения в доспех его навыки рукопашного боя только увеличились. Из-за отсутствия тела под доспехами Альфонс, вероятно, намного сильнее обычных людей, и его сила ограничена лишь прочностью доспехов.\u003cbr\u003e\u003cdiv class="b-spoiler_block to-process" data-dynamic="spoiler_block"\u003e\u003cspan tabindex="0"\u003eспойлер\u003c/span\u003e\u003cdiv\u003eПоначалу ему требуется круг для преобразования, но когда \u003ca href="https://shikimori.one/characters/5103-king-bradley" title="King Bradley" class="bubbled b-link" data-tooltip_url="https://shikimori.one/characters/5103-king-bradley/tooltip" data-attrs="{\u0026quot;id\u0026quot;:5103,\u0026quot;type\u0026quot;:\u0026quot;character\u0026quot;,\u0026quot;name\u0026quot;:\u0026quot;King Bradley\u0026quot;,\u0026quot;russian\u0026quot;:\u0026quot;Кинг Бредли\u0026quot;}"\u003eКинг Бредли\u003c/a\u003e убивает забравшуюся в него химеру-союзника, открывается его способность к преобразованию без алхимического круга.\u003cbr\u003eВ отличие от \u003ca href="https://shikimori.one/animes/z121-fullmetal-alchemist" title="Fullmetal Alchemist" class="bubbled b-link" data-tooltip_url="https://shikimori.one/animes/z121-fullmetal-alchemist/tooltip" data-attrs="{\u0026quot;id\u0026quot;:121,\u0026quot;type\u0026quot;:\u0026quot;anime\u0026quot;,\u0026quot;name\u0026quot;:\u0026quot;Fullmetal Alchemist\u0026quot;,\u0026quot;russian\u0026quot;:\u0026quot;Стальной алхимик\u0026quot;}"\u003eаниме 2003 года\u003c/a\u003e, в \u003ca href="https://shikimori.one/mangas/z25-fullmetal-alchemist" title="Fullmetal Alchemist" class="bubbled b-link" data-tooltip_url="https://shikimori.one/mangas/z25-fullmetal-alchemist/tooltip" data-attrs="{\u0026quot;id\u0026quot;:25,\u0026quot;type\u0026quot;:\u0026quot;manga\u0026quot;,\u0026quot;name\u0026quot;:\u0026quot;Fullmetal Alchemist\u0026quot;,\u0026quot;russian\u0026quot;:\u0026quot;Стальной алхимик\u0026quot;}"\u003eманге\u003c/a\u003e его характер с течением времени сильно изменился. После бегства из Бриггса и скитаний по Аместрису Альфонс становится более жёстким и решительным. Исчезает наивность. В результате понимания масштабов угрозы, возврат его тела отходит на задний план, и для победы он становится готов использовать любые методы. В частности он, в отличие от брата, готов использовать философский камень, но лишь чтобы защитить друзей от опасности. При этом он всё ещё верит в лучшее и готов протянуть руку помощи даже бывшему врагу.\u003c/div\u003e\u003c/div\u003e\u003c/div\u003e',
        "description_source": "http://ru.wikipedia.org/w/index.php?title=Альфонс_Элрик",
        "favoured": False,
        "thread_id": 31111,
        "topic_id": 31111,
        "updated_at": "2024-02-24T13:08:12.086+03:00",
        "seyu": [
            {
                "id": 8,
                "name": "Rie Kugimiya",
                "russian": "Риэ Кугимия",
                "image": {
                    "original": "/system/people/original/8.jpg?1701462672",
                    "preview": "/system/people/preview/8.jpg?1701462672",
                    "x96": "/system/people/x96/8.jpg?1701462672",
                    "x48": "/system/people/x48/8.jpg?1701462672",
                },
                "url": "/people/8-rie-kugimiya",
            },
            {
                "id": 44296,
                "name": "Andi Krösing",
                "russian": "Анди Крёзинг",
                "image": {
                    "original": "/system/people/original/44296.jpg?1697143712",
                    "preview": "/system/people/preview/44296.jpg?1697143712",
                    "x96": "/system/people/x96/44296.jpg?1697143712",
                    "x48": "/system/people/x48/44296.jpg?1697143712",
                },
                "url": "/people/44296-andi-kr-sing",
            },
        ],
        "animes": [
            {
                "id": 121,
                "name": "Fullmetal Alchemist",
                "russian": "Стальной алхимик",
                "image": {
                    "original": "/system/animes/original/121.jpg?1701409305",
                    "preview": "/system/animes/preview/121.jpg?1701409305",
                    "x96": "/system/animes/x96/121.jpg?1701409305",
                    "x48": "/system/animes/x48/121.jpg?1701409305",
                },
                "url": "/animes/z121-fullmetal-alchemist",
                "kind": "tv",
                "score": "8.11",
                "status": "released",
                "episodes": 51,
                "episodes_aired": 0,
                "aired_on": "2003-10-04",
                "released_on": "2004-10-02",
                "roles": ["Main"],
                "role": "Main",
            },
            {
                "id": 430,
                "name": "Fullmetal Alchemist: The Conqueror of Shamballa",
                "russian": "Стальной алхимик: Завоеватель Шамбалы",
                "image": {
                    "original": "/system/animes/original/430.jpg?1701409309",
                    "preview": "/system/animes/preview/430.jpg?1701409309",
                    "x96": "/system/animes/x96/430.jpg?1701409309",
                    "x48": "/system/animes/x48/430.jpg?1701409309",
                },
                "url": "/animes/z430-fullmetal-alchemist-the-conqueror-of-shamballa",
                "kind": "movie",
                "score": "7.51",
                "status": "released",
                "episodes": 1,
                "episodes_aired": 0,
                "aired_on": "2005-07-23",
                "released_on": None,
                "roles": ["Main"],
                "role": "Main",
            },
        ],
        "mangas": [
            {
                "id": 25,
                "name": "Fullmetal Alchemist",
                "russian": "Стальной алхимик",
                "image": {
                    "original": "/system/mangas/original/25.jpg?1702202128",
                    "preview": "/system/mangas/preview/25.jpg?1702202128",
                    "x96": "/system/mangas/x96/25.jpg?1702202128",
                    "x48": "/system/mangas/x48/25.jpg?1702202128",
                },
                "url": "/mangas/z25-fullmetal-alchemist",
                "kind": "manga",
                "score": "9.03",
                "status": "released",
                "volumes": 27,
                "chapters": 116,
                "aired_on": "2001-07-12",
                "released_on": "2010-09-11",
                "roles": ["Main"],
                "role": "Main",
            },
        ],
    }


@pytest.fixture
def character_list_resp(character_list_json):
    response = character_list_json
    return Character(
        id=response["id"],
        altname=response["altname"],
        description=response["description"],
        description_html=response["description_html"],
        description_source=response["description_source"],
        favoured=response["favoured"],
        japanese=response["japanese"],
        name=response["name"],
        russian=response["russian"],
        thread_id=response["thread_id"],
        topic_id=response["topic_id"],
        updated_at=response["updated_at"],
        url=response["url"],
        image=Photo(**response["image"]),
        seyu=[
            MiniCharacter(
                image=Photo(**s["image"]),
                id=s["id"],
                name=s["name"],
                russian=s["russian"],
                url=s["url"],
            )
            for s in response["seyu"]
        ],
        animes=[
            AnimeRole(
                id=an["id"],
                name=an["name"],
                russian=an["russian"],
                image=Photo(**an["image"]),
                url=an["url"],
                kind=an["kind"],
                score=an["score"],
                status=an["status"],
                episodes=an["episodes"],
                episodes_aired=an["episodes_aired"],
                aired_on=an["aired_on"],
                released_on=an["released_on"],
                role=an["role"],
                roles=an["roles"],
            )
            for an in response["animes"]
        ],
        mangas=[
            MangaRole(
                id=mn["id"],
                name=mn["name"],
                russian=mn["russian"],
                image=Photo(**mn["image"]),
                url=mn["url"],
                kind=mn["kind"],
                score=mn["score"],
                status=mn["status"],
                chapters=mn["chapters"],
                volumes=mn["volumes"],
                aired_on=mn["aired_on"],
                released_on=mn["released_on"],
                role=mn["role"],
                roles=mn["roles"],
            )
            for mn in response["mangas"]
        ],
    )


@pytest.fixture
def character_search_json():
    return [
        {
            "id": 8,
            "name": "asdf",
            "russian": "персонаж_8",
            "image": {
                "original": "/assets/globals/missing_original.jpg",
                "preview": "/assets/globals/missing_preview.jpg",
                "x96": "/assets/globals/missing_x96.jpg",
                "x48": "/assets/globals/missing_x48.jpg",
            },
            "url": "/characters/8-asdf",
        }
    ]


@pytest.fixture
def character_search_resp(character_search_json):
    return [
        MiniCharacter(
            image=Photo(**s["image"]),
            id=s["id"],
            name=s["name"],
            russian=s["russian"],
            url=s["url"],
        )
        for s in character_search_json
    ]
