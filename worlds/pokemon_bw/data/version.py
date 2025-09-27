from typing import NamedTuple


class VersionCompatibility(NamedTuple):
    patch_file: tuple[int, int, int]
    rom: tuple[int, int, int]
    ut: tuple[int, int, int]


version: tuple[int, int, int] = (0, 3, 5)

compatibility: dict[tuple[int, int, int], VersionCompatibility] = {
    (0, 3, 0): VersionCompatibility((0, 3, 0), (0, 3, 0), (0, 3, 0)),
    (0, 3, 1): VersionCompatibility((0, 3, 0), (0, 3, 0), (0, 3, 0)),
    (0, 3, 2): VersionCompatibility((0, 3, 0), (0, 3, 2), (0, 3, 2)),
    (0, 3, 3): VersionCompatibility((0, 3, 0), (0, 3, 3), (0, 3, 2)),
    (0, 3, 4): VersionCompatibility((0, 3, 0), (0, 3, 4), (0, 3, 2)),
    (0, 3, 5): VersionCompatibility((0, 3, 0), (0, 3, 4), (0, 3, 2)),
}


def patch_file() -> tuple[int, int, int]:
    return compatibility[version].patch_file


def rom() -> tuple[int, int, int]:
    return compatibility[version].rom


def ut() -> tuple[int, int, int]:
    return compatibility[version].ut
