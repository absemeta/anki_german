from openai import AsyncOpenAI
from .base import BaseTranslator

class OpenAITranslator(BaseTranslator):
    """OpenAI-based translation service."""

    ENV_KEY = "OPENAI_API_KEY"

    def __init__(self, api_key: str):
        super().__init__(api_key)
        self.client = AsyncOpenAI(api_key=api_key)

    def translate(self, text: str, from_lang: str, to_lang: str) -> str:
        # TODO: Implement OpenAI translation
        raise NotImplementedError('not implemented')
