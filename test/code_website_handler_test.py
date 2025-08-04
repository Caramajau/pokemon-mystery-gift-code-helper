from typing import Final, Mapping
from unittest import TestCase, main
from unittest.mock import MagicMock, patch
from model.code_website_handler import CodeWebsiteHandler


class CodeWebsiteHandlerTest(TestCase):
    json_handler_read_method: Final[str] = "json_handler_caramajau.json_handler.JSONHandler.read_json"
    json_handler_write_method: Final[str] = "json_handler_caramajau.json_handler.JSONHandler.write_json"
    example_file_content: Final[Mapping[str, list[str]]] = {
        "test": ["http://example.com"]
    }

    def setUp(self) -> None:
        self.__default_websites: Mapping[str, list[str]] = (
            CodeWebsiteHandler.DEFAULT_WEBSITES
        )

    @patch(json_handler_read_method, return_value={})
    @patch(json_handler_write_method)
    def test_code_website_handler_given_empty_file_uses_and_writes_default_websites(
        self, mocked_write: MagicMock, mocked_read: MagicMock
    ) -> None:
        handler = CodeWebsiteHandler()

        self.assertEqual(handler.get_websites(), self.__default_websites)
        mocked_read.assert_called_once()
        mocked_write.assert_called_once_with(self.__default_websites)

    @patch(json_handler_read_method, return_value=example_file_content)
    @patch(json_handler_write_method)
    def test_code_website_handler_given_file_with_content_reads_file(
        self, mocked_write: MagicMock, mocked_read: MagicMock
    ) -> None:
        handler = CodeWebsiteHandler()

        self.assertEqual(
            handler.get_websites(), CodeWebsiteHandlerTest.example_file_content
        )
        mocked_read.assert_called_once()
        mocked_write.assert_not_called()


if __name__ == "__main__":
    main()
