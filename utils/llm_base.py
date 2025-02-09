from abc import ABC, abstractmethod

class LLMBase(ABC):
    @abstractmethod
    def run(self, question: str) -> str:
        pass 