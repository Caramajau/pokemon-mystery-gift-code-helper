from collections.abc import Mapping
from os import path
from typing import Final

from json_handler_caramajau.json_handler import JSONHandler


class CodeWebsiteHandler:
    # Only "recent" ones included and mostly game8 as they seemed to have good lists.
    DEFAULT_WEBSITES: Final[Mapping[str, list[str]]] = {
        # Mainline games
        "sv": ["https://game8.co/games/Pokemon-Scarlet-Violet/archives/384443"],
        "la": ["https://game8.co/games/Pokemon-Legends-Arceus/archives/353314"],
        "bdsp": [
            "https://game8.co/games/Pokemon-Brilliant-Diamond-Shining-Pearl/archives/342366"
        ],
        "swsh": ["https://game8.co/games/pokemon-sword-shield/archives/280987"],
        # Spin-off games
        "unite": ["https://game8.co/games/Pokemon-UNITE/archives/355379"],
        "go": ["https://www.pockettactics.com/pokemon-go/codes"],
        "ptcgp": [
            "https://www.ign.com/wikis/pokemon-tcg-pocket/Pokemon_TCG_Pocket_Gift_Codes"
        ],
    }

    DATA_PATH: Final[str] = path.join("data", "websites.json")

    def __init__(self) -> None:
        json_handler: JSONHandler[list[str]] = JSONHandler(CodeWebsiteHandler.DATA_PATH)

        websites: Mapping[str, list[str]] = json_handler.read_json()
        if len(websites) < 1:
            self.__websites: Mapping[str, list[str]] = (
                CodeWebsiteHandler.DEFAULT_WEBSITES
            )
            json_handler.write_json(self.__websites)
        else:
            self.__websites = websites

    def get_websites(self) -> Mapping[str, list[str]]:
        return self.__websites
