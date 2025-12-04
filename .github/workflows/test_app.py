from app import get_message

def test_message():
    assert get_message() == "Hello, CI/CD World!"
