from datetime import datetime

import pytest

from backend.domain.entites.messages import Message, Chat
from backend.domain.exceptions.messages import TitleToLongException
from backend.domain.values.messages import Text, Title


def test_create_message_success():
    text=Text('Hello world')
    message = Message(text)

    assert message.text == text
    assert message.created_at.date() == datetime.today().date()
def test_create_title_success():
    title = Title('a' * 10)
    chat = Chat(title)

    assert chat.title == title
    assert chat.created_at.date() == datetime.today().date()

def test_create_title_text_too_long():
    with pytest.raises(TitleToLongException):
        title = Title('a' * 400)

def  test_add_message_to_chat():
    title = Title('a' * 10)
    chat = Chat(title)
    message = Message(Text('Hello world'))
    chat.add_message(message)
    assert message in chat.messages




