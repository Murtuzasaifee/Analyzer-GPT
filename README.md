# Analyzer GPT 🤖📊

An intelligent data analysis assistant powered by GPT-4 and AutoGen, designed to analyze CSV data through natural language queries. The system uses multi-agent collaboration to provide comprehensive data insights through both CLI and web interfaces.

## 🌟 Features

- **Natural Language Data Analysis**: Ask questions about your CSV data in plain English
- **Multi-Agent Architecture**: Powered by AutoGen with specialized agents for different tasks
- **Streamlit Web Interface**: User-friendly web app for interactive data analysis
- **Docker Code Execution**: Secure and isolated Python code execution environment
- **Visualization Support**: Generate charts and graphs automatically using matplotlib
- **CLI Support**: Command-line interface for programmatic usage
- **Conversation Memory**: Maintains context across multiple queries

## 🏗️ Architecture

The system consists of two main agents:

### 1. DataAnalyzerAgent 🧑🏻‍💻
- **Role**: Expert data analyst specializing in Python and CSV data analysis
- **Responsibilities**:
  - Creates analysis plans based on user queries
  - Writes Python code to solve data problems
  - Interprets results and provides insights
  - Generates visualizations when requested

### 2. CodeExecutorAgent 🤖
- **Role**: Secure code execution in Docker containers
- **Responsibilities**:
  - Executes Python code in isolated environment
  - Installs required libraries as needed
  - Returns execution results and error messages
  - Manages file operations and outputs

## 🚀 Getting Started

### Prerequisites

- Python 3.12 or higher
- Docker (for code execution)
- OpenAI API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Analyzer GPT"
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Ensure Docker is running**
   ```bash
   docker --version
   ```

### Quick Start

#### Using the Streamlit Web Interface

1. **Run the application**
   ```bash
   streamlit run main.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to the Streamlit URL (typically `http://localhost:8501`)

3. **Upload and analyze**
   - Upload a CSV file using the file uploader
   - Enter your analysis question in the chat input
   - Watch as the AI agents collaborate to analyze your data


## 🛠️ Project Structure

```
Analyzer GPT/
├── src/
│   └── analyzer_gpt/
│       ├── agents/                 # Agent implementations
│       │   ├── data_analyzer_agent.py
│       │   └── code_executor_agent.py
│       ├── configs/                # Configuration files
│       │   └── constants.py
│       ├── model_clients/          # OpenAI client setup
│       │   └── openai_model_client.py
│       ├── prompts/                # Agent prompts
│       │   └── data_analyzer_prompt.py
│       ├── streamlit/              # Web interface
│       │   └── app.py
│       ├── teams/                  # Team orchestration
│       │   ├── data_analyzer_team.py
│       │   └── team_executor.py
│       └── utils/                  # Utility functions
│           ├── docker_utils.py
│           └── logging_config.py
├── main.py                         # Application entry point
├── pyproject.toml                  # Project dependencies
└── README.md                       # This file
```

## ⚙️ Configuration

The system can be configured through `src/analyzer_gpt/configs/constants.py`:

```python
MODEL = 'gpt-4o'                    # OpenAI model to use
TEXT_MENTION_TERMINATION = 'STOP'  # Termination keyword
DOCKER_WORK_DIR = 'tmp'             # Working directory for Docker
DOCKER_TIMEOUT = 120                # Docker execution timeout (seconds)
MAX_TURNS = 15                      # Maximum conversation turns
```

## 🐳 Docker Requirements

The application uses Docker for secure code execution. Ensure Docker is installed and running on your system. The system will automatically:

- Create Docker containers for code execution
- Install required Python packages as needed
- Manage file operations between host and container
- Clean up containers after execution

## 🚨 Important Notes

- **File Handling**: Uploaded CSV files are saved as `data.csv` in the working directory
- **Output Files**: Generated visualizations are saved as `output.png`
- **Security**: Code execution is isolated in Docker containers
- **Dependencies**: Python packages are installed automatically as needed
- **Memory**: The system maintains conversation context during a session

## 🔒 Security Considerations

- All code execution happens in isolated Docker containers
- Temporary files are stored in the `tmp/` directory (gitignored)
- OpenAI API keys should be kept secure and not committed to version control
- Docker containers are automatically cleaned up after execution

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request
