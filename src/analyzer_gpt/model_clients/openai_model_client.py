from autogen_ext.models.openai import OpenAIChatCompletionClient
import os
from dotenv import load_dotenv
from src.analyzer_gpt.configs.constants import MODEL

load_dotenv()

def get_model_client():
    
    api_key = os.getenv("OPENAI_API_KEY")
    
    if not api_key:
        raise ValueError("Please set the OPENAI_API_KEY environment variable.")

    # Initialize the OpenAI model client
    openai_client = OpenAIChatCompletionClient(model=MODEL, api_key=api_key)
    
    return openai_client
