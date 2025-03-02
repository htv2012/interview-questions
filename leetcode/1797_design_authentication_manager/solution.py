import logging


class AuthenticationManager:
    """
    There is an authentication system that works with authentication
    tokens. For each session, the user will receive a new authentication
    token that will expire timeToLive seconds after the currentTime. If
    the token is renewed, the expiry time will be extended to expire
    timeToLive seconds after the (potentially different) currentTime.

    Note that if a token expires at time t, and another action happens
    on time t (renew or countUnexpiredTokens), the expiration takes
    place before the other actions.
    """

    def __init__(self, timeToLive: int):
        """
        Constructs the AuthenticationManager and sets the timeToLive.
        """
        self.ttl = timeToLive
        self.id2time = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        """
        Generates a new token with the given tokenId at the given
        currentTime in seconds.
        """
        self.id2time[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        """
        Renews the unexpired token with the given tokenId at the given
        currentTime in seconds. If there are no unexpired tokens with
        the given tokenId, the request is ignored, and nothing happens.
        """
        if tokenId not in self.id2time:
            logging.debug("Token %r not found, not renewed", tokenId)
            return
        if currentTime - self.id2time[tokenId] >= self.ttl:
            logging.debug("Token %r expired, not renewed", tokenId)
            return
        self.id2time[tokenId] = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        """
        Returns the number of unexpired tokens at the given currentTime.
        """
        return sum(
            1 for stamp in self.id2time.values() if (currentTime - stamp) < self.ttl
        )
