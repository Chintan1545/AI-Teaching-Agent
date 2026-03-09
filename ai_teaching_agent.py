import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    st.error("Please add GROQ_API_KEY inside .env file")
    st.stop()

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Page configuration
st.set_page_config(page_title="AI Teaching Agent Team ", layout="centered")

st.title("👨‍🏫 AI Teaching Agent Team ")
st.markdown("Generate a complete learning ecosystem for any topic.")

topic = st.text_input("Enter Topic:", placeholder="e.g., Machine Learning")

# Function to generate response using Groq
def generate_response(system_prompt, user_prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",  # Change to llama3-8b-8192 if rate limited
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7,
        max_tokens=3000,
    )
    return response.choices[0].message.content


# Function to save content to file
def save_to_file(agent_name, content):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{agent_name}_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    return filename


if st.button("Start Learning"):

    if not topic:
        st.warning("Please enter a topic.")
        st.stop()

    # 1️⃣ Professor Agent
    with st.spinner("Professor generating knowledge base..."):
        professor_prompt = """
        You are a Professor.
        Create a detailed knowledge base:
        - Fundamentals
        - Advanced topics
        - Key terminology
        - Real-world applications
        Explain from first principles.
        Format using headings and bullet points.
        """

        professor_response = generate_response(professor_prompt, f"The topic is: {topic}")
        professor_file = save_to_file("Professor", professor_response)

    # 2️⃣ Academic Advisor Agent
    with st.spinner("Academic Advisor generating roadmap..."):
        advisor_prompt = """
        You are an Academic Advisor.
        Create a structured learning roadmap:
        - Beginner to Advanced
        - Ordered progression
        - Estimated time for each phase
        """

        advisor_response = generate_response(advisor_prompt, f"The topic is: {topic}")
        advisor_file = save_to_file("Academic_Advisor", advisor_response)

    # 3️⃣ Research Librarian Agent
    with st.spinner("Research Librarian generating resources..."):
        librarian_prompt = """
        You are a Research Librarian.
        Provide:
        - Books
        - Courses
        - YouTube channels
        - GitHub repositories
        - Official documentation
        Add short descriptions.
        """

        librarian_response = generate_response(librarian_prompt, f"The topic is: {topic}")
        librarian_file = save_to_file("Research_Librarian", librarian_response)

    # 4️⃣ Teaching Assistant Agent
    with st.spinner("Teaching Assistant generating practice materials..."):
        assistant_prompt = """
        You are a Teaching Assistant.
        Create:
        - Exercises
        - Quizzes
        - Mini projects
        - Real-world problems
        Include answers and explanations.
        """

        assistant_response = generate_response(assistant_prompt, f"The topic is: {topic}")
        assistant_file = save_to_file("Teaching_Assistant", assistant_response)

    st.success("All agents completed successfully!")

    st.markdown("## 📥 Download Your Files")

    # Download buttons
    with open(professor_file, "rb") as f:
        st.download_button("Download Professor File", f, professor_file, "text/plain")

    with open(advisor_file, "rb") as f:
        st.download_button("Download Academic Advisor File", f, advisor_file, "text/plain")

    with open(librarian_file, "rb") as f:
        st.download_button("Download Research Librarian File", f, librarian_file, "text/plain")

    with open(assistant_file, "rb") as f:
        st.download_button("Download Teaching Assistant File", f, assistant_file, "text/plain")

    st.markdown("---")

    # Display outputs
    st.markdown("## 👨‍🏫 Professor Output")
    st.markdown(professor_response)

    st.markdown("## 🎓 Academic Advisor Output")
    st.markdown(advisor_response)

    st.markdown("## 📚 Research Librarian Output")
    st.markdown(librarian_response)

    st.markdown("## 🧪 Teaching Assistant Output")
    st.markdown(assistant_response)

