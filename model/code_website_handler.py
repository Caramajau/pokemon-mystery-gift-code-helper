import os
from typing import Final, Mapping

from model.json_handler import JSONHandler


class CodeWebsiteHandler:
    # Only "recent" ones included and also just game8 as they seemed to have good lists.
    DEFAULT_WEBSITES: Final[Mapping[str, list[str]]] = {
        "sv": ["https://game8.co/games/Pokemon-Scarlet-Violet/archives/384443"],
        "la": ["https://game8.co/games/Pokemon-Legends-Arceus/archives/353314"],
        "bdsp": [
            "https://game8.co/games/Pokemon-Brilliant-Diamond-Shining-Pearl/archives/342366"
        ],
        "swsh": ["https://game8.co/games/pokemon-sword-shield/archives/280987"],
    }

    DATA_PATH: Final[str] = os.path.join("data", "websites.json")

    def __init__(self) -> None:
        json_handler: JSONHandler = JSONHandler(CodeWebsiteHandler.DATA_PATH)

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
