import pytest
from llm_multiple_choice import MultipleChoiceManager, ChoiceCodeSet, format_choice_codes

def test_multiple_choice_manager() -> None:
    # Initialize the manager
    manager = MultipleChoiceManager()

    # Add a section with an introduction
    section = manager.add_section("Assess the sentiment of the messages.")

    # Add choices to the section
    code1 = section.add_choice("The message expresses positive sentiment.")
    code2 = section.add_choice("The message is neutral in sentiment.")
    code3 = section.add_choice("The message expresses negative sentiment.")

    # Validate choice codes
    assert manager.is_valid_choice_code(code1)
    assert manager.is_valid_choice_code(code2)
    assert manager.is_valid_choice_code(code3)

    # Check that codes are assigned incrementally starting from 1
    assert code1 == 1
    assert code2 == 2
    assert code3 == 3

    # Display the choices (assuming display returns structured content)
    display_content = manager.display()
    assert isinstance(display_content, dict)  # Replace dict with the expected type if different

def test_choice_code_set() -> None:
    # Create a set of choice codes
    code_set = ChoiceCodeSet()

    # Add codes to the set
    code_set.add(1)
    code_set.add(2)
    code_set.add(3)

    # Verify that the codes are in the set
    assert code_set.has(1)
    assert code_set.has(2)
    assert code_set.has(3)

    # Check that adding an existing code does not duplicate it
    code_set.add(2)
    assert len(code_set.codes) == 3  # Should still have only 3 codes

    # Format the codes as a string
    formatted_codes = format_choice_codes(code_set)
    assert formatted_codes == "1, 2, 3"
