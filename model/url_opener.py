import webbrowser


class URLOpener:
    def __init__(self) -> None:
        self.__urls: list[str] = []

    def set_urls(self, new_urls: list[str]) -> None:
        self.__urls = new_urls

    def open_urls(self) -> None:
        for url in self.__urls:
            self.__open_url(url)

    @staticmethod
    def __open_url(url: str) -> None:
        webbrowser.open(url)
