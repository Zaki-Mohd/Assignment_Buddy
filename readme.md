# 🎓 Assignment Buddy


**Assignment Buddy** is a smart, AI-powered academic assistant built using **Google ADK** (Agent Development Kit). It combines multiple specialized agents to help students solve queries, simplify concepts, fetch research facts, generate formulas, and create quizzes — all with a single input.

---

## 🚀 Features

| Agent                    | Description                                                                 |
|-------------------------|-----------------------------------------------------------------------------|
| 🤖 **Solver Agent**      | Provides accurate academic solutions.                                       |
| 🧠 **Simplifier Agent**  | Breaks down complex answers into simpler explanations.                      |
| 🌐 **Web Research Agent**| Gathers real-time facts and sources from the web.                           |
| 📐 **Formula Finder**    | Detects relevant formulas and explains their use.                           |
| 📝 **Quiz Maker Agent**  | Generates MCQs and practice questions from input text.                      |

---

## 🧠 How It Works

Assignment Buddy uses a `RoutingAgent` that intelligently directs queries to the right combination of sub-agents based on the context and intent of the user’s question. This modular design ensures every response is tailored, accurate, and useful.

---

## 🛠 Tech Stack

- ⚙️ **Google ADK** – Modular AI agent framework.
- 🧠 **Gemini 2.0 Flash** – Lightweight, high-performance LLM.
- 🐍 **Python 3.13** – Core backend logic and orchestration.

---

## 📂 Project Structure

ZAKI_ADK/
└── adk-sample/
    └── agents/
        └── Assignment_Buddy/
            ├── __pycache__/             # Python cache
            ├── __init__.py              # Init file
            ├── agent.py                 # Central routing logic
            └── sub_agents/
                ├── formula_finder_agent/
                ├── quiz_maker_agent/
                ├── simplifier/
                ├── solver/
                └── web_research_agent/
├── .env                                # Environment config
├── .gitignore                          # Git ignore rules
├── CONTRIBUTING.md                     # Contribution guidelines
├── LICENSE                             # Project license
└── readme.md                           # Project readme

---

## ⚡️ Quick Start

> Requirements: Python 3.13+, Google ADK

```bash
# Clone the repository (optional)
git clone https://github.com/yourusername/assignment-buddy.git
cd assignment-buddy

# Run with ADK
adk run agents/Assignment_Buddy



🧪 Example Queries
"Explain Newton's Second Law of Motion" → Solver + Simplifier

"Find acceleration given force and mass" → Formula Finder

"Give me a quiz on photosynthesis" → Quiz Maker

"Research facts about climate change" → Web Research

📜 License
This project is licensed under the Apache License 2.0.

🤝 Contributions
Contributions are welcome! Open a pull request or submit an issue to suggest features or improvements.

Made with 💡 using Google ADK by Zaki
