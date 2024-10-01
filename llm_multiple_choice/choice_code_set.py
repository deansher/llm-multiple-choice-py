class ChoiceCodeSet:
    def __init__(self) -> None:
        self._codes: set[ChoiceCode] = set()

    @property
    def codes(self) -> set[ChoiceCode]:
        return self._codes

    def add(self, code: ChoiceCode) -> None:
        self._codes.add(code)

    def has(self, code: ChoiceCode) -> bool:
        return code in self._codes

    def __len__(self) -> int:
        return len(self._codes)

    def __iter__(self) -> Any:
        return iter(self._codes)
