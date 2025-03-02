import contextlib
import collections
import shlex


class LispLex(shlex.shlex):
    def get_token(self):
        token = super().get_token()
        
        # Attempt to convert the token to int
        with contextlib.suppress(ValueError):
            number = int(token)
            return token

        if token == "-":
            number = super().get_token()
            token = f"{token}{number}"
        return token


class Solution:
    def evaluate(self, expression: str) -> int:
        stack = collections.deque()
        for token in LispLex(expression):
            if token == "(":
                stack.append(token)
            elif isinstance(token, int):
                stack.append(token)
            elif token == 'add':
                

