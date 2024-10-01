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

```
    # TBD
```

# Get the answer

```
    # TBD
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Setting Up for Development

TBD

### Editing in VSCode 

<how to specify the python path>

### Running Tests

TBD

### Adding Dependencies

TBD

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
