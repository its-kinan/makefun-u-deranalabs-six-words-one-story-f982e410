#!/usr/bin/env python3
"""Six Words, One Story entry: write one complete story in exactly six
words to /output/entry.txt.

The story: "The ring fit. The marriage didn't."

Six words, two sentences, a whole marriage arc. The first sentence is
the promise kept in shape; the second reverses it. The ring fit — the
symbol worked, the wedding happened. The marriage didn't — and the why
is left for the reader to fill in. Every word earns its place: drop
any one and the contrast collapses. The turn lands on "didn't": the
reader expects a happy ending from the first sentence and gets the
whole divorce instead, in a single word.
"""

import os

TEXT = "The ring fit. The marriage didn't."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
