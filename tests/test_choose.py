from typing import Any
import pytest
from llm_multiple_choice import (
    ChoiceManager,
    ChoiceCode,
    ChoiceCodeSet,
    format_choice_codes,
)

def test_choice_manager() -> None:
    # Initialize the manager
    manager = ChoiceManager()

    # Add a section with an introduction
    section = manager.add_section("Assess the sentiment of the messages.")

    # Add choices to the section
    code1 = section.add_choice("The message expresses positive sentiment.")
    code2 = section.add_choice("The message is neutral in sentiment.")
    code3 = section.add_choice("The message expresses negative sentiment.")

    # Validate choice codes
    assert isinstance(code1, ChoiceCode)
    assert isinstance(code2, ChoiceCode)
    assert isinstance(code3, ChoiceCode)
    assert manager.is_valid_choice_code(code1)
    assert manager.is_valid_choice_code(code2)
    assert manager.is_valid_choice_code(code3)

    # Check that codes are assigned incrementally starting from 1
    assert code1.code == 1
    assert code2.code == 2
    assert code3.code == 3

    # Display the choices (assuming display returns a string for now)
    display_content = manager.display(DisplayFormat.MARKDOWN)
    assert isinstance(display_content, str)

import pytest
from llm_multiple_choice import (
    ChoiceManager,
    ChoiceCode,
    ChoiceCodeSet,
    format_choice_codes,
    DisplayFormat,
    DuplicateChoiceError,
    InvalidChoiceCodeError
)

def test_choice_code_set() -> None:
    # Create a set of choice codes
    code_set = ChoiceCodeSet()

    # Add codes to the set
    code1 = ChoiceCode(1)
    code2 = ChoiceCode(2)
    code3 = ChoiceCode(3)
    code_set.add(code1)
    code_set.add(code2)
    code_set.add(code3)

    # Verify that the codes are in the set
    assert code_set.has(code1)
    assert code_set.has(code2)
    assert code_set.has(code3)

    # Check that adding an existing code raises an exception
    with pytest.raises(DuplicateChoiceError):
        code_set.add(code2)

    assert len(code_set.codes) == 3  # Should still have only 3 codes

    # Format the codes as a string
    formatted_codes = format_choice_codes(code_set)
    assert formatted_codes == "1, 2, 3"

def test_add_duplicate_choice() -> None:
    code_set = ChoiceCodeSet()
    code = ChoiceCode(1)
    code_set.add(code)
    with pytest.raises(DuplicateChoiceError):
        code_set.add(code)

def test_invalid_choice_code() -> None:
    manager = ChoiceManager()
    invalid_code = ChoiceCode(999)
    with pytest.raises(InvalidChoiceCodeError):
        manager.validate_choice_code(invalid_code)

def test_display_unsupported_format() -> None:
    manager = ChoiceManager()
    section = manager.add_section("Introduction")
    with pytest.raises(NotImplementedError):
        section.display(DisplayFormat('unsupported'))

def test_display_empty_section() -> None:
    manager = ChoiceManager()
    section = manager.add_section("Empty Section")
    output = section.display(DisplayFormat.MARKDOWN)
    assert output == "### Empty Section\n\n"

def test_add_choice_empty_description() -> None:
    manager = ChoiceManager()
    section = manager.add_section("Section")
    with pytest.raises(ValueError):
        section.add_choice("")
