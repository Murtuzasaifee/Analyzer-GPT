from autogen_agentchat.agents import CodeExecutorAgent



def getCodeExecutorAgent(docker_executor):
    
    code_executor_agent = CodeExecutorAgent(
        name='CodeExecutorAgent',
        description="An agent that executes code in a Docker container.",
        code_executor=docker_executor,
    )
    
    return code_executor_agent