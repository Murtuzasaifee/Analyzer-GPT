
from src.analyzer_gpt.teams.data_analyzer_team import getDataAnalyzerTeam
from src.analyzer_gpt.utils.docker_utils import getDockerExecutor, startDockerExecutor, stopDockerExecutor
from src.analyzer_gpt.model_clients.openai_model_client import getModelClient
from src.analyzer_gpt.agents.code_executor_agent import getCodeExecutorAgent
from src.analyzer_gpt.agents.data_analyzer_agent import getDataAnalyzerAgent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

async def get_team_and_docker():
    
    model_client = getModelClient()
    data_analyzer_agent = getDataAnalyzerAgent(model_client)
    
    docker_executor = getDockerExecutor()
    code_executor_agent = getCodeExecutorAgent(docker_executor)
    
    data_analyzer_team = getDataAnalyzerTeam(data_analyzer_agent, code_executor_agent)
    
    return data_analyzer_team, docker_executor

async def run_team(task):
   
    try:
        
        team,docker = await get_team_and_docker()
        task = task

        await startDockerExecutor(docker)

        async for message in team.run_stream(task = task):
            print('='*50)
            if isinstance(message, TextMessage):
                print(msg:= f" {message.source}: {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:=f'Task Result: {message.stop_reason}')
                yield msg
            print('='*50)


    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        await stopDockerExecutor(docker)