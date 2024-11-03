import pytest

from llm_multiple_choice import (
    ChoiceCode,
    ChoiceCodeSet,
    ChoiceManager,
    ChoiceSection,
    DisplayFormat,
    DuplicateChoiceError,
    InvalidChoiceCodeError,
    format_choice_codes,
)


def test_choice_manager() -> None:
    # Initialize the manager
    manager = ChoiceManager()

    # Add a section with an introduction
    section: ChoiceSection = manager.add_section("Assess the sentiment of the messages.")

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

    # Display the choices
    display_content = manager.display(DisplayFormat.MARKDOWN)
    assert isinstance(display_content, str)
    assert "### Assess the sentiment of the messages." in display_content
    assert "**1**: The message expresses positive sentiment." in display_content
    assert "**2**: The message is neutral in sentiment." in display_content
    assert "**3**: The message expresses negative sentiment." in display_content


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


def test_display_empty_section() -> None:
    manager = ChoiceManager()
    section = manager.add_section("Empty Section")
    output = manager.display(DisplayFormat.MARKDOWN)
    assert output == "### Empty Section\n\n"


def test_add_choice_empty_description() -> None:
    manager = ChoiceManager()
    section = manager.add_section("Section")
    with pytest.raises(ValueError):
        section.add_choice("")


def test_choice_code_set_iteration() -> None:
    code_set = ChoiceCodeSet()
    codes = [ChoiceCode(1), ChoiceCode(2), ChoiceCode(3)]
    for code in codes:
        code_set.add(code)

    assert set(code_set) == set(codes)


def test_choice_code_set_immutability() -> None:
    code_set = ChoiceCodeSet()
    code_set.add(ChoiceCode(1))

    frozen_set = code_set.codes
    assert isinstance(frozen_set, frozenset)

    # Attempt to modify the frozenset and verify that it raises an error
    with pytest.raises(AttributeError):
        # Since 'add' is not an attribute of frozenset, trying to access it will raise AttributeError
        getattr(frozen_set, "add")(ChoiceCode(2))
