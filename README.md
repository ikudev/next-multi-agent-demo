# CopilotKit & LangGraph Unified Starter

This project is a high-performance, full-stack starter template for building AI agents. It features a **Next.js** frontend integrated with a **LangGraph** (Python) agent, all deployed as a single unified project on **Vercel**.

## 🚀 Overview

- **Frontend**: Next.js 15+ with Turbopack and CopilotKit for seamless AI integration.
- **Backend (Agent)**: Python 3.12+ LangGraph agent hosted as a Vercel Serverless Function via FastAPI.
- **Package Management**: `npm` for Node.js and `uv` for lightning-fast Python dependency management.
- **Persistent State**: Integrated with LangGraph checkpointers for thread-aware memory.

---

## 💻 Local Development

### 1. Prerequisites
- [Node.js 18+](https://nodejs.org/)
- [uv](https://github.com/astral-sh/uv) (for Python management)
- OpenAI API Key

### 2. Setup
Clone the repository and install all dependencies:

```bash
# Install Node.js dependencies
npm install

# Setup Python environment and dependencies
# The .venv should be at the root, while dependencies are in the api/ folder
uv venv
cd api && uv sync
cd ..
```

### 3. Environment Variables
Create a `.env` file in the **root** directory:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```
*(You can use `example.env` as a reference)*

### 4. Run the Project
Start both the Next.js UI and the LangGraph agent concurrently:
```bash
npm run dev
```
- **Frontend**: [http://localhost:3000](http://localhost:3000)
- **Agent API**: [http://localhost:8123](http://localhost:8123)

---

## ☁️ Deployment on Vercel

This project is designed for "Zero Config" deployment on Vercel.

### 1. Prepare for Deployment
Ensure your code is pushed to a GitHub repository. Vercel will automatically detect the `api/` folder and treat the Python files as serverless functions.

### 2. Configure Vercel Project
1.  **Import** your repository into Vercel.
2.  **Environment Variables**: Add your `OPENAI_API_KEY` in the Vercel Dashboard (Settings > Environment Variables).
3.  **Deployment Protection**: If your project is private, you may need to disable "Vercel Authentication" or provide a bypass token in `src/app/api/copilotkit/route.ts` to allow the Node.js runtime to call the Python functions.

### 3. Verification
Once deployed, your agent should be reachable at:
`https://your-domain.vercel.app/agent/health`

---

## 📁 Project Structure

- `src/app/`: Next.js frontend pages and CopilotKit runtime routes.
- `api/`: The Python agent's "home".
  - `main.py`: The FastAPI server entry point.
  - `agent.py`: The LangGraph logic and graph definition.
  - `pyproject.toml`: Python dependencies (managed by `uv`).
- `vercel.json`: Routing configurations to map `/agent` requests to the Python function.
- `.env`: Unified environment variable file for both frontend and backend.

## 🛠 Available Scripts

- `npm run dev`: Start UI and Agent together (Concurrent).
- `npm run dev:ui`: Start only the Next.js frontend.
- `npm run dev:agent`: Start only the Python agent.
- `npm run lint`: Run ESLint to check for code quality issues.

---

## 📚 Resources

- [CopilotKit Docs](https://docs.copilotkit.ai)
- [LangGraph Docs](https://langchain-ai.github.io/langgraph/)
- [uv Documentation](https://docs.astral.sh/uv/)
