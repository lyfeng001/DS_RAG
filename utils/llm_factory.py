from typing import Optional
from .llm_base import LLMBase
from .llm_ollama import LLM_Ollama
from .llm_api import LLM_API

class LLMFactory:
    @staticmethod
    def create_llm(llm_type: str, **kwargs) -> LLMBase:

        if llm_type == "ollama":
            return LLM_Ollama(**kwargs)
        elif llm_type == "api":
            if "api_key" not in kwargs:
                raise ValueError("API key is required for API LLM")
            return LLM_API(**kwargs)
        else:
            raise ValueError(f"Unknown LLM type: {llm_type}") 