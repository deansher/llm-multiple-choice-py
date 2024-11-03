#!/bin/bash
set -e

# Run tests
echo "Running tests..."
poetry run pytest

# Run type checking
echo "Running type checking..."
poetry run mypy llm_multiple_choice

# Build the package
echo "Building package..."
poetry build

# Check if --production flag is passed
if [ "$1" == "--production" ]; then
    echo "Publishing to PyPI..."
    poetry publish
else
    echo "Publishing to TestPyPI..."
    poetry config repositories.testpypi https://test.pypi.org/legacy/
    poetry publish -r testpypi
fi

echo "Done!"
