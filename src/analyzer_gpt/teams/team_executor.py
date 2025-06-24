
from src.analyzer_gpt.teams.data_analyzer_team import getDataAnalyzerTeam
from src.analyzer_gpt.utils.docker_utils import getDockerExecutor, startDockerExecutor, stopDockerExecutor
from src.analyzer_gpt.model_clients.openai_model_client import getModelClient
from src.analyzer_gpt.agents.code_executor_agent import getCodeExecutorAgent
from src.analyzer_gpt.agents.data_analyzer_agent import getDataAnalyzerAgent
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult

async def get_team(docker):
    
    model_client = getModelClient()
    
    data_analyzer_agent = getDataAnalyzerAgent(model_client)
    code_executor_agent = getCodeExecutorAgent(docker)
    
    data_analyzer_team = getDataAnalyzerTeam(data_analyzer_agent, code_executor_agent)
    
    return data_analyzer_team


async def runTeam(task, team_state):
   
    try:
        
        docker = getDockerExecutor()
        await startDockerExecutor(docker) 
       
        team = await get_team(docker)
        
        ## Load Team Previous State
        if team_state is not None:
            await team.load_state(team_state)
       
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
        
def save_team_state(team):
    return team.save_state()