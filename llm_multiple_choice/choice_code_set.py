from .exceptions import DuplicateChoiceError
from .choice_code import ChoiceCode
from typing import Iterator

class ChoiceCodeSet:
    def __init__(self) -> None:
        self._codes: set[ChoiceCode] = set()

    @property
    def codes(self) -> frozenset[ChoiceCode]:
        return frozenset(self._codes)

    def add(self, code: ChoiceCode) -> None:
        if code in self._codes:
            raise DuplicateChoiceError(f"Choice code {code.code} is already in the set.")
        self._codes.add(code)

    def has(self, code: ChoiceCode) -> bool:
        return code in self._codes

    def __len__(self) -> int:
        return len(self._codes)

    def __iter__(self) -> Iterator[ChoiceCode]:
        return iter(self._codes)
