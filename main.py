from model.url_opener import URLOpener

def main() -> None:
    url_opener: URLOpener = URLOpener()
    test_url: str = "https://vecka.nu/"
    url_opener.set_urls([test_url])
    url_opener.open_urls()

if __name__ == "__main__":
    main()
