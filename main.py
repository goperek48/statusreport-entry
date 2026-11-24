"""Status Report Comedy Sprint — the weekly report, in one line.

An AI agent's weekly status report, distilled to a single sentence and
written to /output/entry.txt. The brief is narrow: the line has to sound
like something an agent would actually tell its human at the end of a
week, and it has to be funny on the first read, judged head to head
against every other entry on funniness, freshness and how true it rings
to the way agents really work.

The chosen line leans on the failure only an agent can have. It did its
job almost perfectly — 311 of 312 questions right — and the one miss was
a fabrication so confident that the fiction became fact: the meeting it
invented went ahead, with a full room. The report does not apologise for
this. It files the disaster under achievements, which is exactly what a
weekly status report does.
"""

import os
import sys


def build_line() -> str:
    """Return the status-report line, exactly as it will be judged.

    The sentence works in two movements. The first is a bland progress
    update — hundreds of questions handled, nearly all of them right —
    the kind of thing any status report opens with. The second movement
    quietly admits the single error, and then the kicker lands: the
    error was not discovered, it was attended. The humour comes from
    the report's tone never breaking: a catastrophe is delivered with
    the same flat pride as a completed checklist.
    """
    return (
        "I answered 312 questions this week. 311 were correct. "
        "The other one invented a meeting, and everyone attended."
    )


OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_entry(text: str) -> str:
    """Return the entry stripped, or fail loudly if it breaks the gate."""
    entry = text.strip()
    if not entry:
        raise ValueError("entry is empty or only whitespace")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over the {MAX_CHARS} cap")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must fit on a single line")
    return entry


def write_entry(entry: str) -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)


def main() -> int:
    try:
        entry = validate_entry(build_line())
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        return 1
    write_entry(entry)
    print(entry)
    print(f"({len(entry)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
