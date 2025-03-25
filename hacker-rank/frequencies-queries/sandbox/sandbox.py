import marimo

__generated_with = "0.11.25"
app = marimo.App(width="medium")


@app.cell
def _():
    import collections
    import dataclasses

    class Freq:
        def __init__(self):
            self.freq = {}
            self.el = {}

        def __repr__(self):
            return f"{self.__class__.__name__}(freq={self.freq}, el={self.el})"

        def append(self, value):
            current_freq = self.freq.get(value, 0)
            self.freq[value] = current_freq + 1

            self.el.get(current_freq, set()).discard(value)
            if current_freq in self.el and not self.el[current_freq]:
                del self.el[current_freq]
            self.el.setdefault(current_freq + 1, set()).append(value)

        def remove(self, value):
            current_freq = self.freq.get(value, 0)
            if current_freq == 0:
                return

            if current_freq == 1:
                del self.freq[value]
                self.el[1].discard(value)
                if not self.el[1]:
                    del self.el[1]
                return

            self.freq[value] -= 1
            self.el[current_freq].discard(value)
            if not self.el[current_freq]:
                del self.el[current_freq]
            self.el.setdefault(current_freq - 1, set()).append(value)

        def __contains__(self, frequency):
            """Return True if frequency is found here"""
            return frequency in self.el and self.el[frequency]

    return Freq, collections, dataclasses


@app.cell
def _(Freq):
    freq = Freq()
    freq
    return (freq,)


@app.cell
def _(freq):
    def try_append(f):
        for v in [25, 37, 49, 25, 25]:
            f.append(v)
            print(f"append {v} => {f}")

    try_append(freq)
    return (try_append,)


@app.cell
def _(freq):
    def try_query(f):
        for i in range(5):
            print(f"Query {i} => {i in f}")

    try_query(freq)
    return (try_query,)


@app.cell
def _(freq):
    def try_remove(f):
        for v in [-9, 25, 37]:
            f.remove(v)
            print(f"Remove {v} => {f}")

    try_remove(freq)
    return (try_remove,)


@app.cell
def _(freq):
    5 in freq
    return


@app.cell
def _(freq):
    freq.remove(49)
    freq
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
