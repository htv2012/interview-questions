import shlex


# @pysnooper.snoop("/tmp/snoop.txt")
def tokenize(s: str):
    tokens = []
    for token in shlex.shlex(s):
        if token[-1].isdigit():
            # Split abc,123 into abc, 123
            for i, c in enumerate(token):
                if c.isdigit():
                    word = token[:i]
                    if word:
                        tokens.append(word)
                    token = token[i:]
                    break
        tokens.append(token)
    return tokens


# @pysnooper.snoop("/tmp/snoop.txt")
def decode_string(tokens) -> str:
    stack = []
    for token in tokens:
        if token.isdigit():
            count = int(token)
            stack.append(count)
        elif token == "[":
            stack.append(token)
        elif token == "]":
            # Pops 1) the word, 2) left bracket, 3) count
            # Then process and push back into the stack
            word = stack.pop()
            assert stack.pop() == "["
            count = stack.pop()
            decoded = count * word
            if stack and stack[-1] != "[":
                stack[-1] += decoded
            else:
                stack.append(decoded)
        else:
            # Must be a word, concatenate or push
            if stack and stack[-1] != "[":
                stack[-1] += token
            else:
                stack.append(token)

    assert len(stack) == 1
    return stack[0]


class Solution:
    def decodeString(self, s: str) -> str:
        tokens = tokenize(s)
        result = decode_string(tokens)
        return result
