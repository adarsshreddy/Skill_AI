
import streamlit as st

from core.llm import ask_gemini, stream_gemini
from prompts.agent_prompts import (
    LEARNING_MENTOR_PROMPT,
    DAILY_PLAN_PROMPT
)

# Page configuration
st.set_page_config(
    page_title="SkillPilot AI",
    page_icon="🚀",
    layout="wide"
)

# Application heading
st.title("🚀 SkillPilot AI")
st.subheader("Your Personal AI Learning Mentor")

st.write(
    "Discover future technologies, learn new skills, "
    "practice coding and track your growth."
)

# Sidebar
with st.sidebar:
    st.title("🎯 My Learning Profile")
    st.write("Level: Beginner")
    st.write("Daily Target: 90 Minutes")

    st.divider()

    st.write("Learning Categories")
    st.write("🤖 Artificial Intelligence")
    st.write("💻 Software Development")
    st.write("🔐 Cybersecurity")
    st.write("☁️ Cloud Computing")
    st.write("📊 Data Science")
    st.write("🚀 Emerging Technologies")

# Dashboard
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Daily Target", "90 min")

with col2:
    st.metric("Learning Level", "Beginner")

with col3:
    st.metric("AI Mentor", "Active")

st.divider()

# Two application sections
tab1, tab2 = st.tabs([
    "📚 Daily Learning Plan",
    "💬 Ask Your AI Mentor"
])

# Daily learning plan
with tab1:
    st.header("Your Personalized Learning Plan")

    st.write(
        "Generate a learning schedule based on your "
        "beginner level and 90-minute daily target."
    )

    if st.button("Generate Today's Learning Plan"):
        with st.spinner("Your AI mentor is preparing your plan..."):
            try:
                result = ask_gemini(
                    LEARNING_MENTOR_PROMPT + "\n\n" +
                    DAILY_PLAN_PROMPT
                )

                st.session_state["daily_plan"] = result

            except Exception as error:
                st.error(f"Something went wrong: {error}")

    if "daily_plan" in st.session_state:
        st.markdown(st.session_state["daily_plan"])


# AI Mentor Chat
with tab2:
    st.header("Ask SkillPilot AI")
    st.caption("Fast AI-powered learning assistant")

    if "messages" not in st.session_state:
        st.session_state["messages"] = []

    # Display previous messages
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_question = st.chat_input(
        "What do you want to learn today?"
    )

    if user_question:

        st.session_state["messages"].append({
            "role": "user",
            "content": user_question
        })

        with st.chat_message("user"):
            st.markdown(user_question)

        with st.chat_message("assistant"):
            try:
                prompt = f"""
                Learner question: {user_question}

                Explain simply with a practical example.
                Keep the answer concise.
                """

                # Stream the answer as it is generated
                answer = st.write_stream(
                    stream_gemini(prompt)
                )

                st.session_state["messages"].append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as error:
                st.error(f"AI error: {error}")
