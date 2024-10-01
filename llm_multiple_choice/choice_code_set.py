from .exceptions import DuplicateChoiceError
from .choice_code import ChoiceCode
from typing import Iterator

class ChoiceCodeSet:
    """A set of unique ChoiceCode objects."""

    def __init__(self) -> None:
        self._codes: set[ChoiceCode] = set()

    @property
    def codes(self) -> frozenset[ChoiceCode]:
        """
        Returns a frozenset of the ChoiceCodes in the set.

        Returns:
            frozenset[ChoiceCode]: An immutable set of the ChoiceCodes.
        """
        return frozenset(self._codes)

    def add(self, code: ChoiceCode) -> None:
        """
        Adds a ChoiceCode to the set.

        Args:
            code (ChoiceCode): The ChoiceCode to add.

        Raises:
            DuplicateChoiceError: If the ChoiceCode is already in the set.
        """
        if code in self._codes:
            raise DuplicateChoiceError(f"Choice code {code.code} is already in the set.")
        self._codes.add(code)

    def has(self, code: ChoiceCode) -> bool:
        """
        Checks if a ChoiceCode is in the set.

        Args:
            code (ChoiceCode): The ChoiceCode to check.

        Returns:
            bool: True if the ChoiceCode is in the set, False otherwise.
        """
        return code in self._codes

    def __len__(self) -> int:
        """
        Returns the number of ChoiceCodes in the set.

        Returns:
            int: The number of ChoiceCodes in the set.
        """
        return len(self._codes)

    def __iter__(self) -> Iterator[ChoiceCode]:
        """
        Returns an iterator over the ChoiceCodes in the set.

        Returns:
            Iterator[ChoiceCode]: An iterator over the ChoiceCodes.
        """
        return iter(self._codes)
