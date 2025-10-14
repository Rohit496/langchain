# LangChain Learning Repository

This repository contains my learning materials and examples for LangChain, a framework for developing applications powered by language models.

## Repository Structure

### 📁 Langchain/
Main directory containing organized learning modules:

#### 1. Models Demo (`1.Models_Demo/`)
- **LLMs**: Basic language model examples
- **ChatModels**: Chat-based model implementations (OpenAI, HuggingFace)
- **EmbeddingModels**: Text embedding examples and document similarity

#### 2. Prompts (`2.Prompts/`)
- Static and dynamic prompt templates
- Chatbot implementations with history
- Message placeholders and template management

#### 3. Structured Output (`3.Structure_Output/`)
- TypedDict implementations
- Pydantic model examples
- JSON schema handling

#### 4. Output Parsers (`4.Output_Parsers/`)
- String output parsers
- JSON output parsers
- Structured and Pydantic output parsers

#### 5. Chains (`5.Chains/`)
- Simple chains
- Sequential chains
- Parallel chains
- Conditional chains

#### 6. Runnables (`6.Runnables/`)
- Runnable sequences
- Parallel execution
- Passthrough operations
- Lambda functions
- Branch operations

#### 7. Document Loaders (`7.Document_Loader/`)
- Text file loaders
- PDF processing
- Directory scanning
- Web-based content loading
- CSV file handling

#### 8. Text Splitters (`8.Text_Splitters/`)
- Length-based text splitting techniques

### 📁 IPYNB/
Jupyter notebooks for interactive learning and experimentation

### 📁 Root Files
- `demo.py`: Main demonstration file
- `requirements.txt`: Python dependencies
- `virtual_ENV.md`: Virtual environment setup guide
- Other utility scripts

## Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Rohit496/lanchain.git
cd lanchain
```

2. **Create virtual environment:**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Environment Variables:**
Create a `.env` file and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key
GROQ_API_KEY=your_groq_api_key
```

## Usage

Each directory contains numbered examples that build upon each other. Start with:

1. `Langchain/1.Models_Demo/` - Understanding different model types
2. `Langchain/2.Prompts/` - Learning prompt engineering
3. Continue through the numbered directories in sequence

## Dependencies

Key packages used in this repository:
- `langchain`
- `openai`
- `transformers`
- `pypdf2`
- `beautifulsoup4`
- And more (see `requirements.txt`)

## Contributing

This is a personal learning repository, but feel free to:
- Report issues
- Suggest improvements
- Share your own examples

## License

This project is for educational purposes. Please respect the licenses of the underlying frameworks and models used.

---

Happy learning with LangChain! 🚀