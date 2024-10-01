# LLM Multiple Choice

A Python library for using Large Language Models (LLMs) to fill out multiple-choice questionnaires about chat conversations.

## Features

- Integrate with various LLM providers
- Process chat conversations
- Generate responses for multiple-choice questions
- Customizable question formats and answer options

## Installation

You can install the library using pip:

```bash
pip install llm-multiple-choice
```

## Usage

Here's a basic example of how to use the library:

```python
from llm_multiple_choice import ChatAnalyzer

# Initialize the analyzer
analyzer = ChatAnalyzer()

# Load a chat conversation
chat = [
    {"role": "user", "content": "Hello, how are you?"},
    {"role": "assistant", "content": "I'm doing well, thank you! How can I assist you today?"},
    {"role": "user", "content": "I'd like to know more about Python programming."},
    {"role": "assistant", "content": "Certainly! Python is a versatile and popular programming language..."}
]

# Define a multiple-choice question
question = {
    "text": "What topic did the user express interest in?",
    "options": [
        "A. Java programming",
        "B. Python programming",
        "C. Web development",
        "D. Data science"
    ]
}

# Get the answer
answer = analyzer.analyze(chat, question)
print(f"The answer is: {answer}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.
