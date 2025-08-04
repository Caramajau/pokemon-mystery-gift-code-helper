import webbrowser
from unittest import TestCase, main
from unittest.mock import patch

from model.url_opener import open_url, open_urls


class URLOpenerTest(TestCase):
    def setUp(self) -> None:
        self.__invalid_url: str = "Not a url"
        self.__valid_url: str = "https://example.com"

        self.__invalid_urls: list[str] = ["Not a url", "Definitely a url, maybe?"]
        self.__valid_urls: list[str] = ["https://example.com", "https://test.com"]

    def test_open_url_given_valid_url_opens_the_url(self) -> None:
        with patch.object(webbrowser, webbrowser.open.__name__) as mocked_open:
            open_url(self.__valid_url)
            self.assertEqual(mocked_open.call_count, 1)
            mocked_open.assert_called_once_with(self.__valid_url)

    # The open function from webbrowser still opens the browser and kind of succeeds.
    # I could use regex to check if it is a URL and raise an exception, but
    # I don't think it is worth it.
    def test_open_url_given_invalid_url_still_attempts_to_open_the_url(self) -> None:
        with patch.object(webbrowser, webbrowser.open.__name__) as mocked_open:
            open_url(self.__invalid_url)
            self.assertEqual(mocked_open.call_count, 1)
            mocked_open.assert_called_once_with(self.__invalid_url)

    def test_open_urls_given_valid_urls_opens_each_url(self) -> None:
        with patch.object(webbrowser, webbrowser.open.__name__) as mocked_open:
            open_urls(self.__valid_urls)
            self.assertEqual(mocked_open.call_count, len(self.__valid_urls))

            for url in self.__valid_urls:
                mocked_open.assert_any_call(url)

    # The same situation for opening urls as opening just one.
    def test_open_urls_given_invalid_urls_still_attempts_to_open_the_urls(self) -> None:
        with patch.object(webbrowser, webbrowser.open.__name__) as mocked_open:
            open_urls(self.__invalid_urls)
            self.assertEqual(mocked_open.call_count, len(self.__invalid_urls))

            for url in self.__invalid_urls:
                mocked_open.assert_any_call(url)


if __name__ == "__main__":
    main()
