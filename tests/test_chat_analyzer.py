import pytest
from llm_multiple_choice import ChatAnalyzer

def test_chat_analyzer_initialization():
    analyzer = ChatAnalyzer()
    assert isinstance(analyzer, ChatAnalyzer)

def test_chat_analyzer_analyze():
    analyzer = ChatAnalyzer()
    chat = [
        {"role": "user", "content": "Hello, how are you?"},
        {"role": "assistant", "content": "I'm doing well, thank you! How can I assist you today?"},
        {"role": "user", "content": "I'd like to know more about Python programming."},
        {"role": "assistant", "content": "Certainly! Python is a versatile and popular programming language..."}
    ]
    question = {
        "text": "What topic did the user express interest in?",
        "options": [
            "A. Java programming",
            "B. Python programming",
            "C. Web development",
            "D. Data science"
        ]
    }
    answer = analyzer.analyze(chat, question)
    assert answer in ["A", "B", "C", "D"]
