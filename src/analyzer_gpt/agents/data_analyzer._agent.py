from autogen_agentchat.agents import AssistantAgent
from src.analyzer_gpt.prompts.data_analyzer_prompt import DATA_ANAYLZER_PROMPT

def getDataAnalyzerAgent(model_client):
    
    problem_solver_expert = AssistantAgent(
        name='DataAnalyzerAgent',
        description="An expert agent that analyzes data using code execution.",
        model_client=model_client,
        system_message=DATA_ANAYLZER_PROMPT
    )

    return problem_solver_expert