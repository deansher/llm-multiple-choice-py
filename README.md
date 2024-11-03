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
