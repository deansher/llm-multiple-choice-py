from .choice_code import ChoiceCode
from .choice_section import ChoiceSection
from .exceptions import InvalidChoiceCodeError
from .display_format import DisplayFormat
from typing import List

class ChoiceManager:
    def __init__(self) -> None:
        self.sections: List[ChoiceSection] = []
        self.next_choice_code = 1

    def add_section(self, introduction: str) -> ChoiceSection:
        section = ChoiceSection(introduction, self)
        self.sections.append(section)
        return section

    def get_next_choice_code(self) -> ChoiceCode:
        code = ChoiceCode(self.next_choice_code)
        self.next_choice_code += 1
        return code

    def is_valid_choice_code(self, code: ChoiceCode) -> bool:
        return 1 <= code.code < self.next_choice_code

    def validate_choice_code(self, code: ChoiceCode) -> None:
        if not self.is_valid_choice_code(code):
            raise InvalidChoiceCodeError(f"Choice code {code.code} is invalid.")

    def display(self, format: DisplayFormat) -> str:
        if format == DisplayFormat.MARKDOWN:
            return "\n\n".join(section.display(format) for section in self.sections)
        else:
            raise NotImplementedError(f"Display format '{format}' is not supported.")
