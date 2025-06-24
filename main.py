import asyncio
from src.analyzer_gpt.teams.team_executor import runTeam
from src.analyzer_gpt.streamlit.app import load_app


async def main():
    ## Run team via CLI
    # task = 'Analyse from titanic dataset the relationship between age and survival'
    # await run_team(task)
    
    # Run team via Streamlit
    await load_app()
    
    


if __name__ == "__main__":
    # Run the main function using asyncio
    asyncio.run(main())