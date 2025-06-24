from autogen_agentchat.agents import AssistantAgent
from src.analyzer_gpt.prompts.data_analyzer_prompt import DATA_ANAYLZER_PROMPT

def getDataAnalyzerAgent(model_client):
    
    data_analyzer_agent = AssistantAgent(
        name='DataAnalyzerAgent',
        description="An expert agent that analyzes data using code execution.",
        model_client=model_client,
        system_message=DATA_ANAYLZER_PROMPT
    )

    return data_analyzer_agent