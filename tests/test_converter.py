from autoscriptest.converter import convert_line_message_to_google_chat
from autoscriptest.models import LineMessage, GoogleChatMessage

def test_convert_line_message_to_google_chat():
    line_message = LineMessage(text="Hello\nWorld!")
    google_chat_message = convert_line_message_to_google_chat(line_message)
    assert isinstance(google_chat_message, GoogleChatMessage)
    assert google_chat_message.text == "Hello\n\nWorld!"