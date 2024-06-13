from autoscriptest.models import LineMessage, GoogleChatMessage

def convert_line_message(line_message: LineMessage) -> GoogleChatMessage:
    """Converts a Line message to a Google Chat message"""
    # Replace Line's newline character (\n) with Google Chat's newline character (\\n)
    text = line_message.text.replace("\n", "\\n")
    return GoogleChatMessage(text=text)