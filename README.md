# LLM Multiple Choice

A Python library for having an LLM fill out a multiple-choice questionnaire about the current state of a chat.

## Features

- Composible with any LLM provider -- this library does not call the LLM itself.
- Flexible questionnaire structure.
- Simple API for using the questionnaire results in code.

## Installation

You can install the library using pip:

```bash
pip install llm-multiple-choice
```

If you're using Poetry:

```bash
poetry add llm-multiple-choice
```

## Usage

This library helps you create multiple-choice questionnaires for LLMs to fill out. Here's a basic example:

```python
from llm_multiple_choice import ChoiceManager, DisplayFormat

# Create a questionnaire
manager = ChoiceManager()

# Add a section with choices
section = manager.add_section("Assess the sentiment of the message.")
positive = section.add_choice("The message expresses positive sentiment.")
neutral = section.add_choice("The message is neutral in sentiment.")
negative = section.add_choice("The message expresses negative sentiment.")

# Get the prompt to send to your LLM
prompt = manager.prompt_for_choices(DisplayFormat.MARKDOWN)
# The prompt will look like:
# ### Assess the sentiment of the message.
# - **1**: The message expresses positive sentiment.
# - **2**: The message is neutral in sentiment.
# - **3**: The message expresses negative sentiment.
#
# Response Instructions:
# - Respond ONLY with the numbers of your chosen options
# - Separate multiple choices with commas
# - Example valid responses: '1' or '1,3' or '2,4,6'
# - Do not include any other text or explanations

# Send the prompt to your LLM and get its response
llm_response = "2"  # This would come from your LLM

# Validate the response
try:
    choices = manager.validate_choices_response(llm_response)
    if choices.has(neutral):
        print("The message was assessed as neutral.")
except InvalidChoicesResponseError as e:
    print(f"The LLM's response was invalid: {e}")
```

### Creating a Questionnaire

1. Create a `ChoiceManager`:
   ```python
   manager = ChoiceManager()
   ```

2. Add sections and choices:
   ```python
   section = manager.add_section("Your section introduction")
   choice1 = section.add_choice("First choice description")
   choice2 = section.add_choice("Second choice description")
   ```

3. Get the prompt for your LLM:
   ```python
   prompt = manager.prompt_for_choices(DisplayFormat.MARKDOWN)
   ```

### Processing LLM Responses

The library enforces these rules for LLM responses:
- Must contain only numbers corresponding to valid choices
- Numbers must be separated by commas
- Each number can only appear once
- Cannot be empty

Process the response:
```python
try:
    choices = manager.validate_choices_response(llm_response)
    # Check which choices were selected
    if choices.has(choice1):
        print("Choice 1 was selected")
except InvalidChoicesResponseError as e:
    print(f"Invalid response: {e}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Setting Up for Development

To set up the project for development:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/deansher/llm-multiple-choice.git
   ```

2. **Navigate to the project directory**:

   ```bash
   cd llm-multiple-choice
   ```

3. **Install dependencies using Poetry**:

   ```bash
   poetry install
   ```

   This will install all the required packages in a virtual environment.

You can either activate the virtual environment in a shell by running `poetry shell`
or run commands directly using `poetry run <command>`.

### Editing in VSCode

To ensure VSCode uses the correct Python interpreter from the Poetry environment:

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac).
2. Select `Python: Select Interpreter`.
3. Choose the interpreter that corresponds to the project's virtual environment. It should be listed with the path to `.venv`.

If the virtual environment is not listed, you may need to refresh the interpreters or specify the path manually.

### Running Tests

`poetry run pytest`

### Adding Dependencies

To add a new dependency to the project:

- For regular dependencies:

  ```bash
  poetry add <package_name>
  ```

- For development dependencies (e.g., testing tools):

  ```bash
  poetry add --group dev <package_name>
  ```

This updates the `pyproject.toml` and `poetry.lock` files accordingly.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
