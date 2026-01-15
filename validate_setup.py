#!/usr/bin/env python3
"""
LangGraph Workshop - Setup Validation Script
Checks dependencies, environment variables, and provides helpful feedback
"""

import sys
import os
from pathlib import Path

def print_header(text):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(text)
    print("=" * 60)

def check_python_version():
    """Check if Python version is 3.10+"""
    print("\n1. Checking Python Version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 10):
        print(f"❌ Python 3.10+ required. Current: {version.major}.{version.minor}")
        print("   Please upgrade Python: https://www.python.org/downloads/")
        return False
    print(f"✅ Python version: {version.major}.{version.minor}.{version.micro}")
    return True

def check_dependencies():
    """Check if required packages are installed"""
    print("\n2. Checking Dependencies...")
    
    required_packages = {
        'langgraph': 'LangGraph (core framework)',
        'langchain_core': 'LangChain Core',
        'langchain_community': 'LangChain Community',
        'langchain_openai': 'LangChain OpenAI',
        'langchain_google_genai': 'LangChain Google GenAI',
        'google_search_results': 'Google Search Results',
        'dotenv': 'Python dotenv',
        'pydantic': 'Pydantic'
    }
    
    missing = []
    for package, description in required_packages.items():
        try:
            __import__(package)
            print(f"✅ {description}")
        except ImportError:
            print(f"❌ {description} - NOT INSTALLED")
            missing.append(package)
    
    if missing:
        print(f"\n⚠️  Missing {len(missing)} package(s)")
        print("   To install, run: pip install -r requirements.txt")
        return False
    
    return True

def check_env_file():
    """Check if .env file exists and has required keys"""
    print("\n3. Checking Environment Configuration...")
    
    env_path = Path('.env')
    if not env_path.exists():
        print("❌ .env file not found")
        print("   Steps to fix:")
        print("   1. Copy .env.example to .env")
        print("   2. Add your API keys to .env")
        return False
    
    print("✅ .env file exists")
    
    # Try to load environment variables
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        print("⚠️  Cannot load .env file (python-dotenv not installed)")
        return False
    
    required_keys = {
        'GOOGLE_API_KEY': 'Google Gemini API',
        'GOOGLE_CSE_ID': 'Google Custom Search Engine ID',
        'MISTRAL_API_KEY': 'Mistral API'
    }
    
    all_configured = True
    for key, description in required_keys.items():
        value = os.getenv(key)
        if not value or 'your_' in value.lower() or '_here' in value.lower():
            print(f"⚠️  {description} ({key}) - Not configured")
            all_configured = False
        else:
            # Show first few characters for verification
            masked_value = value[:4] + "..." + value[-4:] if len(value) > 8 else "****"
            print(f"✅ {description} ({key}): {masked_value}")
    
    if not all_configured:
        print("\n⚠️  Some API keys are not configured")
        print("   Edit .env file and add your actual API keys")
        print("   Get keys from:")
        print("   - Google Gemini: https://aistudio.google.com/")
        print("   - Google Custom Search: https://programmablesearchengine.google.com/")
        print("   - Mistral: https://console.mistral.ai/")
    
    return all_configured

def check_notebooks():
    """Check if workshop notebooks exist"""
    print("\n4. Checking Workshop Notebooks...")
    
    notebooks = [
        'Workshop_agent_v1_basic.ipynb',
        'Workshop_agent_v2_enhanced.ipynb',
        'Workshop_agent_v3_complete.ipynb',
        'Workshop_agent_v4_loops.ipynb',
        'Workshop_agent_simple_v1_learner_version.ipynb'
    ]
    
    all_present = True
    for notebook in notebooks:
        if Path(notebook).exists():
            print(f"✅ {notebook}")
        else:
            print(f"❌ {notebook} - NOT FOUND")
            all_present = False
    
    return all_present

def print_summary(py_ok, deps_ok, env_ok, nb_ok):
    """Print final summary"""
    print_header("Validation Summary")
    
    if py_ok and deps_ok and env_ok and nb_ok:
        print("✅ All checks passed! You're ready for the workshop.")
        print("\nNext steps:")
        print("1. Ensure your virtual environment is activated")
        print("2. Open the first notebook: Workshop_agent_v1_basic.ipynb")
        print("3. Follow along with the workshop")
    else:
        print("⚠️  Some issues found. Please fix them before starting.")
        print("\nIssue Summary:")
        if not py_ok:
            print("❌ Python version: Upgrade to Python 3.10+")
        if not deps_ok:
            print("❌ Dependencies: Run 'pip install -r requirements.txt'")
        if not env_ok:
            print("❌ Environment: Configure .env file with your API keys")
        if not nb_ok:
            print("❌ Notebooks: Ensure all workshop files are present")
        
        print("\nFor detailed help, see README.md or RECOMMENDATIONS.md")
    
    print("=" * 60)

def main():
    """Run all validation checks"""
    print_header("LangGraph Workshop - Setup Validation")
    print("This script will check if your environment is ready for the workshop.")
    
    py_ok = check_python_version()
    deps_ok = check_dependencies()
    env_ok = check_env_file()
    nb_ok = check_notebooks()
    
    print_summary(py_ok, deps_ok, env_ok, nb_ok)
    
    # Return appropriate exit code
    sys.exit(0 if all([py_ok, deps_ok, env_ok, nb_ok]) else 1)

if __name__ == "__main__":
    main()
