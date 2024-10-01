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

Here's a basic example of how to use the library:

```python
from llm_multiple_choice import ChatAnalyzer

# Initialize the analyzer
analyzer = ChatAnalyzer()

# Load a chat conversation
chat = [
    {"role": "system" , "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I'm doing well, thank you! How can I assist you today?"},
    {"role": "user", "content": "I'd like to know more about Python programming."},
]

# Define a multiple-choice question

# Define a multiple-choice question
question = {
    "prompt": "What is the sentiment of the user's last message?",
    "choices": {
        "A": "Positive",
        "B": "Neutral",
        "C": "Negative"
    }
}

# Get the answer
answer = analyzer.analyze(chat, question)

print(f"The user's last message sentiment is: {answer}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Setting Up for Development

To set up the project for development:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/llm-multiple-choice.git
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

4. **Activate the virtual environment**:

   ```bash
   poetry shell
   ```

Now you're ready to start developing!

### Editing in VSCode

To ensure VSCode uses the correct Python interpreter from the Poetry environment:

1. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on Mac).
2. Select `Python: Select Interpreter`.
3. Choose the interpreter that corresponds to the project's virtual environment. It should be listed with the path to `.venv`.

If the virtual environment is not listed, you may need to refresh the interpreters or specify the path manually.

### Running Tests

To run the tests:

1. Ensure you're in the virtual environment:

   ```bash
   poetry shell
   ```

2. Run the tests using pytest:

   ```bash
   pytest
   ```

   This will execute all tests located in the `tests/` directory.

### Adding Dependencies

To add a new dependency to the project:

- For regular dependencies:

  ```bash
  poetry add <package_name>
  ```

- For development dependencies (e.g., testing tools):

  ```bash
  poetry add --dev <package_name>
  ```

This updates the `pyproject.toml` and `poetry.lock` files accordingly.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
