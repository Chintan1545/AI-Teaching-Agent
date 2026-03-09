# 🚀 AI Teaching System 

A **100% free, open-source AI learning assistant** that automatically generates a **complete learning ecosystem for any topic** using multiple AI agents.

This system uses a **multi-agent architecture**, **Retrieval-Augmented Generation (RAG)**, and **web search** to produce:

* 📚 A detailed **knowledge base**
* 🎓 A structured **learning roadmap**
* 🔎 Curated **learning resources**
* 🧪 **Exercises and projects**

All outputs can be **downloaded as files** from the Streamlit interface.

---

# 🧠 System Overview

The system works through **four specialized AI agents**:

### 👨‍🏫 Professor

Creates a **comprehensive knowledge base** including:

* Fundamentals
* Key concepts
* Advanced topics
* Real-world applications

### 🎓 Academic Advisor

Generates a **step-by-step learning roadmap**:

* Beginner → Advanced progression
* Recommended study order
* Estimated time per stage

### 📚 Research Librarian

Finds **learning resources** such as:

* Books
* Courses
* GitHub repositories
* Documentation
* Online tutorials

### 🧪 Teaching Assistant

Creates **practice materials**:

* Exercises
* Quizzes
* Mini-projects
* Real-world problems
* Solutions

---

# ⚙️ Architecture

User Input
↓
Web Search (DuckDuckGo)
↓
Professor Agent
↓
FAISS Vector Database (RAG)
↓
Academic Advisor Agent
↓
Research Librarian Agent
↓
Teaching Assistant Agent
↓
Downloadable Learning Materials

---

# 🧰 Tech Stack

| Component              | Technology            |
| ---------------------- | --------------------- |
| LLM Inference          | Groq                  |
| Model                  | Llama-3               |
| Frontend               | Streamlit             |
| Vector Database        | FAISS                 |
| Embeddings             | Sentence Transformers |
| Web Search             | DuckDuckGo            |
| Environment Management | Conda                 |
| Language               | Python                |

---

# 📂 Project Structure

```
ai_teaching_agent/
│
├── app.py
├── .env
├── README.md
│
└── generated_files/
```

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Chintan1545/ai-teaching-agent.git
cd ai-teaching-agent
```

---

## 2️⃣ Create Conda Environment

```bash
conda create -n ai_teaching_agent python=3.10 -y
conda activate ai_teaching_agent
```

---

## 3️⃣ Install Dependencies

```bash
pip install streamlit groq python-dotenv
pip install langchain faiss-cpu sentence-transformers
pip install duckduckgo-search
```

---

## 4️⃣ Add API Key

Create a `.env` file:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

# ▶️ Run the Application

```bash
streamlit run app.py
```

Then open your browser:

```
http://localhost:8501
```

---

# 🧪 How to Use

1. Enter a topic (example: **Machine Learning**)
2. Click **Start Learning**
3. Wait while the agents generate content
4. Download the generated files

Outputs include:

* Professor report
* Learning roadmap
* Resource list
* Practice exercises

---

# 📥 Example Topics

You can test the system with:

```
Machine Learning
Deep Learning
Python Programming
Artificial Intelligence
Data Science
Computer Vision
```

---

# 💰 Cost

This project is designed to run **at zero cost**.

| Component             | Cost      |
| --------------------- | --------- |
| Groq API              | Free tier |
| FAISS                 | Free      |
| Sentence Transformers | Free      |
| DuckDuckGo Search     | Free      |
| Streamlit             | Free      |

---

# 🧠 Key Features

- ✔ Multi-Agent AI architecture
- ✔ Retrieval-Augmented Generation (RAG)
- ✔ Live web search integration
- ✔ Downloadable learning materials
- ✔ Fully local and free
- ✔ Streamlit UI
- ✔ Clean modular design

---

# 🎯 Use Cases

* AI Learning Assistant
* Educational Platforms
* Personalized Study Planner
* AI Teaching Tools
* AI Portfolio Project

---

# 🧑‍💻 Author

**Chintan Dabhi**

AI / ML Enthusiast
Python Developer

---

# ⭐ Future Improvements

Possible upgrades:

* PDF report generation
* ZIP file downloads
* Chat interface
* Vector database persistence
* Parallel agent execution
* Online deployment

---

# 📜 License

This project is open-source and available under the **MIT License**.
