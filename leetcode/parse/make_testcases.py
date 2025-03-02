import argparse
import io
import json


def create_tests(description: str):
    tid = None
    params = {}
    buf = io.StringIO()

    for line in description.splitlines():
        line = line.strip()
        if line.startswith("Example "):
            tid = line.removesuffix(":")
        elif line.startswith("Input: "):
            tokens = line.removeprefix("Input: ").split(", ")
            varsdict = dict(token.split(" = ") for token in tokens)
            varsdict = {name: json.loads(value) for name, value in varsdict.items()}
            params[tid] = varsdict
        elif line.startswith("Output: "):
            expected = json.loads(line.removeprefix("Output: "))
            params[tid]["expected"] = expected

    with open("params.json", "w") as stream:
        json.dump(params, stream, indent=4)

    # Grab the names of the parameters
    for varsdict in params.values():
        param_names = list(varsdict)
        break

    buf.write("import pytest\n\n\n")
    buf.write("@pytest.mark.parametrize(\n")
    buf.write(f"    {param_names},\n")
    buf.write("    [\n")
    for tid, varsdict in params.items():
        buf.write(
            f"        pytest.param({', '.join(repr(varsdict[name]) for name in param_names)}, ",
        )
        buf.write(f"id={tid!r}),\n")
    buf.write("    ]\n")
    buf.write(")\n")
    buf.write(f"def test_solution(fut, {', '.join(param_names)}):\n")
    buf.write("    pass\n")


def main():
    """Entry"""
    parser = argparse.ArgumentParser()
    parser.add_argument("input")
    args = parser.parse_args()
    with open(args.input) as stream:
        description = stream.read()
    print(create_tests(description))


if __name__ == "__main__":
    main()
