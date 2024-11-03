from .choice_code import ChoiceCode
from .choice_section import ChoiceSection
from .exceptions import InvalidChoiceCodeError, InvalidChoicesResponseError
from .display_format import DisplayFormat
from .choice_code_set import ChoiceCodeSet
from typing import List


class ChoiceManager:
    """Manages sections and choices for the multiple-choice questionnaire."""

    def __init__(self) -> None:
        self.sections: List[ChoiceSection] = []
        self.next_choice_code = 1

    def add_section(self, introduction: str) -> ChoiceSection:
        """
        Adds a new section to the questionnaire.

        Args:
            introduction (str): The introduction text for the section.

        Returns:
            ChoiceSection: The newly created section.
        """
        section = ChoiceSection(introduction, self)
        self.sections.append(section)
        return section

    def get_next_choice_code(self) -> ChoiceCode:
        """
        Generates the next available choice code.

        Returns:
            ChoiceCode: The next available choice code.
        """
        code = ChoiceCode(self.next_choice_code)
        self.next_choice_code += 1
        return code

    def is_valid_choice_code(self, code: ChoiceCode) -> bool:
        """
        Checks if a given choice code is valid.

        Args:
            code (ChoiceCode): The choice code to validate.

        Returns:
            bool: True if the code is valid, False otherwise.
        """
        return 1 <= code.code < self.next_choice_code

    def validate_choice_code(self, code: ChoiceCode) -> None:
        """
        Validates a choice code and raises an exception if it's invalid.

        Args:
            code (ChoiceCode): The choice code to validate.

        Raises:
            InvalidChoiceCodeError: If the choice code is invalid.
        """
        if not self.is_valid_choice_code(code):
            raise InvalidChoiceCodeError(f"Choice code {code.code} is invalid.")

    def prompt_for_choices(self, format: DisplayFormat) -> str:
        """
        Creates a prompt that displays choices and instructs how to respond.

        Args:
            format (DisplayFormat): The format to display the sections in.

        Returns:
            str: The complete prompt including choices and response instructions.
        """
        choices = self.display(format)
        instructions = (
            "\nResponse Instructions:\n"
            "- Respond ONLY with the numbers of your chosen options\n"
            "- Separate multiple choices with commas\n"
            "- Example valid responses: '1' or '1,3' or '2,4,6'\n"
            "- Do not include any other text or explanations\n"
        )
        return choices + instructions

    def display(self, format: DisplayFormat) -> str:
        """
        Displays all sections in the specified format.

        Args:
            format (DisplayFormat): The format to display the sections in.

        Returns:
            str: The formatted display of all sections.

        Raises:
            NotImplementedError: If the specified format is not supported.
        """
        if format == DisplayFormat.MARKDOWN:
            return "\n\n".join(section.display(format) for section in self.sections)
        else:
            raise NotImplementedError(
                f"Display format '{format.value}' is not supported."
            )

    def validate_choices_response(self, response: str) -> ChoiceCodeSet:
        """
        Validates a choices response string and returns a ChoiceCodeSet.

        Args:
            response (str): The response string containing comma-separated choice numbers.

        Returns:
            ChoiceCodeSet: A set containing the validated choice codes.

        Raises:
            InvalidChoicesResponseError: If any validation checks fail. The error message
                will contain a complete list of all validation problems found.
        """
        errors = []
        choice_set = ChoiceCodeSet()
        
        # Check for empty response
        cleaned = response.strip()
        if not cleaned:
            errors.append("Response cannot be empty")
            raise InvalidChoicesResponseError("Response cannot be empty")

        # Parse and validate number format
        try:
            numbers = [int(num.strip()) for num in cleaned.split(',')]
        except ValueError:
            errors.append("Response must contain only numbers separated by commas")
            raise InvalidChoicesResponseError(errors[0])

        # Track seen numbers to detect duplicates
        seen_numbers = set()
        
        # Validate each number
        for num in numbers:
            # Check for duplicates
            if num in seen_numbers:
                errors.append(f"Choice {num} is duplicated")
            seen_numbers.add(num)
            
            # Validate choice code
            code = ChoiceCode(num)
            if not self.is_valid_choice_code(code):
                errors.append(f"Choice {num} is not a valid option")
                continue

        # If any errors occurred, raise with consolidated message
        if errors:
            error_msg = "\n".join([f"- {err}" for err in errors])
            raise InvalidChoicesResponseError(
                f"Invalid response. The following problems were found:\n{error_msg}"
            )

        # Only create the final set if all validation passed
        for num in numbers:
            choice_set.add(ChoiceCode(num))

        return choice_set
