"""The Worst App Idea Ever Pitched.

One terrible app pitch, printed to stdout.
Deterministic, standard library only, writes no files.
"""

LINE = (
    "Uber, but for borrowing your neighbour's Wi-Fi password — "
    "surge pricing kicks in every time they change it."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
