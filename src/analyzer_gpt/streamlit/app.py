import streamlit as st
import asyncio
from src.analyzer_gpt.teams.team_executor import run_team

async def load_app():
    
    st.title("Data Analyzer GPT")
    st.write("This is a Streamlit app for Data Analyzer GPT.")


