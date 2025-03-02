from solution import Codec

c = Codec()

long = "https://google.com"
short = c.encode(long)
print(f"{long=}")
print(f"{short=}")
