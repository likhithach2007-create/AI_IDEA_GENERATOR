import streamlit as st
from ollama import chat
st.set_page_config(
    page_title="ProjectGen AI",
    page_icon="💡",
    layout="wide"
)
st.markdown("""
<style>
.stApp {
    background-color: #f5f3ff;
}
.title {
    text-align: center;
    color: #5b21b6;
    font-size: 42px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 30px;
}
.stButton > button {
    width: 100%;
    border-radius: 10px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)
def ask_llama(prompt):
    try:
        response = chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        return response.message.content
    except Exception as e:
        return f"Something went wrong: {e}"
st.markdown(
    '<div class="title">💡 ProjectGen AI</div>',
    unsafe_allow_html=True
)
st.markdown(
    '<div class="subtitle">'
    'Intelligent Project Ideation, Evaluation & Innovation System'
    '</div>',
    unsafe_allow_html=True
)
st.header("🚀 Generate Project Ideas")
col1, col2 = st.columns(2)
with col1:
    domain = st.text_input(
        "📚 Project Domain",
        placeholder="AI, Healthcare, Agriculture..."
    )
    skills = st.text_input(
        "🛠️ Your Skills",
        placeholder="Python, Machine Learning..."
    )
    interests = st.text_input(
        "❤️ Your Interests",
        placeholder="Education, Healthcare..."
    )
with col2:
    team_size = st.number_input(
        "👥 Team Size",
        min_value=1,
        max_value=10,
        value=3
    )
    available_time = st.selectbox(
        "⏳ Available Time",
        ["1 Week", "2 Weeks", "1 Month", "2 Months", "3+ Months"]
    )
    difficulty = st.selectbox(
        "🎯 Difficulty",
        ["Beginner", "Intermediate", "Advanced"]
    )
if st.button("🚀 Generate Project Ideas"):
    if domain.strip() == "":
        st.warning("Please enter a project domain.")
    else:
        prompt = f"""You are an expert engineering project mentor.Generate exactly 3 innovative and realistic college project ideas.
Student details:
Domain: {domain}
Skills: {skills}
Interests: {interests}
Team Size: {team_size}
Available Time: {available_time}
Difficulty: {difficulty}
For each project provide:
1. Project Title
2. Problem Statement
3. Proposed Solution
4. Key Features
5. Technologies
6. Difficulty Level
7. Innovation Score out of 10
8. Feasibility Score out of 10
9. Future Scope
Avoid basic chatbots, simple CRUD applications,attendance systems and calculator projects.Make the ideas practical, innovative and suitable for college students."""
        with st.spinner("🤖 Generating project ideas..."):
            result = ask_llama(prompt)
        st.subheader("✨ Generated Project Ideas")
        st.write(result)
st.divider()
st.header("🔍 Evaluate & Improve an Existing Idea")
existing_idea = st.text_area(
    "💡 Enter your project idea",
    placeholder="Example: AI-based student performance prediction system"
)
if st.button("✨ Evaluate & Improve"):
    if existing_idea.strip() == "":
        st.warning("Please enter a project idea.")
    else:
        prompt = f"""You are an expert engineering project evaluator.Analyze this project idea:
{existing_idea}
Provide:
1. Originality Score out of 10
2. Difficulty Level
3. Feasibility Score out of 10
4. Weak Points
5. Limitations
6. Three Innovative Improvements
Then create the improved version with:
7. Improved Project Title
8. Problem Statement
9. Main Modules
10. Technology Stack
11. Why This Version Is Better
12. Future Scope
Keep the project realistic for college students."""
        with st.spinner("🧠 Evaluating your project..."):
            result = ask_llama(prompt)
        st.subheader("✨ Evaluation & Improved Project")
        st.write(result)