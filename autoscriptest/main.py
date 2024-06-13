from .converter import convert_line_message_to_google_chat
from .models import LineMessage

def main():
    # Example usage
    line_message = LineMessage(text="Hello\nWorld!")
    google_chat_message = convert_line_message_to_google_chat(line_message)
    print(google_chat_message.text)

if __name__ == "__main__":
    main()