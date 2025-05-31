from typing import Mapping
from model.code_website_handler import CodeWebsiteHandler
from model.url_opener import URLOpener


def main() -> None:
    url_opener: URLOpener = URLOpener()
    website_handler: CodeWebsiteHandler = CodeWebsiteHandler()
    websites: Mapping[str, list[str]] = website_handler.get_websites()

    process_game_selection(url_opener, websites)


def process_game_selection(
    url_opener: URLOpener, websites: Mapping[str, list[str]]
) -> None:
    print_available_games(websites)

    selected_game: str = input("Choose a game: ")

    if selected_game in websites.keys():
        url_opener.set_urls(websites[selected_game])
        url_opener.open_urls()
    else:
        process_game_selection(url_opener, websites)


def print_available_games(websites: Mapping[str, list[str]]) -> None:
    print("The following games have links:")
    for game in websites.keys():
        print(game)
    print()


if __name__ == "__main__":
    main()
