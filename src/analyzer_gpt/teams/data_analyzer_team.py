from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from src.analyzer_gpt.configs.constants import TEXT_MENTION_TERMINATION, MAX_TURNS  


def getDataAnalyzerTeam(data_analyzer_agent, code_executor_agent):
    
    termination_condition = TextMentionTermination(TEXT_MENTION_TERMINATION)
    
    team = RoundRobinGroupChat(
        participants=[data_analyzer_agent, code_executor_agent],
        termination_condition=termination_condition,
        max_turns=MAX_TURNS,
    )
    
    return team
