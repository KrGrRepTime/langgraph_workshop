# LangGraph Workshop - Quick Reference Guide

## 📚 Workshop Structure

### Progressive Learning Path

```
v1: Basic Agent (30 min)
└─→ Single-node Q&A
    └─→ State management basics

v2: Enhanced Agent (45 min)
└─→ Multi-node workflow
    └─→ Web search integration

v3: Complete Agent (1 hour)
└─→ Conditional routing
    └─→ Intelligent enrichment

v4: Advanced Patterns (2-3 hours)
└─→ 5 loop patterns
    └─→ Streaming & persistence
    └─→ Multi-agent systems

Learner Version (1 hour)
└─→ Hands-on practice
```

## 🚀 Quick Start Checklist

- [ ] Python 3.10+ installed
- [ ] Virtual environment created and activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created with API keys
- [ ] Validation script passed (`python validate_setup.py`)
- [ ] First notebook opened (`Workshop_agent_v1_basic.ipynb`)

## 🔑 API Keys Required

| Service | Free Tier | Get Key From |
|---------|-----------|--------------|
| Google Gemini | Yes | https://aistudio.google.com/ |
| Mistral | Yes | https://console.mistral.ai/ |
| Google Custom Search | 100/day | https://programmablesearchengine.google.com/ |

## 📖 Notebook Overview

### v1: Basic Agent
**File:** `Workshop_agent_v1_basic.ipynb`
**Concepts:**
- State with Pydantic BaseModel
- Single node workflow
- LLM integration (Gemini/Mistral)
- Direct Q&A without tools

**Pattern:**
```
User Query → analyze → LLM Response → END
```

---

### v2: Enhanced Agent
**File:** `Workshop_agent_v2_enhanced.ipynb`
**Concepts:**
- Multi-node workflow (3 nodes)
- Web search integration
- Query optimization
- Result synthesis with citations

**Pattern:**
```
User Query → optimize → search → process → END
```

---

### v3: Complete Agent
**File:** `Workshop_agent_v3_complete.ipynb`
**Concepts:**
- Conditional routing (5 nodes)
- LLM-based decisions
- Content enrichment
- Quality-aware processing

**Pattern:**
```
Query → optimize → search → decide → [enrich OR process] → END
```

---

### v4: Advanced Patterns
**File:** `Workshop_agent_v4_loops.ipynb`
**Concepts:**
- Part 1: Fixed iteration loops
- Part 2: Quality-driven loops
- Part 3: Plan-execution research
- Part 4: Streaming & persistence
- Part 5: Multi-agent debate

**Patterns:**
```
Loop Pattern 1: Fixed Iterations
generate → check_count → [continue OR END]

Loop Pattern 2: Quality-Driven
generate → critique → [refine OR END]

Loop Pattern 3: Research
plan → search → evaluate → [continue OR END]

Loop Pattern 4: Streaming
[Any pattern] + real-time monitoring + checkpoints

Loop Pattern 5: Multi-Agent
agent1 → agent2 → consensus_check → [debate OR END]
```

---

### Learner Version
**File:** `Workshop_agent_simple_v1_learner_version.ipynb`
**Purpose:** Hands-on practice with guided exercises
**Status:** Intentionally incomplete (for workshop activities)

## 🎯 Learning Objectives by Version

| Version | You'll Learn |
|---------|-------------|
| v1 | Build basic agent, manage state, integrate LLM |
| v2 | Add external tools, handle API calls, optimize queries |
| v3 | Implement routing, make decisions, enrich content |
| v4 | Create loops, stream events, persist state, build multi-agent systems |

## 💡 Key Concepts

### State Management
```python
class AgentState(BaseModel):
    messages: List[HumanMessage | AIMessage]
    search_results: Optional[List[SearchResult]] = None
    decision: Optional[str] = None
    
    class Config:
        arbitrary_types_allowed = True
```

### Node Definition
```python
def node_function(state: AgentState) -> dict:
    """Process state and return updates"""
    # Your logic here
    return {"messages": [AIMessage(content="result")]}
```

### Graph Construction
```python
workflow = StateGraph(AgentState)
workflow.add_node("node_name", node_function)
workflow.set_entry_point("node_name")
workflow.add_edge("node_name", END)
agent = workflow.compile()
```

### Conditional Routing
```python
def route_decision(state: AgentState) -> str:
    return state.decision  # "option_a" or "option_b"

workflow.add_conditional_edges(
    "decide",
    route_decision,
    {"option_a": "node_a", "option_b": "node_b"}
)
```

### Loop Pattern
```python
def should_continue(state: AgentState) -> str:
    if state.iteration < MAX_ITER:
        return "continue"
    return "end"

workflow.add_conditional_edges(
    "process",
    should_continue,
    {"continue": "process", "end": END}
)
```

## 🛠️ Common Patterns

### 1. Error Handling
```python
try:
    result = api_call()
except Exception as e:
    print(f"Error: {e}")
    result = fallback_value
```

### 2. State Update
```python
return {
    "messages": state.messages + [new_message],
    "field": updated_value
}
```

### 3. Debugging
```python
print(f"[NODE_NAME] Processing...")
print(f"Current state: {state}")
```

### 4. Safety Pattern
```python
MAX_ITERATIONS = 10  # Always have a limit
if iteration >= MAX_ITERATIONS:
    return END
```

## 🔍 Troubleshooting

### Issue: "Module not found"
**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# Reinstall dependencies
pip install -r requirements.txt
```

### Issue: "Invalid API key"
**Solution:**
1. Check `.env` file exists
2. Verify no extra spaces in keys
3. Ensure keys are not placeholder values
4. Restart Jupyter kernel

### Issue: "Rate limit exceeded"
**Solution:**
- Wait a few minutes
- Check free tier limits
- Reduce test query frequency

### Issue: Graph won't compile
**Solution:**
- Verify all nodes are defined
- Check all edges are connected
- Ensure END is reachable
- No circular dependencies

## 📊 Version Comparison

| Feature | v1 | v2 | v3 | v4 |
|---------|----|----|----|----|
| Nodes | 1 | 3 | 5 | Varies |
| Routing | None | Linear | Conditional | Loops |
| Tools | None | Search | Search + Fetch | Any |
| State Fields | 1 | 3 | 4+ | Custom |
| Complexity | ⭐ | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ |
| Production Ready | No | Partially | Yes | Yes |

## 🎓 Best Practices

### DO ✅
- Always activate virtual environment
- Clear notebook outputs before committing
- Use type hints
- Add error handling
- Include max iteration limits in loops
- Print debug messages
- Test with simple queries first

### DON'T ❌
- Commit `.env` file with real keys
- Remove max iteration checks
- Run without error handling
- Exceed free tier rate limits
- Make blocking API calls without timeouts

## 📝 Cheat Sheet

### Essential Imports
```python
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage
from pydantic import BaseModel
from dotenv import load_dotenv
```

### LLM Setup
```python
# Google Gemini
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# Mistral
from langchain_openai import ChatOpenAI
llm = ChatOpenAI(
    base_url="https://api.mistral.ai/v1",
    api_key=os.environ["MISTRAL_API_KEY"],
    model="mistral-large-2512"
)
```

### Search Setup
```python
from langchain_google_community import GoogleSearchAPIWrapper
search = GoogleSearchAPIWrapper(k=3)
results = search.results(query)
```

### Persistence
```python
from langgraph.checkpoint.sqlite import SqliteSaver
memory = SqliteSaver.from_conn_string(":memory:")
agent = workflow.compile(checkpointer=memory)
```

## 🔗 Useful Links

- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [LangChain Docs](https://python.langchain.com/)
- [Pydantic Docs](https://docs.pydantic.dev/)
- [Google Gemini](https://ai.google.dev/docs)
- [Mistral AI](https://docs.mistral.ai/)

## 📂 Repository Files

| File | Purpose |
|------|---------|
| `README.md` | Setup instructions |
| `PROJECT_REVIEW.md` | Comprehensive analysis |
| `RECOMMENDATIONS.md` | Improvement roadmap |
| `requirements.txt` | Dependencies |
| `.env.example` | Environment template |
| `validate_setup.py` | Setup checker |
| `QUICK_REFERENCE.md` | This guide |

## 🎯 Next Steps After Workshop

1. **Practice:** Modify the learner version
2. **Experiment:** Change LLM models, adjust prompts
3. **Build:** Create your own agent for a specific task
4. **Advanced:** Combine patterns from v4
5. **Deploy:** Add FastAPI wrapper for production

## 💪 Practice Exercises

### Beginner
1. Modify v1 to use a different LLM
2. Change the system prompt in v1
3. Add more search results in v2

### Intermediate
4. Add a new state field in v3
5. Implement a custom routing function
6. Create a 3-iteration loop in v4

### Advanced
7. Build a multi-search research agent
8. Implement parallel tool calling
9. Create a custom multi-agent debate system
10. Add Redis persistence for production

---

**Last Updated:** January 15, 2026
**Workshop Version:** 1.0

For detailed information, see the full [PROJECT_REVIEW.md](PROJECT_REVIEW.md).
