import json
import requests
import uuid
import os
from typing import Optional, Dict, List
from datetime import datetime
from dotenv import load_dotenv
import sys

# Load environment variables
load_dotenv()

class OpenAI_LLM:
    def __init__(
        self,
        model: str = "gpt-3.5-turbo",
        temperature: float = 0.7,
        max_tokens: int = 2000,
        stream: bool = True,
        top_p: float = 0,
        frequency_penalty: Optional[float] = None,
        presence_penalty: Optional[float] = None,
    ):
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.stream = stream
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.api_key = os.getenv('OPENAI_API_KEY')
        
        if not self.api_key:
            raise ValueError("OPENAI_API_KEY not found in environment variables")

    def _make_request(self, messages: List[Dict]) -> requests.Response:
        """Make request to OpenAI API"""
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        
        payload = {
            "model": self.model,
            "messages": messages,
            "response_format": {"type": "text"},
            "temperature": self.temperature,
            "max_tokens": self.max_tokens,
            "top_p": self.top_p,
            "stream": self.stream
        }

        if self.frequency_penalty is not None:
            payload["frequency_penalty"] = self.frequency_penalty
        if self.presence_penalty is not None:
            payload["presence_penalty"] = self.presence_penalty

        return requests.post(url, headers=headers, json=payload, stream=self.stream)
