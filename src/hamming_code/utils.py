from typing import Generator

PARITY_CHECK_OFFSET = 1
PARITY_PLACE_BASE = 2
PARITY_INITIAL = 0


def encode(data: list[int]) -> list[int]:
    encoded = data.copy()

    for parity_place in iter_parity_places(encoded):
        encoded = encoded[:parity_place] + [PARITY_INITIAL] + encoded[parity_place:]

    for parity_index, parity_place in enumerate(iter_parity_places(encoded)):
        parity = get_parity(encoded, parity_index)
        encoded[parity_place] = parity

    return encoded


def decode(data: list[int]) -> list[int]:
    decoded = data.copy()
    for deleted, place in enumerate(iter_parity_places(data)):
        del decoded[place - deleted]
    return decoded


def fix(data: list[int]) -> list[int]:
    if not detect(data):
        return data

    fixed = data.copy()
    error_place = sum(place + PARITY_CHECK_OFFSET for place in get_incorrect_parity_places(data)) - PARITY_CHECK_OFFSET
    fixed[error_place] ^= 1
    return fixed


def detect(data: list[int]) -> bool:
    return any(True for _ in get_incorrect_parity_places(data))


def get_incorrect_parity_places(data: list[int]) -> Generator[int, None, None]:
    for parity_index, parity_place in enumerate(iter_parity_places(data)):
        parity = data[parity_place]
        expected_parity = get_parity(data, parity_index) ^ parity
        if parity != expected_parity:
            yield parity_place


def get_parity(data: list[int], parity_index: int) -> int:
    parity = PARITY_INITIAL
    mask = 1 << parity_index
    for place, bit in enumerate(data):
        in_parity_check = (place + PARITY_CHECK_OFFSET) & mask
        if in_parity_check and bit:
            parity ^= 1
    return parity


def iter_parity_places(data: list[int]) -> Generator[int, None, None]:
    parity_place = PARITY_CHECK_OFFSET
    while parity_place <= len(data):
        yield parity_place - PARITY_CHECK_OFFSET
        parity_place *= PARITY_PLACE_BASE
