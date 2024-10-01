from dataclasses import dataclass

@dataclass(frozen=True)
class ChoiceCode:
    code: int

    def __str__(self) -> str:
        return str(self.code)
