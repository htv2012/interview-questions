class BrowserHistory:
    def __init__(self, homepage: str):
        self.history = []
        self.here = -1  # Current page
        self.visit(homepage)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}("
            f"here={self.here!r}"
            f", "
            f"history={self.history!r}"
            f")"
        )

    def visit(self, url: str) -> None:
        del self.history[self.here + 1 :]
        self.history.append(url)
        self.here = len(self.history) - 1

    def back(self, steps: int) -> str:
        self.here = max(self.here - steps, 0)
        return self.history[self.here]

    def forward(self, steps: int) -> str:
        self.here = min(self.here + steps, len(self.history) - 1)
        return self.history[self.here]
