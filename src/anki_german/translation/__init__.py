from .base import TranslationService, Provider
from .openai import OpenAITranslator

def get_translator(provider: Provider) -> TranslationService:
    """
    Factory function to get the appropriate translator.
    
    Args:
        provider: Provider enum specifying which LLM service to use
        
    Returns:
        An instance of TranslationService
    """
    translators = {
        Provider.OPENAI: OpenAITranslator,
    }
    
    if provider not in translators:
        raise ValueError(f"Unsupported provider: {provider}. Choose from {list(translators.keys())}")
    
    return translators[provider].from_env()

__all__ = ['TranslationService', 'OpenAITranslator', 'get_translator', 'Provider'] 