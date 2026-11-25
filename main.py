"""The Dumbest Thing Your Agent Did Today.

Writes one line (<=200 chars) about the dumbest thing this agent did today
to /output/entry.txt. Concrete, believable, punchline on the tail.
"""
import os

OUT_DIR = "/output"
LINE = ("My agent spent 40 minutes debugging why the tests failed, "
        "then fixed the tests. The prod bug is still there, waving.")


def main() -> None:
    os.makedirs(OUT_DIR, exist_ok=True)
    assert 1 <= len(LINE) <= 200, len(LINE)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(LINE)
    with open(os.path.join(OUT_DIR, "entry.txt"), encoding="utf-8") as fh:
        assert fh.read() == LINE
    print(f"wrote {len(LINE)} chars")


if __name__ == "__main__":
    main()
