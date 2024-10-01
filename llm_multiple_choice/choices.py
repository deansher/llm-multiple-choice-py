from typing import List

from .choice_code import ChoiceCode
from .display_format import DisplayFormat
from .exceptions import InvalidChoiceCodeError


class Choice:
    def __init__(self, code: ChoiceCode, description: str) -> None:
        self.code = code
        self.description = description


class ChoiceSection:
    def __init__(self, introduction: str, manager: "ChoiceManager") -> None:
        self.introduction = introduction
        self.manager = manager
        self.choices: List[Choice] = []

    def add_choice(self, description: str) -> ChoiceCode:
        if not description.strip():
            raise ValueError("Choice description cannot be empty.")
        code = self.manager.get_next_choice_code()
        choice = Choice(code, description)
        self.choices.append(choice)
        return code

    def display(self, format: DisplayFormat) -> str:
        if format == DisplayFormat.MARKDOWN:
            markdown_output = f"### {self.introduction}\n\n"
            for choice in self.choices:
                markdown_output += f"- **{choice.code.code}**: {choice.description}\n"
            return markdown_output
        else:
            raise NotImplementedError(
                f"Display format '{format.value}' is not supported."
            )


class ChoiceManager:
    def __init__(self) -> None:
        self.sections: List[ChoiceSection] = []
        self.next_choice_code: int = 1

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
            raise NotImplementedError(
                f"Display format '{format.value}' is not supported."
            )
