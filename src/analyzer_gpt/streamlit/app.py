import streamlit as st
import os
from src.analyzer_gpt.configs.constants import DOCKER_WORK_DIR
from src.analyzer_gpt.teams.team_executor import runTeam



if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'autogen_team_state' not in st.session_state:
    st.session_state.autogen_team_state =  None

    
async def load_app():
    
    file = st.file_uploader("Upload a CSV file", type=["csv"])
    task = st.chat_input("Enter your task")
    
    st.title('Analyzer GPT - Data analyzer')

    if task:
        
        try:
            if file is not None and task:
                if not os.path.exists(DOCKER_WORK_DIR):
                    os.makedirs(DOCKER_WORK_DIR)

                with open(f"{DOCKER_WORK_DIR}/data.csv", "wb") as f:
                    f.write(file.getbuffer())
                    
            st.write('Solving your question...')
            
            async for msg in runTeam(task, st.session_state.autogen_team_state):
                print("Message:",msg)
                if msg.startswith(' user'):
                    with st.chat_message('User',avatar='👤'):
                        st.markdown(msg)
                elif msg.startswith(' DataAnalyzerAgent:'):
                    with st.chat_message(' DataAnalyzerAgent:',avatar='🧑🏻‍💻') :
                        st.markdown(msg)
                elif msg.startswith(' CodeExecutorAgent:'):
                    with st.chat_message('CodeExecutorAgent:',avatar='🤖'):
                        st.markdown(msg)
                else:
                    st.markdown(msg)
            
            if os.path.exists(f'{DOCKER_WORK_DIR}/output.png'):
                st.image(f'{DOCKER_WORK_DIR}/output.png',caption='Generated Image')
        
        except  Exception as e:
            print(e)
            st.error("Please upload a file and enter a task")   
        
        

