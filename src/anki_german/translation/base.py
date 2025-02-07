import os
from abc import ABC, abstractmethod
from enum import Enum
from typing import Protocol, ClassVar
from dotenv import load_dotenv

load_dotenv()

class Provider(Enum):
    """Available translation service providers."""
    OPENAI = "openai"


class TranslationService(Protocol):
    """Protocol defining the interface for translation services."""
    
    def translate(self, text: str, from_lang: str, to_lang: str) -> str:
        """
        Translate text from one language to another.
        
        Args:
            text: Text to translate
            from_lang: Source language
            to_lang: Target language
            
        Returns:
            Translated text
        """
        pass


class BaseTranslator(ABC):
    """Base class for all translator implementations."""
    
    ENV_KEY: ClassVar[str]  # Each subclass should define its env var key
    
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    @classmethod
    def from_env(cls) -> "BaseTranslator":
        """Create instance using API key from environment variables."""
        api_key = os.getenv(cls.ENV_KEY)
        if not api_key:
            raise ValueError(f"{cls.ENV_KEY} environment variable is not set")
        return cls(api_key)
    
    @abstractmethod
    def translate(self, text: str, from_lang: str, to_lang: str) -> str:
        print("test", text)
        pass 