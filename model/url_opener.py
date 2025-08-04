import webbrowser
from collections.abc import Iterable


def open_urls(urls: Iterable[str]) -> None:
    for url in urls:
        open_url(url)


def open_url(url: str) -> None:
    webbrowser.open(url)
