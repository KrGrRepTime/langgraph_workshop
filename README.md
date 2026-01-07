# LangGraph Workshop - Introduction to AI Agents

Welcome to the LangGraph Workshop! This hands-on session introduces the basics of building AI agents with LangGraph in Python.

## Workshop Overview

This workshop covers fundamental concepts for building AI agents using LangGraph. Whether you're new to LangGraph or looking to refresh your knowledge, this session will get you up to speed with:

- Basic agent architecture
- State management
- Tool integration
- Agent loops and workflows

## Prerequisites Setup

### I. Google Gemini API Key

1. Visit [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click "Get API Key" or navigate to the API keys section
4. Create a new API key and copy it

### II. Mistral API Key (Free Tier)

1. Visit [Mistral AI Console](https://console.mistral.ai/)
2. Sign up or log in to your account
3. Navigate to the API Keys section
4. Click "Create new key"
5. Copy your API key
6. **Free tier includes**: Access to Mistral models with generous rate limits for development and testing

### III. Google Custom Search API

1. Create a [Programmable Search Engine](https://programmablesearchengine.google.com/)
   - Make sure to enable "Search the entire web"
   - Copy your Search Engine ID (CSE ID)
2. Go to [Google Cloud Console](https://console.cloud.google.com/)
3. Create a project or select an existing one
4. Enable the Custom Search API
5. Create API credentials from the Credentials page
6. **Free tier includes**: 100 searches per day

### IV. Setup Clean Environment

1. **Create a new project folder** to work in

2. **Create a clean Python environment** by running the following commands in your terminal:

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required packages**:

   ```bash
   pip install langgraph langchain-core langchain-openai google-search-results langchain-google-genai langchain-community langchain-google-community python-dotenv
   ```

5. **Create environment file**:

   - On Windows:
     ```bash
     type nul > .env
     ```
   
   - On macOS/Linux:
     ```bash
     touch .env
     ```

### V. Setup Local Environment Variables

In the `.env` file, add the following lines and fill in your API keys:

```env
GOOGLE_API_KEY=your_google_api_key_here
GOOGLE_CSE_ID=your_custom_search_engine_id_here
MISTRAL_API_KEY=your_mistral_api_key_here
```

**Important**: Never commit your `.env` file to version control. A `.gitignore` file is included in this repository to prevent this.

## Workshop Files

- `Workshop_agent_v1_basic.ipynb` - Basic agent implementation
- `Workshop_agent_v2_enhanced.ipynb` - Enhanced agent features
- `Workshop_agent_v3_complete.ipynb` - Complete agent with all features
- `Workshop_agent_v4_loops.ipynb` - Agent loops and workflows
- `Wokshop_agent_simple_v1 learner_version.ipynb` - Learner practice version

## Getting Started

1. Complete all the prerequisite steps above
2. Ensure your virtual environment is activated
3. Open the first notebook: `Workshop_agent_v1_basic.ipynb`
4. Follow along with the workshop instructor

## Troubleshooting

- **API Key Issues**: Double-check that your keys are correctly copied into the `.env` file
- **Import Errors**: Ensure all packages are installed and your virtual environment is activated
- **Rate Limits**: Be mindful of free tier limits for API calls

## Resources

- [LangGraph Documentation](https://langchain-ai.github.io/langgraph/)
- [LangChain Documentation](https://python.langchain.com/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [Mistral AI Documentation](https://docs.mistral.ai/)

## Support

If you encounter any issues during the workshop, please reach out to the instructor or check the documentation links above.

Happy coding! 🚀
