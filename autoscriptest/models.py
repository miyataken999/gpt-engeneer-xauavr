from dataclasses import dataclass

@dataclass
class LineMessage:
    """Represents a Line message"""
    text: str

@dataclass
class GoogleChatMessage:
    """Represents a Google Chat message"""
    text: str