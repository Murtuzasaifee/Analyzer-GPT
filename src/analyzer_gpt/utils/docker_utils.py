from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from src.analyzer_gpt.configs.constants import DOCKER_WORK_DIR, DOCKER_TIMEOUT

def getDockerExecutor():
    docker=DockerCommandLineCodeExecutor(
        work_dir=DOCKER_WORK_DIR,
        timeout=DOCKER_TIMEOUT
    )
    return docker
 
 
async def startDockerExecutor(docker):
      await docker.start()
      print("Docker executor started.")
      
      
async def stopDockerExecutor(docker):
      await docker.stop()
      print("Docker executor stopped.")