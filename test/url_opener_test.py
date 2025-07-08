import webbrowser
from unittest.mock import patch
from unittest import main, TestCase
from model.url_opener import open_url, open_urls


class URLOpenerTest(TestCase):
    def setUp(self) -> None:
        self.__valid_url: str = "https://example.com"
        self.__valid_urls: list[str] = ["https://example.com", "https://test.com"]

    def test_open_url_given_valid_url_opens_the_url(self) -> None:
        with patch.object(webbrowser, webbrowser.open.__name__) as mocked_open:
            open_url(self.__valid_url)
            self.assertEqual(mocked_open.call_count, 1)
            mocked_open.assert_called_once_with(self.__valid_url)

    def test_open_urls_given_valid_urls_opens_each_url(self) -> None:
        with patch.object(webbrowser, webbrowser.open.__name__) as mock_open:
            open_urls(self.__valid_urls)
            self.assertEqual(mock_open.call_count, len(self.__valid_urls))

            for url in self.__valid_urls:
                mock_open.assert_any_call(url)


if __name__ == "__main__":
    main()
