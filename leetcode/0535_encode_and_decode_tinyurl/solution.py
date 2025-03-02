import itertools
import string


class Codec:
    def __init__(self):
        self.long2short = {}
        self.short2long = {}

        args = [string.ascii_lowercase] * 3
        self.shorts = ("".join(letters) for letters in itertools.product(*args))

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        short_url = self.long2short.get(longUrl)
        if short_url is None:
            short_url = f"https://tinyurl.com/{next(self.shorts)}"
            self.short2long[short_url] = longUrl
            self.long2short[longUrl] = short_url
        return short_url

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        return self.short2long[shortUrl]
