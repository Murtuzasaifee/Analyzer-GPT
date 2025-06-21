from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from src.analyzer_gpt.configs.constants import DOCKER_WORK_DIR, DOCKER_TIMEOUT

def get_docker_executor():
    docker=DockerCommandLineCodeExecutor(
        work_dir=DOCKER_WORK_DIR,
        timeout=DOCKER_TIMEOUT
    )
    return docker
 
 
async def start_docker_executor(docker):
      await docker.start()
      print("Docker executor started.")
      
      
async def stop_docker_executor(docker):
      await docker.stop()
      print("Docker executor stopped.")