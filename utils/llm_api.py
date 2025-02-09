import requests
from typing import Dict, Any, Optional
from .llm_base import LLMBase

class LLM_API(LLMBase):
    def __init__(self, api_key: str, model: str = "deepseek-ai/DeepSeek-V3"):
        self.url = "https://api.siliconflow.cn/v1/chat/completions"
        self.api_key = api_key
        self.model = model
        
    def _get_default_payload(self, question: str) -> Dict[str, Any]:
        return {
            "model": self.model,
            "messages": [
                {
                    "role": "user",
                    "content": question
                }
            ],
                "stream": False,
                "max_tokens": 512,
                "stop": ["null"],
                "temperature": 0.7,
                "top_p": 0.7,
                "top_k": 50,
                "frequency_penalty": 0.5,
                "n": 1,
                "response_format": {"type": "text"},
                # "tools": [
                #     {
                #         "type": "function",
                #         "function": {
                #             "description": "<string>",
                #             "name": "<string>",
                #             "parameters": {},
                #             "strict": False
                #         }
                #     }
                # ]
            }

    def run(self, question: str, **kwargs) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        payload = self._get_default_payload(question)
        # 更新payload中的参数
        for key, value in kwargs.items():
            if key in payload:
                payload[key] = value
                
        response = requests.request("POST", self.url, json=payload, headers=headers)

        
        return response.text