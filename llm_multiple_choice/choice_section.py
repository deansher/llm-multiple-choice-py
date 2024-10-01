from .choice_code import ChoiceCode
from .display_format import DisplayFormat
from typing import List

class Choice:
    def __init__(self, code: ChoiceCode, description: str):
        self.code = code
        self.description = description

class ChoiceSection:
    def __init__(self, introduction: str, manager: 'ChoiceManager'):
        self.introduction = introduction
        self.manager = manager
        self.choices: List[Choice] = []

    def add_choice(self, description: str) -> ChoiceCode:
        """
        Adds a choice to the section.

        Args:
            description (str): The description of the choice.

        Returns:
            ChoiceCode: The code assigned to the new choice.

        Raises:
            ValueError: If the description is empty.
        """
        if not description.strip():
            raise ValueError("Choice description cannot be empty.")
        code = self.manager.get_next_choice_code()
        choice = Choice(code, description)
        self.choices.append(choice)
        return code

    def display(self, format: DisplayFormat) -> str:
        """
        Displays the section in the specified format.

        Args:
            format (DisplayFormat): The format to display the section in.

        Returns:
            str: The formatted display of the section.

        Raises:
            NotImplementedError: If the specified format is not supported.
        """
        if format == DisplayFormat.MARKDOWN:
            markdown_output = f"### {self.introduction}\n\n"
            for choice in self.choices:
                markdown_output += f"- **{choice.code.code}**: {choice.description}\n"
            return markdown_output
        else:
            raise NotImplementedError(f"Display format '{format.value}' is not supported.")
